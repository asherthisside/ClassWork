from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        enteredname = request.POST['uname']
        enteredemail = request.POST['uemail']
        userpass = request.POST['upass']
        userpass2 = request.POST['upass2']

        if userpass2 == userpass:
            # Username already exist
            if User.objects.filter(username=enteredname).exists():
                messages.info(request, 'Username already exists')
                return redirect("home")
            # Email already exist
            elif User.objects.filter(email=enteredemail).exists():
                messages.info(request, 'Email already in use')
                return redirect("home")
            else:
                new_user = User.objects.create_user(
                    username=enteredname, email=enteredemail, password=userpass)
                new_user.save()
                return redirect("login")
        else:
            messages.info(request, 'Password does not match')
            return redirect("home")
    else:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        enteredname = request.POST['uname']
        enteredpass = request.POST['upass']
        user = auth.authenticate(username=enteredname, password=enteredpass)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
           messages.info(request, 'Invalid credentials')
           return redirect("login")
    else:
        return render(request, 'login.html')

def dash(request):
    return render(request, 'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

