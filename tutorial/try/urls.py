from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', views,contact, name='contact'),
    path('signup/', views.signup, name='signup'),
]
