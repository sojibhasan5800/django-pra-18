from django.shortcuts import render
from .forms import registration_form

# Create your views here.

def singuPpage(request):
    signup_form= registration_form()
    return render(request,'html/signup.html',{'form':signup_form})

