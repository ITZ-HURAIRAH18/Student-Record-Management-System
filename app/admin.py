from django.contrib import admin
from .models import Std

class stdAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'address', 'mail']

admin.site.register(Std, stdAdmin)
