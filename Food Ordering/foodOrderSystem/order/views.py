from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from restaurant.models import foodItems

# Create your views here.
@login_required
def Cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    print(cart)
    cartDetails = {}
    totalCost = 0
    for items in cart:

        print(cart[items])
        item = foodItems.objects.get(id=items)
        totalCost += cart[items] * item.price
        cartDetails[items] = {"item":item,"quantity":cart[items]}

    return render(request,'cart.html',{'cart':cartDetails,"totalCost":totalCost})
