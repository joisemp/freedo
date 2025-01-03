from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, 
    PasswordResetCompleteView, PasswordResetConfirmView, 
    PasswordResetDoneView, PasswordResetView
    )
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
    
    
class ResetPasswordView(PasswordResetView):
    email_template_name = 'core/password_reset/password_reset_email.html'
    html_email_template_name = 'core/password_reset/password_reset_email.html'
    subject_template_name = 'core/password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('core:done_password_reset')
    template_name = 'core/password_reset/password_reset_form.html'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['email'].widget.attrs.update({
            'class': 'form-control',
        })
        return form


class DonePasswordResetView(PasswordResetDoneView):
    template_name = 'core/password_reset/password_reset_done.html'


class ConfirmPasswordResetView(PasswordResetConfirmView):
    success_url = reverse_lazy('core:complete_password_reset')
    template_name = 'core/password_reset/password_reset_confirm.html'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        form.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })
        return form


class CompletePasswordResetView(PasswordResetCompleteView):
    template_name = 'core/password_reset/password_reset_complete.html'