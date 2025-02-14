
from django.urls import path
from .views import singuPpage


urlpatterns = [
    path('signuppage',singuPpage,name="signup_page")
]
