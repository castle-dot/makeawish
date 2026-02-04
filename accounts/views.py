# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm  # or SignUpForm — use whatever name you have


# Signup
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')
    success_message = "Account created successfully! Please log in."


# Login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


# Logout – this is the missing "logged out thing"
class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    http_method_names = ['get', 'post']  # create this template
    
    

# Profile – basic version for now
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = 'accounts:login'