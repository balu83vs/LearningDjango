from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import NoteUser, Notes

class UserRegForm(UserCreationForm):
    class Meta:
        model = NoteUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class UserLogForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
