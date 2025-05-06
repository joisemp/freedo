from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Project
from . forms import ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    login_url = reverse_lazy('core:login')

    def get_queryset(self):
        return Project.objects.filter(freelancer=self.request.user)
    

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('projects:project_list')
    login_url = reverse_lazy('core:login')

    def form_valid(self, form):
        project = form.save(commit=False)
        project.freelancer = self.request.user
        project.save()
        return super().form_valid(form)

