from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('loginUser', views.loginUser, name="login"),
    path('logoutUsers', views.logoutUsers, name="logout"),
]
