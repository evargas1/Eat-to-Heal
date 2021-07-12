from django.db import models
from django.forms import ModelForm

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.name

class AuthorForm(ModelForm):
    model = Author
    fields = ['name', 'title', 'email']

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email
        
