from django.urls import path
from . views import TaskListView

app_name = 'tasks'

urlpatterns = [
    path('projects/<slug:project_slug>/tasks/', TaskListView.as_view(), name='task_list'),
    # path('projects/<slug:project_slug>/tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    # path('projects/<slug:project_slug>/tasks/create/', TaskCreateView.as_view(), name='task_create'),
    # path('projects/<slug:project_slug>/tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    # path('projects/<slug:project_slug>/tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    # path('projects/<slug:project_slug>/tasks/<int:pk>/complete/', TaskCompleteView.as_view(), name='task_complete'),
    # path('projects/<slug:project_slug>/tasks/<int:pk>/uncomplete/', TaskUncompleteView.as_view(), name='task_uncomplete'
]
