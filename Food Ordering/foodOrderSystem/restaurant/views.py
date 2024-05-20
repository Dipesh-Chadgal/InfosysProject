from django.shortcuts import render,redirect
from django.http import HttpResponse
from restaurant.models import restaurantUser,foodItems
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
        restaurant_data = restaurantUser(restaurantName=restaurantName,
                                     address=address,
                                     restaurantContact=restaurantContact,
                                     email=email,
                                     password=make_password(password))
        restaurant_data.save()
        return redirect('loginRestaurant')

    return render(request,'registerRestaurant.html')


def testing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        item = foodItems(name=name, price=price, image=image)
        item.save()
        return HttpResponse('Successfully uploaded')
    return render(request, 'addMenu.html')