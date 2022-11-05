from django.contrib import admin
from .models import Appoinment
# Register your models here.

class SocmAdmin(admin.ModelAdmin):
        list_display = ['id', 'name', 'phone', 'email', 'work', 'date']

admin.site.register(Appoinment, SocmAdmin)
