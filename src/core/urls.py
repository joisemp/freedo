from django.urls import path
from django.views.generic import TemplateView
from core import views


app_name = 'core'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
     path('register/', views.UserRegisterView.as_view(), name='register'),
     
     path('verify/<int:uid>/<str:token>/', views.VerifyAccountView.as_view(), name='verify_account'),
     path('email-sent/', TemplateView.as_view(template_name='core/email_sent.html'), name='email_sent'),
     path('verified/', TemplateView.as_view(template_name='core/verified.html'), name='verified'),
     
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
     path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
     path('done-password-reset/', views.DonePasswordResetView.as_view(),
          name='done_password_reset'),
     path('confirm-password-reset/<uidb64>/<token>/',
          views.ConfirmPasswordResetView.as_view(), name='confirm_password_reset'),
     path('complete-password-reset/', views.CompletePasswordResetView.as_view(),
          name='complete_password_reset'),
]

