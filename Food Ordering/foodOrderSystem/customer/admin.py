from django.contrib import admin
from customer.models import customerUser

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']

admin.site.register(customerUser,UserAdmin)
# Register your models here.
