from django.urls import path
from . views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView

app_name = 'tasks'

urlpatterns = [
    path('<slug:project_slug>/', TaskListView.as_view(), name='task_list'),
    path('<slug:project_slug>/create/', TaskCreateView.as_view(), name='task_create'),
    path('<slug:project_slug>/update/<slug:task_slug>/', TaskUpdateView.as_view(), name='task_update'),
    path('<slug:project_slug>/delete/<slug:task_slug>/', TaskDeleteView.as_view(), name='task_delete'),
]
