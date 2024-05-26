from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from restaurant.models import foodItems
from django.http import JsonResponse
import json


@login_required
def cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    cart_details = {}
    total_cost = 0
    for item_id, quantity in cart.items():
        item = foodItems.objects.get(id=item_id)
        total_cost += quantity * item.price
        cart_details[item_id] = {"item": item, "quantity": quantity}

    return render(request, 'cart.html', {'cart': cart_details, "total_cost": total_cost})

@login_required
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        action = data.get('action')

        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session['cart']

        if action == 'increment':
            cart[item_id] = cart.get(item_id, 0) + 1
        elif action == 'decrement':
            if cart[item_id] > 1:
                cart[item_id] -= 1
            else:
                del cart[item_id]
        elif action == 'remove':
            del cart[item_id]

        request.session.modified = True
        total_cost = sum(foodItems.objects.get(id=int(item_id)).price * quantity for item_id, quantity in cart.items())
        return JsonResponse({'total_cost': f'Rs. {total_cost}'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def payment(request):
    # print(Cart.totalCost)
    return render(request,'payment.html') 