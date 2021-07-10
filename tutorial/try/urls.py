from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),

    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),

    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

]