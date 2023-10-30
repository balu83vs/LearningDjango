from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class NoteUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()

class Notes(models.Model):
    note = models.TextField()
    username = models.ForeignKey(NoteUser, on_delete=models.CASCADE)
    date = models.DateField(timezone.now())    
