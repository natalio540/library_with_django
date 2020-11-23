from django import forms
from .models import  clientsTable


class ClientsForm(forms.ModelForm):
     class Meta:
        model = clientsTable
        fields = '__all__'
        
        labels = {
            'name': 'Name',
            'adress': 'Adress',
            'phone': 'Phone',
            'mail': 'Email',
        }
        widgets= {
            'name':forms.TextInput(attrs = {'class':'form-control'}),
            'adress':forms.TextInput(attrs = {'class':'form-control'}),
            'phone':forms.TextInput(attrs = {'class':'form-control'}),
            'email':forms.TextInput(attrs = {'class':'form-control'}),
            
        }