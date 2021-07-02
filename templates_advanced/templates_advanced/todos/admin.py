from templates_advanced.todos.models import Todo
from django.contrib import admin


@admin.register(Todo)
class TodosAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_done']