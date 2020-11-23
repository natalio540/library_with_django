from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control','type':'password',}))
    password2 = forms.CharField(label='Repeat Password',widget=forms.TextInput(attrs={'class': 'form-control','type':'password',}))
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
        
        
