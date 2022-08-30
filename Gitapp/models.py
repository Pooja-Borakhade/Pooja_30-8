from django.db import models

# Create your models here.

class Hospital(models.Model):
    name =  models.CharField(max_length=200)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)


    class Meta:
        db_table = "Hospital"

