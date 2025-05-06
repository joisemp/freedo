from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Client
from . forms import ClientForm


class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    
class ClientCreateView(CreateView):
    model = Client
    template_name = 'clients/client_form.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')  
    
    def form_valid(self, form):
        client = form.save(commit=False)
        client.freelancer = self.request.user
        client.save()
        return super().form_valid(form)
    
class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/client_form.html'
    form_class = ClientForm
    slug_field = 'slug'
    slug_url_kwarg = 'client_slug'
    success_url = reverse_lazy('clients:client_list')
      
