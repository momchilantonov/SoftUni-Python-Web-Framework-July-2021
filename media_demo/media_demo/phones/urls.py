
from media_demo.phones.views import create_phone, index
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('create/', create_phone, name='create phone')

]