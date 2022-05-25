from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Category(models.Model):
    c_name = models.CharField(max_length=35)
    # icon 
    delivery_charge = models.FloatField()
    time_to_prepare = models.IntegerField()

    def __str__(self):
        return self.c_name 

class Product(models.Model):
    p_name = models.CharField(max_length=60)
    price = models.FloatField()
    description = models.TextField()
    # Image 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.p_name 


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_order_items(self):
        items = self.orderitem_set.all()
        for i in items:
            names = i.product.p_name
            return names

    
    @property 
    def status(self):
        if self.complete == True:
            return "Completed"
        else:
            return "Pending"


    def __str__(self):
        return str(self.id) + " " + self.customer.username

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.p_name + " " + self.order.customer.username