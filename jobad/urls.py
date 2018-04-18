from django.urls import path
from . import views

app_name = 'jobad'

urlpatterns = [
    path('', views.index, name='index'),
]
