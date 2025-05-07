from django.urls import path
from . views import TaskListView, TaskCreateView, TaskDeleteView

app_name = 'tasks'

urlpatterns = [
    path('projects/<slug:project_slug>/tasks/', TaskListView.as_view(), name='task_list'),
    path('projects/<slug:project_slug>/tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('projects/<slug:project_slug>/tasks/<slug:task_slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
