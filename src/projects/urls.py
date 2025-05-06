from django.urls import path
from . views import ProjectListView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    # Add other URL patterns for project detail, create, update, delete views here
]