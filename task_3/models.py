from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.     

class Users(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80) 
    
    
class Goods(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()    
    

class Token(models.Model):
    key = models.CharField(max_length=100)
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.key