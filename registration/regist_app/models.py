from django.db import models

# Create your models here.
class Students(models.Model):


    
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    gender=models.CharField()
    nationality = models.CharField()
    city = models.CharField()
    age = models.IntegerField()


