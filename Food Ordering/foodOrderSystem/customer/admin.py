from django.contrib import admin
from customer.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']

admin.site.register(User,UserAdmin)
# Register your models here.
