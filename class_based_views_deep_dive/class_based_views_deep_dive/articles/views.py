from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

from .models import Article, Source


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'create-article.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class SourceCreateView(CreateView):
    model = Source
    template_name = 'create-source.html'
    fields = '__all__'

    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('source details', kwargs={
            'pk': self.object.id,
        })


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'


# class SourceDetailsView(DetailView):
#     model = Source
#     template_name = 'source-details.html'


class SourceDetailsView(SingleObjectMixin, ListView):
    model = Source
    template_name = 'source-details.html'
    object = None
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Source.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.object
        return context

    def get_queryset(self):
        return self.object.article_set.all()


class SourceListView(ListView):
    model = Source
    template_name = 'sources.html'
    context_object_name = 'sources'
