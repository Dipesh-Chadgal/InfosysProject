from django.shortcuts import render,redirect
from restaurant.models import Restaurant
from django.contrib.auth.hashers import make_password
# Create your views here.


def loginRestaurant(request):
    return render(request,'loginRestaurant.html')

def registerRestaurant(request):
    if request.method == 'POST':
        
        restaurantName = request.POST.get('restaurantName')
        address = request.POST.get('address')
        restaurantContact = request.POST.get('restaurantContact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        restaurant_data = Restaurant(restaurantName=restaurantName,
                                     address=address,
                                     restaurantContact=restaurantContact,
                                     email=email,
                                     password=make_password(password))
        restaurant_data.save()
        return redirect('loginRestaurant')

    return render(request,'registerRestaurant.html')
