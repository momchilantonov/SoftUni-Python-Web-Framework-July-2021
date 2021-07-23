from django.contrib import admin

# Register your models here.
from .models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
