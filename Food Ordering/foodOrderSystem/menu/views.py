from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from restaurant.models import foodItems,restaurantUser

User = get_user_model()

@login_required
def menu(request):
    user = request.user
    foods = foodItems.objects.all()
    cartEmpty = True
    if hasattr(user, 'customeruser'): 
        name = user.customeruser.name 
    else:
        name = "No name found"

    if 'cart' not in request.session:
        request.session['cart'] = {}

    if request.method == 'POST':
        id = request.POST.get("id")
        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] += 1
            cartEmpty = False
        else:
            cart[id] = 1
            cartEmpty = False
        request.session['cart'] = cart

    list_restaurant = restaurantUser.objects.all()
    for i in list_restaurant:

        print(i.restaurantName)

    print('cart', request.session['cart'])
    return render(request, 'index1.html', {'name': name, 'foodItems': foods, 'cart': request.session.get('cart', {}), 'Empty':cartEmpty, 'restaurant_list':list_restaurant})
