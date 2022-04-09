from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    department = models.CharField(max_length=10)
    salary = models.IntegerField()
