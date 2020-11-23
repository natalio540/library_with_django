from django.urls import path
from ClientsLoans import views

app_name = 'clientsLoans'


urlpatterns = [

    path('clients', views.clients_list, name='clients'),
    path('addclient', views.clients_form, name='addclient'),
    path('delete/<int:id>', views.client_delete, name='client_delete'),
    path('addclient/<int:id>/',views.clients_form, name = 'client_update'),
]