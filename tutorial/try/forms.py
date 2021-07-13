from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from .models import Contact
from django.forms import ModelForm


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(SignUpForm, self).save(commit=False)
#         user.username(self.cleaned_data['username'])
#         user.email(self.cleaned_data['email'])
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class SignUpForm()

class LoginForm(forms.Form):
    username = forms.CharField()
    # typically used on senstieve data
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")



    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid error")

        return username



# class SignUpForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Password')
#     password2 = forms.CharField(label='Confirm Password')

#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         qs = User.objects.filter(username__iexact=username)
#         # qs.save()
#         if qs.exists():
#             raise forms.ValidationError("This is an invalid username")

#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         qs = User.objects.filter(email__iexact=email)
#         # qs.save()
#         if qs.exists():
#             raise forms.ValidationError("This is an invalid email")

#         return email

    # def save(self, *args, **kwargs):
    #     u = self.instance.user
    #     u.first_name = self.cleaned_data['username']
    #     u.last_name = self.cleaned_data['password1']
    #     u.save()
    #     return super(SignUpForm, self).save(*args, **kwargs)



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user