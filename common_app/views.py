from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def common_app_index(request):
    return render(request,'common_app_templates/index.html')

# def common_app_base(request):
#     return render(request,'common_app_templates/base.html')

def common_app_about(request):
    return render(request,'common_app_templates/about.html')

def common_app_contact(request):
    return render(request,'common_app_templates/contact.html')

def common_app_login(request):
    return render(request,'common_app_templates/login.html')

def common_app_register(request):
    return render(request,'common_app_templates/register.html')

def common_app_department(request):
    return render(request,'common_app_templates/department.html')

def common_app_doctors(request):
    return render(request,'common_app_templates/doctors.html')
