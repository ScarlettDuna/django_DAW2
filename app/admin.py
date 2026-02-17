
# Register your models here.
from django.contrib import admin
from .models import Proveedor, Topping, Pizza

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Proveedor)
