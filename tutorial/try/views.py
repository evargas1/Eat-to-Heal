from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.core.mail import send_mail
from django.urls import reverse
# from .models import Contact, ContactForm, Blog
import requests
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, 'try/index.html', context)

def contact(request):
    context = {}
    return render(request, 'try/contact.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('/contact/')
    else:
        if request.method == 'POST':
            formIn = SignUpForm(request.POST)
            if formIn.is_valid():
                
                
                username = formIn.cleaned_data.get('username')
                raw_password = formIn.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                formIn.save(using='db2')
            return HttpResponseRedirect(reverse('contact'))
        else:
            formIn = SignUpForm
    return render(request, 'try/register.html', {'formIn': formIn})

def aboutus(request):
    context = {}
    return render(request, 'try/about-us.html', context)
    

def dashboard(request):
    context = {}
    return render(request, 'try/dashboard.html', context)

def login(request):
    context = {}
    return render(request, 'try/login.html', context)
