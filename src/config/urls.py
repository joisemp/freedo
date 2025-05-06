from django.contrib import admin
from django.urls import path, include
from core.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('core/', include('core.urls', namespace='core')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
]
