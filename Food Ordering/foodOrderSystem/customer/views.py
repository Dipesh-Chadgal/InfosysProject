from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from customer.models import User
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username,password)


        
    return render(request,'authentication/login.html')

def registerUser(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User(name=name,email=email,password=password)
        user.save()
    return render(request,'authentication/register.html')

def forgetPassword(request):
    return render(request,'authentication/forgetPassword.html')