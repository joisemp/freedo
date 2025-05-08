from django.urls import path
from .views import PaymentListView, PaymentCreateView, PaymentUpdateView

app_name = 'payments'

urlpatterns = [
    path('<slug:project_slug>/', PaymentListView.as_view(), name='payment_list'),
    path('<slug:project_slug>/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('<slug:project_slug>/update/<slug:payment_slug>/', PaymentUpdateView.as_view(), name='payment_update'),
]