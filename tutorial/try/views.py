from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'try/index.html', context={})

def aboutus(request):
    # configure and can see
    return render(request, 'try/about-us.html', context={})

def contact(request):
    # configure and can see
    return render(request, 'try/contact.html', context={})

def dashboard(request):
    return render(request, 'try/dashboard.html', context={})

def login(request):
    # configure and can see
    return render(request, 'try/login.html', context={})

def register(request):
    # configure and can see
    return render(request, 'try/register.html', context={})