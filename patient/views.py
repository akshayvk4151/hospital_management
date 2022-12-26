from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def patient_doc_booking(request):
    return render(request,'patient_templates/doc_booking.html')

def patient_profile(request):
    return render(request,'patient_templates/profile.html')

def patient_booked(request):
    return render(request,'patient_templates/booked.html')
