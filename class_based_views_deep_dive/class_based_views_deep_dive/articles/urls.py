from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    SourceCreateView,
    SourceListView,
    SourceDetailsView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('articles/create/', ArticleCreateView.as_view(), name='create article'),
    path('sources/create/', SourceCreateView.as_view(), name='create source'),
    path('sources/', SourceListView.as_view(), name='sources list'),
    path('sources/<int:pk>', SourceDetailsView.as_view(), name='source details'),
]

