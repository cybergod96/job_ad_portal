from django.urls import path
from . import views

app_name = 'jobad'

urlpatterns = [
    path('', views.index, name='index'),
    path('ad/<int:ad_id>', views.viewad, name='viewad'),
    path('ad/<int:ad_id>/apply', views.apply, name='apply'),
    path('ad/<int:ad_id>/remove', views.remove_ad, name='remove'),
    path('ad/<int:ad_id>/edit', views.edit_ad, name='edit'),
    path('ad/<int:ad_id>/replies', views.view_replies, name='replies'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_ad, name='add'),
    #path('add/custom', views.add_fields, name='custom')
]
