from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show(request):
    stds = Student.objects.filter(name="Monika")
    return render(request, 'data.html', {'stud': stds})