from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from django import forms

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username' : TextInput(attrs={'class': 'form-control mb-30' , 'placeholder':'username'}),
            'email' : EmailInput(attrs={'class': 'form-control mb-30' , 'placeholder':'email'}),
            'first_name' : TextInput(attrs={'class': 'form-control mb-30' , 'placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'form-control mb-30' , 'placeholder':'last_name'}),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'form-control mb-30', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'form-control mb-30', 'placeholder': 'image'}),
        }


