from django.contrib import admin
from django.urls import path 
from .views import EmployeeApiView

urlpatterns = [
    path('employees/', EmployeeApiView.as_view()),
    path('employees/<int:id>', EmployeeApiView.as_view()),
]
