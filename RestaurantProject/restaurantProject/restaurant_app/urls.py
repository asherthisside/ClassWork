from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('admin-dashboard/', views.adminDashboard, name='admindash'),
    path('customers/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    path('product/<str:pk>', views.view_product, name='view-product'),
    path('categories/', views.categories, name='categories'),
    path('orders/', views.orders, name='orders'),
]
