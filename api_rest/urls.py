from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user_list/', views.user_list, name='user_list'),
    path('', views.user_registration_page, name='get_all_users'),
    path('user/<str:nick>/', views.get_by_nick, name='get_by_nick'),
    path('data/', views.user_manager, name='user_manager'),
    path('create/', views.create_user, name='create_user'),
    path('update/<str:nick>/', views.update_user, name='update_user'),
    path('delete/<str:nick>/', views.delete_user, name='delete_user'),
    path('success/', views.user_success_page, name='success'),  
    path('register/', views.user_registration_page, name='register'), 
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout')
]
