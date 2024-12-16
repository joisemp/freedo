from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from todo.models import Task
from django.shortcuts import redirect


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = Task.objects.filter(created_by=self.request.user.id)
        return queryset


class TaskCreateView(CreateView):
    model = Task
    fields = ['name',]
    template_name = 'todo/task_create.html'
    
    def form_valid(self, form):
        task = form.save(commit=False)
        print(task.name)
        task.created_by = self.request.user
        task.save()
        return redirect('todo:task_list')
    
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'done']
    template_name = 'todo/task_create.html'
    
    def form_valid(self, form):
        return redirect('todo:task_list')

