from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout,get_user_model
# Create your views here.
from django.shortcuts import render

User = get_user_model()

@login_required()
def menu(request):
    user = request.user

    if hasattr(user, 'customeruser'): 
        name = user.customeruser.name 
    else:
        name = "No name found"      

    return render(request, 'index.html', {'name': name})

