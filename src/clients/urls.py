from django.urls import path
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('<slug:client_slug>/', ClientDetailView.as_view(), name='client_detail'),
    path('update/<slug:client_slug>/', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<slug:client_slug>/', ClientDeleteView.as_view(), name='client_delete'),
]