from django.db import models

# Create your models here.

class Articles(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_lenght=200)
    Text = models.TextField()
    Author = models.CharField(max_lenght = 50)
    Category = models.CharField(max_lenght = 50)
    Date = models.DateField()

class Coments(models.Model):
    Author = models.CharField(max_lenght = 50)
    Email = models.EmailField()
    Message = models.TextField()
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE)


