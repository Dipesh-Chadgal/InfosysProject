from django.contrib import admin
from restaurant.views import foodItems

class ItemsList(admin.ModelAdmin):
    list_display = ['name','price','image']  

admin.site.register(foodItems, ItemsList)