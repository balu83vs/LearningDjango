from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NoteUsers 


class UserRegForm(UserCreationForm):
    class Meta:
        model = NoteUsers
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email'
                  ]
        
class UserLogForm(forms.Form):
    username = forms.CharField() 
    password = forms.CharField(widget=forms.PasswordInput())      