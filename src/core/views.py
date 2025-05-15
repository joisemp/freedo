from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

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
        user = form.save(commit=False)
        user.is_active = False 
        user.save()

        token = default_token_generator.make_token(user)
        verification_url = self.request.build_absolute_uri(
            reverse('core:verify_account', kwargs={'uid': user.pk, 'token': token})
        )

        subject = 'Verify Your Account'
        message = render_to_string('core/verify_email.html', {'verification_url': verification_url, 'user': user})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

        return redirect('core:email_sent')
    
    
class VerifyAccountView(View):
    def get(self, request, uid, token):
        user = get_object_or_404(User, pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('core:verified')
        else:
            return HttpResponse('Verification link is invalid or has expired.')
        

class CustomLogoutView(LogoutView):
    template_name = 'core/logout.html'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('landing_page')
    
    
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