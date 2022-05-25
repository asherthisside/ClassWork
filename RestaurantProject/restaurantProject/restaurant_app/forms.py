from django import forms
from .models import Customer

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'address', 'phone')