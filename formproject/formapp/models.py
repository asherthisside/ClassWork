from django.db import models

# Create your models here.
class Emails(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)


class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=50)
    staff_phone = models.IntegerField()