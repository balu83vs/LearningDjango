from django import forms
from .models import NoteUsers 


class UserRegForm(forms.ModelForm):
    class Meta:
        model = NoteUsers
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password'
                  ]
        #fields = '__all__'