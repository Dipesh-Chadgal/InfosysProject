from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout,get_user_model
from restaurant.models import foodItems
# Create your views here.
from django.shortcuts import render

User = get_user_model()

@login_required
def menu(request):
    user = request.user
    foods = foodItems.objects.all()
    print("my output ",foodItems)

    if hasattr(user, 'customeruser'): 
        name = user.customeruser.name 
    else:
        name = "No name found"      

    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    if request.method == 'POST':
        
        id = request.POST.get("id")
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(id)
            if quantity:
                cart[id] = quantity+1
            else:
                cart[id] = 1
                
        else:
            cart = {}
            cart[id] = 1
        request.session['cart'] = cart
        
    

    print('cart',request.session['cart'])
    return render(request, 'index1.html', {'name': name, 'foodItems':foods})

