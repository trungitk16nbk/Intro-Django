from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField() 
    gender = models.CharField(max_length=10)
    FlagDel =  models.BooleanField(default = False) 
    
