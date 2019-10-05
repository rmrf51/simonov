# from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView
# from django.views.generic import
from .forms import CustomUserCreationForm


class LoginPageView(LoginView):
    template_name = 'login.html'
    # authentication_form = CustomUserCreationForm
    next = 'home'
