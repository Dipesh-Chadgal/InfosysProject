from django.contrib import admin
from customer.models import customerUser,Feedback

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']

admin.site.register(customerUser,UserAdmin)
# Register your models here.
class Comments(admin.ModelAdmin):
    list_display = ['stars','comments']  

admin.site.register(Feedback, Comments)