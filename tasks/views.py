from django.shortcuts import render, redirect
from tasks.models import Category, Task
from tasks.forms import TaskForm
def main_page_view(request):
    return render(request, 'base.html')

def task_list_view(request):
    tasks = Task.objects.all()
    if request.method == 'GET':
        form = TaskForm(request.GET)
        search = request.GET.get('search')
        if search:
            tasks = tasks.filter(title__icontains=search)

        category = request.GET.get('category')
        if category:
            tasks = tasks.filter(category_id=category)

        ordering = request.GET.get('ordering')
        if ordering:
            tasks = tasks.order_by(ordering)

        categories = Category.objects.all()

        context = {
            'tasks': tasks,
            'form': form,
            'categories': categories,
        }
    
    return render(request, 'task_list.html', context= context)


def task_detail_view(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'task_detail.html', context={'task': task})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            if category is None: 
                form.add_error('category', 'Это поле обязательно.')
            else:
                form.save()
                return redirect('task_list') 

    
    return render(request, 'task_create.html', context={'form': form})