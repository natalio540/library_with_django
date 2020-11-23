from django import forms
from .models import booksTable
from loansApp.models import loansTable
 #clientsTable, loansTable

class BookForm(forms.ModelForm):
    # name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'titulo'}))
    #  message = forms.CharField(widget = forms.Textarea(attrs={'class':'#add class name', 'placeholder':'If you require'}))
    class Meta:
        model = booksTable
        fields = ['name', 'author']
        
        labels = {
            'name': 'Titulo',
            'author': 'Autor'
        }
        widgets= {
            'name':forms.TextInput(attrs = {'class':'form-control'}),
            'author':forms.TextInput(attrs = {'class':'form-control'}),
            
        }




loan_status= [('borrowed','borrowed'),('returned','returned')]
class BookLoanForm(forms.ModelForm):
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
            # 'bookLoan': forms.Select(attrs = {'class':'form-control'}),
            'clientLoan': forms.Select(attrs = {'class':'form-control'}),
            'dateLoan': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
            'dateReturn': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
            'status': forms.Select(choices=loan_status, attrs = {'class':'form-control'}),
        }




# class ClientsForm(forms.ModelForm):
#     class Meta:
#         model = clientsTable
#         fields = '__all__'
       


   
# class LoansForm(forms.ModelForm):
#     class Meta():
#         model = loansTable
#         fields = ['bookLoan','clientLoan','dateLoan','dateReturn']
#         labels={
#             'bookLoan':'Book',
#             'clientLoan':'Client',
#             'dateLoan':'Date',
#             'dateReturn':'Return',
#         }
#         widgets = {
#             'bookLoan': forms.Select(attrs = {'class':'form-control'}),
#             'clientLoan': forms.Select(attrs = {'class':'form-control'}),
#             'dateLoan': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
#             'dateReturn': forms.TextInput(attrs = {'class':'form-control','type':'date'}),
#         }