from itertools import product
from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpForm

# Create your views here.
def index(request):
    prods = Product.objects.all()
    return render(request, 'index.html', {'products' : prods})

def view_product(request, pk):
    prod = Product.objects.get(id=pk)
    return render(request, 'view-product.html', {'product' : prod})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            entered_username = form.cleaned_data['username']
            entered_first_name = form.cleaned_data['first_name']
            entered_last_name = form.cleaned_data['last_name']
            entered_address = form.cleaned_data['address']
            entered_phone = form.cleaned_data['phone']

            # print(entered_name, entered_email, entered_phone)

            user = request.user
            cust = Customer(user = user, username = entered_username, first_name = entered_first_name, last_name = entered_last_name, address = entered_address, phone = entered_phone)
            cust.save()

            return redirect("login")
    else: 
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})

def adminDashboard(request):
    return render(request, 'admin-dashboard.html')


def customers(request):
    cust = Customer.objects.all()
    return render(request, 'customers.html', {'customers': cust})

def products(request):
    prods = Product.objects.all()
    return render(request, 'products.html', {'products' : prods})

def categories(request):
    cats = Category.objects.all()
    return render(request, 'categories.html', {'categories': cats})

def orders(request):
    ords = Order.objects.all()
    return render(request, 'orders.html', {'orders': ords})