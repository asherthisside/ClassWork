from django.shortcuts import render
from .forms import ContactForm, StaffForm
from .models import Emails, Staff

def index(request):
    # bound form 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            entered_name = form.cleaned_data['user_name']
            entered_email = form.cleaned_data['email']
            # print(name, email)
            em = Emails(name=entered_name, email=entered_email)
            em.save()

    # Unbound form 
    form = ContactForm()
    return render(request, 'index.html', {'form_one' : form})


def add(request):
    if request.method == 'POST':
        form2 = StaffForm(request.POST)

        if form2.is_valid():
            entered_name = form2.cleaned_data['staff_name']
            entered_email = form2.cleaned_data['staff_email']
            entered_phone = form2.cleaned_data['staff_phone']
            # print(entered_name, entered_email, entered_phone)
            em = Staff(staff_name=entered_name, staff_email=entered_email, staff_phone=entered_phone)
            em.save()

    addstaff = StaffForm()
    return render(request, 'add-staff.html', {'form2': addstaff})