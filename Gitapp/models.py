from pyexpat import model
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    quali = models.CharField(max_length=100)
    number = models.IntegerField()
    
    class Meta:
        db_name = 'Doctor'
    