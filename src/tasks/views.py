from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        project_slug = self.kwargs.get('project_slug')
        return Task.objects.filter(project__slug=project_slug).order_by('-completed', 'due_date')

