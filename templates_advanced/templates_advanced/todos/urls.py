from templates_advanced.todos.views import create_todo, list_todos
from django.urls import path


urlpatterns = [
    path('', list_todos, name='list todos'),
    path('create/', create_todo, name='create todo'),
]