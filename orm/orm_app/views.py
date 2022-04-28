from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    kids = Kid.objects.all()
    context = {'all_kids' : kids}
    return render(request, 'index.html', context)