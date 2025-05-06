from django.urls import path
from . views import ProjectListView, ProjectCreateView, ProjectDetailView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<slug:project_slug>/', ProjectDetailView.as_view(), name='project_detail'),
]