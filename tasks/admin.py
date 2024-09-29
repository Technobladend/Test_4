from django.contrib import admin
from tasks.models import Category, Task
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    list_display_links = ('title', 'description', 'created_at')
    list_filter = ('category',)
