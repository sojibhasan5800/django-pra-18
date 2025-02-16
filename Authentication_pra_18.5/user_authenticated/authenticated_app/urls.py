
from django.urls import path
from .views import singuPpage
from .views import loginpage


urlpatterns = [
    path('signuppage/',singuPpage,name="signup_page"),
    path('loginpage/',loginpage,name="login_page"),
]
