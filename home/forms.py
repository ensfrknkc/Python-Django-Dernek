from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={
        'placeholder': 'User Name',
        'class': 'form-control mb-30',
    }))
    email = forms.EmailField(label='E-Mail', widget=forms.TextInput(attrs={
        'placeholder': 'E-Mail',
        'class': 'form-control mb-30',
    }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control mb-30',
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control mb-30',
    }))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'password',
        'class': 'form-control mb-30',
    }))
    password2 = forms.CharField(label='Password Confirm', widget=forms.TextInput(attrs={
        'placeholder': 'Password Confirm',
        'type': 'password',
        'class': 'form-control mb-30',
    }))


class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1','password2',)
