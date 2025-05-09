from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from projects.models import Project
from . models import Payment

from . forms import PaymentForm

class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'
    context_object_name = 'payments'
    

class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'payments/payment_form.html'
    form_class = PaymentForm

    def get_success_url(self):
        return reverse('payments:payment_list')
    

class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = 'payments/payment_update_form.html'
    form_class = PaymentForm
    slug_field = 'slug'
    slug_url_kwarg = 'payment_slug'

    def get_success_url(self):
        return reverse('payments:payment_list')  
    

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payments/payment_confirm_delete.html'
    context_object_name = 'payment'
    slug_field = 'slug'
    slug_url_kwarg = 'payment_slug'

    def get_success_url(self):
        return reverse('payments:payment_list')  

