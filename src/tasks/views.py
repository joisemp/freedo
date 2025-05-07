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
        project_slug = self.kwargs.get('project_slug')
        return Task.objects.filter(project__slug=project_slug).order_by('-completed', 'due_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context
    

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save(commit=False)
        task.project = Project.objects.get(slug=self.kwargs['project_slug'])
        task.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context
    
    def get_success_url(self):
        return reverse('tasks:task_list', kwargs={'project_slug':self.kwargs['project_slug']})
    

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_update_form.html'
    form_class = TaskForm
    slug_field = 'slug'
    slug_url_kwarg = 'task_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context
    
    def get_success_url(self):
        return reverse('tasks:task_list', kwargs={'project_slug':self.kwargs['project_slug']})
    

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    context_object_name = 'task'
    slug_field = 'slug'
    slug_url_kwarg = 'task_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_slug"] = self.kwargs['project_slug']
        return context
    
    def get_success_url(self):
        return reverse('tasks:task_list', kwargs={'project_slug':self.kwargs['project_slug']})


class TaskCompleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(slug=kwargs['task_slug'])
        task.completed = True
        task.save()
        return HttpResponseRedirect(reverse('tasks:task_list', kwargs={'project_slug': kwargs['project_slug']}))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TaskUncompleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(slug=kwargs['task_slug'])
        task.completed = False
        task.save()
        return HttpResponseRedirect(reverse('tasks:task_list', kwargs={'project_slug': kwargs['project_slug']}))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

