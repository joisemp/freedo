from django.urls import path
from .views import DashboardView, DashboardFilterView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('filter/', DashboardFilterView.as_view(), name='filter'),
]