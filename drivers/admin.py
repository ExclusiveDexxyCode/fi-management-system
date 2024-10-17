from django.contrib import admin

# Register your models here.
from .models import DriverModel


class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'date_of_birth','championship_won')
    search_field = ('name', 'team')
    
admin.site.register(DriverModel, DriverAdmin)
