from django.urls import path
from todo.views import TaskListView, TaskCreateView, TaskUpdateView

app_name = 'todo'

urlpatterns=[
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
]