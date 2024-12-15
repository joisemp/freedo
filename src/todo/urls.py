from django.urls import path
from todo.views import TaskListView, TaskCreateView

app_name = 'todo'

urlpatterns=[
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
]