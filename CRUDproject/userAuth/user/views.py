from django.shortcuts import render
from django.contrib.auth.models import auth, User

# Create your views here.
def index(request):
    return render(request, 'index.html')