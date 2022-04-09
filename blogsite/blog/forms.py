from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=500000)
