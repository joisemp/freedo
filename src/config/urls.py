from django.contrib import admin
from django.urls import path, include
from core.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('core/', include('core.urls', namespace='core')),
    path('todos/', include('todo.urls', namespace='todo')),
]
