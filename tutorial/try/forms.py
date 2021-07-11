from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import CustomUser


# class SignUpForm(UserCreationForm):
#     full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
#     email = forms.EmailField(max_length=254)

#     class Meta:
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('full_name', 'email',)

    
# you do not have to register this in the admin panel
# it will automatically appear. 