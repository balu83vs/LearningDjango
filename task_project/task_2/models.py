from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class NoteUsers(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    #def create_user(self, data):
    #    self.username = data['username']
    #    self.first_name = data['first_name']
    #    self.last_name = data['last_name']
    #    self.email = data['email']
    #    self.set_password(data['password1']) 
    #    self.save()

      
class Notes(models.Model):
    note_text = models.TextField()  
    username = models.ForeignKey(NoteUsers, on_delete=models.CASCADE)

    def new_note(self, data, curent_user):
        self.note_text = data  
        self.username = curent_user
        self.save()