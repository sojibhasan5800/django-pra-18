from django.shortcuts import render,redirect
from .forms import registration_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def singuPpage(request):
    if request.method =='POST':      
        signup_form = registration_form(request.POST)
        if signup_form.is_valid():
            messages.success(request, 'Account created successfully')
            signup_form.save()
            print(signup_form.changed_data)
            return redirect('signup_page')        
    else:
        signup_form=registration_form()
    signup_form=registration_form()
    return render(request,'html/signup.html',{'form':signup_form, 'type':"Register"})

def loginpage(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.info(request,'Login Successfully')
                login(request,user)
                return redirect('profile_page')
            else:
                messages.success(request,'Invalid Username and password')
                return redirect('login_page')
    else:
        login_form = AuthenticationForm()
    return render(request,'html/signup.html',{'form':login_form,'type':'Login'})


