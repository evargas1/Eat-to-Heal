from django.shortcuts import render
from django.shortcuts import render, redirect
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
    # configure and can see
    return render(request, 'try/login.html', context={})

def register(request):
    # configure and can see
    return render(request, 'try/register.html', context={})