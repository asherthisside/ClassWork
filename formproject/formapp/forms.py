from django import forms
from .models import Staff

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=50, label="Please enter your name")
    password = forms.CharField(max_length=10, widget=forms.PasswordInput, required=False)
    email = forms.EmailField()
    category = forms.ChoiceField(choices=[
        ('', 'Select One'),  
        ('query', 'Query'),  
        ('complaint', 'Complaint'), 
        ('other', 'Other')
        ])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea, required=False)
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
    

# >>> CHOICES = [('1', 'First'), ('2', 'Second')]
# >>> choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)