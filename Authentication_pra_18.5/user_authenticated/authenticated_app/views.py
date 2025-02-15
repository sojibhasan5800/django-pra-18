from django.shortcuts import render,redirect
from .forms import registration_form

# Create your views here.

def singuPpage(request):
    if request.method =='POST':      
        signup_form = registration_form(request.POST)
        if signup_form.is_valid():
            data = signup_form.cleaned_data['username']
            print(data)
            print(10)
            return redirect('singup_page')

    signup_form=registration_form()
    return render(request,'html/signup.html',{'form':signup_form})

