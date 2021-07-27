from django.contrib import admin

from .models import Article, Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
