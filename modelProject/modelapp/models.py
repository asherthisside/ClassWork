from statistics import mode
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    std = models.IntegerField()
    address = models.TextField()
    