from django.contrib import admin
from django.urls import path
from .views import ShoppingViewClass

urlpatterns = [
    path('products/', ShoppingViewClass.as_view()),
    path('products/<int:id>', ShoppingViewClass.as_view()),
]
