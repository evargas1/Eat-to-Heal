from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.core.mail import send_mail
from django.urls import reverse
# from .models import Contact, ContactForm, Blog
import requests
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm

User = get_user_model()

def index(request):
    context = {}
    return render(request, 'try/index.html', context)

def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user == None:
            # attempt = request.session.get("attemplt") or 0
            # request.session['attempt'] += 1
            request.session['invalid_user'] = 1
            return render(request, "try/login.html", {"form": form})
        auth_login(request, user)
        return HttpResponseRedirect('/dashboard/')

    
    return render(request, 'try/login.html', {"form": form})



def contact(request):

    return render(request, 'try/contact.html', {})


# def signup(request):
#     form = SignUpForm(request.POST or None)
#     if form.is_valid():
        
#         print("is valid")
#         username = form.cleaned_data.get("username")
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password1")
#         password2 = form.cleaned_data.get("password2")
#         try:
#             user = User.objects.create_user(username, email, password)
#             form.save()
#         except:
#             user = None

#         if user != None:
#             auth_login(request, user)
#             form.save()
#             # form.save(commit=false)  
            
#             # attempt = request.session.get("attemplt") or 0
#             # request.session['attempt'] += 1
            
#             return HttpResponseRedirect('/dashboard/')
#         else:
#             request.session['register_error'] = 1
     

    
#     return render(request, 'try/login.html', {"form": form})



def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = formIn.cleaned_data.get('username')
                raw_password = formIn.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            form = SignUpForm
    return render(request, 'try/register.html', {'form': form})



def aboutus(request):
    context = {}
    return render(request, 'try/about-us.html', context)
    

def dashboard(request):
    context = {}
    return render(request, 'try/dashboard.html', context)


