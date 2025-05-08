from django.urls import path
from .views import PaymentListView

app_name = 'payments'

urlpatterns = [
    path('<slug:project_slug>/', PaymentListView.as_view(), name='payment_list'),
]