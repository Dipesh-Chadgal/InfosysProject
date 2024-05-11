from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from random import choice
from customer.models import customerUser

from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def loginUser(request):
    if request.method == 'POST':
        User = get_user_model()
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # if not User.objects.filter(email = username).exists():
        #     messages.error(request,'Username is not in database')
        #     return redirect('login')

        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.error(request,'Invalid Password or Username')
            return redirect('login')
        else:
            login(request,user)
            messages.success(request,'Successfully Login')
            render(request,'authentication/login.html')
            return redirect('menu')


        
    return render(request,'authentication/login.html')

def registerUser(request):
    if request.method == 'POST':
        
        User = get_user_model()
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if customerUser.objects.filter(email= email).exists():
            messages.error(request,'User Already Exist in the System')
            return redirect('login')
        hashed_password = make_password(password)


        try:
            user = customerUser.objects.create(
                name=name,
                email=email,
                username=email,
                password=hashed_password,
                is_user=True
            )
            user.save()
            messages.success(request,'Successfully Registered')
            return redirect('login')
        except:
            messages.error(request,'Error!! Try Again')
            

    return render(request,'authentication/register.html')

def forgetPassword(request):
    return render(request,'authentication/forgetPassword.html')

def logoutUser(request):
    logout(request,User)
    messages.success(request,'Successfully logout')
    return redirect('login')