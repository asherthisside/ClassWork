from django.db import models

# Create your models here.
class Kid(models.Model):
    kid_name = models.CharField(max_length=35)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.kid_name


class Toffee(models.Model):
    toffee_name = models.CharField(max_length=35)
    kid = models.OneToOneField(Kid, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.toffee_name


class Language(models.Model):
    lang_name = models.CharField(max_length=35)

    def __str__(self):
        return self.lang_name


class Framework(models.Model):
    frame_name = models.CharField(max_length=35)
    language = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default='Unknown Language')

    def __str__(self):
        return self.frame_name

class Shirt(models.Model):
    shirt_name = models.CharField(max_length=35)

    def __str__(self):
        return self.shirt_name

class Customer(models.Model):
    cust_name = models.CharField(max_length=35)
    shirt = models.ManyToManyField(Shirt)

    def __str__(self):
        return self.cust_name



