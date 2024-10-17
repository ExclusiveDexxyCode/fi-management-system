from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.
class CustomuserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name','password','username','role', 'is_staff')
    search_field = ('id', 'email', 'first_name', 'last_name')
    
    
admin.site.register(User, CustomuserAdmin)
admin.site.unregister(Group)