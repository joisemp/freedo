from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Task
from projects.models import Project
from . forms import TaskForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(project__freelancer=user).order_by('completed', 'due_date')
    

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    
    def get_success_url(self):
        return reverse('tasks:task_list')
    

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_update_form.html'
    form_class = TaskForm
    slug_field = 'slug'
    slug_url_kwarg = 'task_slug'
    
    def get_success_url(self):
        return reverse('tasks:task_list')
    

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    context_object_name = 'task'
    slug_field = 'slug'
    slug_url_kwarg = 'task_slug'
    
    def get_success_url(self):
        return reverse('tasks:task_list')


class TaskCompleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(slug=kwargs['task_slug'])
        task.completed = True
        task.save()
        return HttpResponseRedirect(reverse('tasks:task_list'))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TaskUncompleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(slug=kwargs['task_slug'])
        task.completed = False
        task.save()
        return HttpResponseRedirect(reverse('tasks:task_list'))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

