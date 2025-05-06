from django.urls import path
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('update/<slug:client_slug>/', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<slug:client_slug>/', ClientDeleteView.as_view(), name='client_delete'),
]