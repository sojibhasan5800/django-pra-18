from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registration_form(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'id': 'required'}))
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1']
        help_texts = {
            'password1': 'Password must be at least 8 characters.',
            'password2': 'Enter the same password for confirmation.',
        }
        labels = {  # ✅ Correct spelling
            'first_name': 'F_name',  # Change "First Name" label to "F_name"
        }
        error_messages={
            'username': {
                'required': 'Please enter a username2.',
                'invalid':'place@',
                'unique': 'This username is already taken. Please choose another one.',
        }
        }
