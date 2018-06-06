from django.urls import path
from . import views

app_name = 'jobad'

urlpatterns = [
    path('', views.index, name='index'),
    path('ad/<int:ad_id>', views.viewad, name='viewad'),
    path('apply/<int:ad_id>', views.appply, name='apply'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_ad, name='add'),
    path('remove/', views.remove_ad, name='remove'),
    path('edit/', views.edit_ad, name='edit')
]
