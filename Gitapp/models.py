from pyexpat import model
from django.db import models

# Create your models here.


class Hospital(models.Model):
    name =  models.CharField(max_length=200)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)


    class Meta:
        db_table = "Hospital"


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    quali = models.CharField(max_length=100)
    number = models.IntegerField()
    
    class Meta:
        db_name = 'Doctor'
    