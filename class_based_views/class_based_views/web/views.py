from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .core.FormMixin import BootStrapFormMixin
from .models import Cat


def index(req):
    context = {
        'title': 'Hello from func views'
    }
    return render(req, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hello from CBV views'
        }


def show_cats(req):
    context = {
        'cats': Cat.objects.all(),
        'cats_title': 'Cats title func view',
    }

    return render(req, 'cats-list.html', context)


class ShowCatsListView(ListView):
    model = Cat
    template_name = 'cats-list.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats_title'] = 'Cats title CBV view'
        return context


class CatCreateView(BootStrapFormMixin, CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'create-cat.html'
    success_url = reverse_lazy('cbv show cats')
    # form_class =
