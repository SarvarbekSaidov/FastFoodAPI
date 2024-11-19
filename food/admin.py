from django.contrib import admin

# Register your models here.
from .models import Supplier, Ingredient, Meal

admin.site.register(Supplier)
admin.site.register(Ingredient)
admin.site.register(Meal)
