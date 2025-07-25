from django.db import models

# Create your models here.

class Std(models.Model):
    name=models.CharField(max_length=200)
    roll=models.PositiveIntegerField()
    address=models.CharField(max_length=200)
    mail=models.EmailField(max_length=254)
    