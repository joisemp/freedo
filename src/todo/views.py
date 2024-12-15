from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from todo.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = Task.objects.filter(created_by=self.request.user.id)
        return queryset

