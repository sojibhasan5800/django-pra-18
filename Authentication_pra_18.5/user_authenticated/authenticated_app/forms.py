from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm

class registration_form(UserCreationForm):

    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        help_texts={
            'username':None,
        }
        lables={
            'first_name':'F_name',
        }
        