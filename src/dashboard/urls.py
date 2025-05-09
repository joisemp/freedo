from django.urls import path

app_name = 'dashboard'

from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]