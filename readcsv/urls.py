from django.urls import path, include
from .views import index

app_name = 'readcsv'
urlpatterns = [
    path('', index, name='index'),
]
