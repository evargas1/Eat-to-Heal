from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
# from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'try/index.html', context={})

def aboutus(request):
    # configure and can see
    return render(request, 'try/about-us.html', context={})

def contact(request):
    if request.method == 'POST':
        form = ContactForm()(request.POST)
        form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # some sort of action needs to be performed here
            # (1) save data
            # (2) send an email ####
            # (3) return search result
            # (4) upload a file
            return redirect('try:aboutus')
    else:
        form = ContactForm()


    return render(request, 'try/contact.html', {'form': form})
    # configure and can see
    
@login_required(login_url='/login/')
def dashboard(request):
    if request.method == 'POST':
        auth_logout(request)

        return redirect('/login/')

    return render(request, 'try/dashboard.html', context={})

def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:

        form = AuthenticationForm()
    
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']
            # check if user is in database
            user = authenticate(username=username, password=password)

            if user is not None:
                login_auth(request, user)
                return redirect('/dashboard/')
            else:
                messages.info(request, "username or password is incorrect")
    # configure and can see
    return render(request, 'try/login.html', {'form':form})


def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user.save()
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=user.username, password=raw_password)
    #         auth_login(request, user)
    #         return redirect('')
    # else:
    #     form = SignUpForm()

    return render(request, 'try/register.html', {})