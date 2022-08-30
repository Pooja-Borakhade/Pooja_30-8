from pyexpat import model
from django.db import models

# Create your models here.
<<<<<<< HEAD

class Hospital(models.Model):
    name =  models.CharField(max_length=200)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)


    class Meta:
        db_table = "Hospital"

=======
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    quali = models.CharField(max_length=100)
    number = models.IntegerField()
    
    class Meta:
        db_name = 'Doctor'
    
>>>>>>> 70b425b398e3b44ec35cafa3ed4a9a699a2e5082
