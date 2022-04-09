from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Welcome<h1>")

def about(request):
    return render(request, 'about.html')

def intro(request):
    # user_name = "Monika"
    # designation = "Senior Python Developer"

    context = {
        'uname' : "Haaris", 
        'des' : "ABC"
    }
    return render(request, 'myintro.html', context)

def userdata(request):
    return render(request, 'form.html')

def dashboard(request):
    # uname = request.GET['username']
    # password = request.GET['password']
    uname = request.POST['username']
    password = request.POST['password']
    context = {
        'uname' : uname,
        'pass' : password
    }
    return render(request, 'dashboard.html', context)

def posts(request):
    post_numbers = [1, 2, 3, 4, 5, 6]
    return render(request, 'posts.html', {'posts' : post_numbers})

def dynpost(request, pk):
    return render(request, 'dynpost.html', {'key' : pk})