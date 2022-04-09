from django.contrib import admin
from .models import Emails, Staff

# Register your models here.
admin.site.register([Emails, Staff])