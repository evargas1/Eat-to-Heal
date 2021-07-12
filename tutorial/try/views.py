from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.core.mail import send_mail
from django.urls import reverse
from .models import Contact, ContactForm, Blog
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
        return redirect('/welcome-back/')
    else:
        if request.method == 'POST':
<<<<<<< HEAD

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
=======
            formIn = SignUpForm(request.POST)
            if formIn.is_valid():
                formIn.save()
                username = formIn.cleaned_data.get('username')
                raw_password = formIn.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return HttpResponseRedirect(reverse('contact'))
        else:
            formIn = SignUpForm
    return render(request, 'try/register.html', {'formIn': formIn})
>>>>>>> 43aed833a4ea1066b107400ac664c5c87b296cee
