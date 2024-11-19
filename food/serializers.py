from rest_framework import serializers
from .models import Supplier, Ingredient, Meal

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
