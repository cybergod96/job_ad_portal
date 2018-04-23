from django.urls import path
from . import views

app_name = 'jobad'

urlpatterns = [
    path('', views.index, name='index'),
    path('ad/<int:id>', views.viewad, name='viewad'),
    path('apply/<int:id>', views.appply, name='apply'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
