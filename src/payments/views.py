from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from . models import Payment


class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'
    context_object_name = 'payments'

    def get_queryset(self):
        project_slug = self.kwargs.get('project_slug')
        return Payment.objects.filter(project__slug=project_slug).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context
