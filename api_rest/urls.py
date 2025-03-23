from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_user_by_nick, name='get_user_by_nick'),
]
