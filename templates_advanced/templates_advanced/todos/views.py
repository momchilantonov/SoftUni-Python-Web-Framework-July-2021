from templates_advanced.todos.forms import TodoForm
from templates_advanced.todos.models import Todo
from django.shortcuts import redirect, render


def list_todos(req):
    temp = 'list_todos.html'
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'page_name': 'list_todos',
    }
    return render(req, temp, context)

def create_todo(req):
    temp = 'create_todo.html'
    if req.method == 'GET':
        form = TodoForm()
        context = {
            'form': form,
            'page_name': 'create_todo',
        }
        return render(req, temp, context)
    form = TodoForm(req.POST)
    if form.is_valid():
        form.save()
        return redirect('list todos')
    form = TodoForm()
    context = {
        'form': form,
        'page_name': 'create_todo',
    }
    return render(req, temp, context)
    