from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from core.forms import CustomAuthenticationForm, UserRegisterForm

User = get_user_model()


class LandingPageView(TemplateView):
    template_name = 'landing_page.html'


class LoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'core/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('landing_page')
    

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('landing_page')
    

class LogoutView(LogoutView):
    template_name = 'core/logout.html'
    
    
class ChangePasswordView(PasswordChangeView):
    template_name = 'core/change_password.html'
    success_url = reverse_lazy('landing_page')
    