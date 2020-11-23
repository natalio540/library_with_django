from django.urls import path
from loansApp import views 


app_name = 'loansApp'

urlpatterns = [
    path('loans', views.loans_list, name = 'loans'),
    path('addloan/', views.loan_add, name='addloan'),
    path('delete/<int:id>', views.loan_delete, name='loan_delete'),
    path('addloan/<int:id>/',views.loan_update, name = 'loan_update'),
]

