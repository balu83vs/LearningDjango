from rest_framework import serializers
from .models import Notes, NoteUser


class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = NoteUser
        fields = ["id", "username", "first_name", "last_name", "email"] 

class NoteSerialiser(serializers.ModelSerializer):   
    author = UserSerializer() 
    class Meta:
        model = Notes
        fields = ["id", "note", "date", "author"]        

        
             



