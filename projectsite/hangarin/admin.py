from django.contrib import admin

from .models import Task, Priority, Category, Note, SubTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description')

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('priority_name',)
    search_fields = ('priority_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_task', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('sub_title', 'sub_status', 'parent_task',)
    list_filter = ('sub_status',)
    search_fields = ('sub_title',)