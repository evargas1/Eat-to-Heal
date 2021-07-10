from django.contrib import admin
from .models import Contact
from .forms import SignUpForm

# Register your models here.
admin.site.register(Contact)
admin.site.register(SignUpForm)