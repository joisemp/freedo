from django.urls import path
from core.views import LoginView, UserRegisterView, LogoutView


app_name = 'core'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]

