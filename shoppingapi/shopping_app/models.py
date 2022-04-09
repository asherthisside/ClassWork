from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()

    class Meta:
        db_table = "products"