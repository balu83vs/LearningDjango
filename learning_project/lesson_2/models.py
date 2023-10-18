from django.db import models

# Create your models here.
class Articles(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.CharField(max_length = 50)
    Categories = models.CharField(max_length=50)
    Date = models.DateField()

class Comments(models.Model):
    Author = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()
    Article = models.ForeignKey(Articles, on_delete=models.CASCADE)


