from django.urls import path
from .views import PaymentListView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView

app_name = 'payments'

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment_list'),
    path('create/', PaymentCreateView.as_view(), name='payment_create'),
    path('<slug:payment_slug>/update/', PaymentUpdateView.as_view(), name='payment_update'),
    path('<slug:payment_slug>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),
]