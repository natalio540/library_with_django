from django import forms
from .models import loansTable



loan_status= [('borrowed','borrowed'),('returned','returned')]

class LoansForm(forms.ModelForm):
    class Meta():
        model = loansTable
        fields = ['bookLoan','clientLoan','dateLoan','dateReturn','status']
        labels={
            'bookLoan':'Book',
            'clientLoan':'Client',
            'dateLoan':'Date',
            'dateReturn':'Return',
            'status': 'Status',
        }
        widgets = {
            'bookLoan': forms.Select(attrs = {'class':'form-control'}),
            'clientLoan': forms.Select(attrs = {'class':'form-control'}),
            'dateLoan': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
            'dateReturn': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
            'status': forms.Select(choices=loan_status, attrs = {'class':'form-control'}),
        }

class LoansFormUpdate(forms.ModelForm):
    class Meta():
        model = loansTable
        fields = ['dateReturn','status']
        labels={
            'dateReturn':'Return',
            'status': 'Status',
        }
        widgets = {
            'dateReturn': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
            'status': forms.Select(choices=loan_status, attrs = {'class':'form-control'}),
        }        