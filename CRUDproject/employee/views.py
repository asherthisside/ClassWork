from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['empname']
        userdepartment = request.POST['empdepartment']
        usersalary = request.POST['empsalary']
        emp = Employee(name=username, department=userdepartment, salary=usersalary)
        emp.save()
        return redirect("dashboard")

    else:
        return render(request, 'index.html')

def show(request):
    details = Employee.objects.all()
    return render(request, 'dashboard.html', {'userdetails' : details})

def edit(request, pk):
    employee = Employee.objects.get(id=pk)
    return render(request, 'edit.html', {'details' : employee})

def update(request, pk):
    newname = request.POST['empname']
    newdepartment = request.POST['empdepartment']
    newsalary = request.POST['empsalary']
    employee = Employee.objects.get(id=pk)
    employee.name = newname
    employee.department = newdepartment
    employee.salary = newsalary
    employee.save()
    return redirect("dashboard")

def delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect("/dashboard")