from django.urls import path
from . views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskCompleteView, TaskUncompleteView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<slug:task_slug>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<slug:task_slug>/', TaskDeleteView.as_view(), name='task_delete'),
    path('complete/<slug:task_slug>/', TaskCompleteView.as_view(), name='task_complete'),
    path('uncomplete/<slug:task_slug>/', TaskUncompleteView.as_view(), name='task_uncomplete'),
]
