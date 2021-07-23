from django.apps import AppConfig
from django.db.models import BigAutoField


class PythonsAuthConfig(AppConfig, BigAutoField):
    name = 'pythons.pythons_auth'
