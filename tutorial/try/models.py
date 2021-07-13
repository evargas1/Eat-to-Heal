from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# Create your models here.


SUBJECT_CHOICES = [
    ('Questions', 'Questions'),
    ('Book Consulation', 'Book Consulation'),
    ('Request More Reviews', 'Request More Reviews'),
    ('Contact a Specialist', 'Contact a Specialist'),
    ('Bussiness Inquery', 'Bussiness Inquery')
   

]

class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    sender = models.EmailField()

    def __str__(self):
        return self.name



class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields = ('name', 'subject', 'sender')
        
        help_texts = {
            'sender':_('We will contact you soon'),
        }
        error_messages = {
            'name': {
                'max_length':_("Just you first name will suffice!"),
            },
        }

