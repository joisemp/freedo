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

    def get_queryset(self):
        project_slug = self.kwargs.get('project_slug')
        return Payment.objects.filter(project__slug=project_slug).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context
    

class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'payments/payment_form.html'
    form_class = PaymentForm

    def form_valid(self, form):
        payment = form.save(commit=False)
        payment.project = Project.objects.get(slug=self.kwargs['project_slug'])
        payment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context

    def get_success_url(self):
        return reverse('payments:payment_list', kwargs={'project_slug':self.kwargs['project_slug']})
    

class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = 'payments/payment_update_form.html'
    form_class = PaymentForm
    slug_field = 'slug'
    slug_url_kwarg = 'payment_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context

    def get_success_url(self):
        return reverse('payments:payment_list', kwargs={'project_slug':self.kwargs['project_slug']})  
    

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payments/payment_confirm_delete.html'
    context_object_name = 'payment'
    slug_field = 'slug'
    slug_url_kwarg = 'payment_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context

    def get_success_url(self):
        return reverse('payments:payment_list', kwargs={'project_slug':self.kwargs['project_slug']})  

