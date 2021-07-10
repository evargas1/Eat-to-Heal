from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, ContactForm
# Create your views here.
def index(request):
    return render(request, 'try/index.html', context={})

def aboutus(request):
    # configure and can see
    return render(request, 'try/about-us.html', context={})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            # some sort of action needs to be performed here
            # (1) save data
            # (2) send an email ####
            # (3) return search result
            # (4) upload a file
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ContactForm()


    return render(request, 'try/contact.html', {'form': form})
    # configure and can see
    

def dashboard(request):
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
                auth_login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                messages.info(request, "username or password is incorrect")
    # configure and can see
    return render(request, 'try/login.html', {'form':form})

def register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        if request.method == 'POST':
            formIn = SignUpForm(request.POST)
            if formIn.is_valid():
                formIn.save()
                username = formIn.cleaned_data.get('username')
                raw_password = formIn.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login_auth(request, user)
                return redirect('/dashboard/')
        else:
            formIn = SignUpForm
    return render(request, 'try/register.html', {'formIn': formIn})