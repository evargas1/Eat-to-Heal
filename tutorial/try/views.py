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
from .models import Contact, ContactForm

User = get_user_model()

def index(request):
    context = {}
    return render(request, 'try/index.html', context)

# def login(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")

#         user = authenticate(request, username=username, password=password)
#         if user == None:
#             # attempt = request.session.get("attemplt") or 0
#             # request.session['attempt'] += 1
#             request.session['invalid_user'] = 1
#             return render(request, "try/login.html", {"form": form})
#         auth_login(request, user)
#         return HttpResponseRedirect('/dashboard/')

    
#     return render(request, 'try/login.html', {"form": form})


def aboutus(request):
    context = {}
    return render(request, 'try/about-us.html', context)


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
            return HttpResponseRedirect(reverse('aboutus'))
    else:
        form = ContactForm()
    context = {}
    return render(request, 'try/contact.html', context)



def login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:

        # form = AuthenticationForm()
    
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            # check if user is in database
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/dashboard/')
            else:
                messages.info(request, "username or password is incorrect")
       
    return render(request, 'try/login.html', context)




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
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            form = SignUpForm
            context = {}
    return render(request, 'try/register.html', {})



    

@login_required(login_url='/login/')
def dashboard(request):
    if request.method == 'POST':
        auth_logout(request)

        return redirect('/login/')
    context = {}
    return render(request, 'try/dashboard.html', context)


