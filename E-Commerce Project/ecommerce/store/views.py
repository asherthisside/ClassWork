from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")

def store(request):
    if request.user.is_authenticated:
        this_customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=this_customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'all_products' : products, 'no_of_products': cartItems}
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        this_customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=this_customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']
    context = {'all_items' : items, 'order_key' : order, 'no_of_products': cartItems}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        this_customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=this_customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']
    context = {'all_items' : items, 'order_key' : order, 'no_of_products': cartItems}
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


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()

    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        print("User is not logged in")

    total = data['form']['total']
    order.transaction_id = transaction_id

    print(total, order.get_cart_total)

    # if total == order.get_cart_total:
    order.complete = True 
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer, 
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
    return JsonResponse("Order Completed", safe=False)