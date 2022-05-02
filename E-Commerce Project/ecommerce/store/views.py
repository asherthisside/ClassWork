from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def store(request):
    products = Product.objects.all()
    context = {'all_products' : products}
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        this_customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=this_customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
    context = {'all_items' : items, 'order_key' : order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        this_customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=this_customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
    context = {'all_items' : items, 'order_key' : order}
    return render(request, 'checkout.html', context)

def update_order(request):
    data = json.loads(request.body)

    pr_id = data['productId']
    act = data['action']

    # print('Product Id:', pr_id)
    # print('Action:', act)

    customer = request.user.customer 
    product = Product.objects.get(id=pr_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if act == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif act == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Product Added", safe=False)