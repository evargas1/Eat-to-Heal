from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.index, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    
]
