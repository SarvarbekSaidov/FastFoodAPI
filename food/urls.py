from django.urls import path
from .views import SupplierView, IngredientView, MealView

urlpatterns = [
    path('suppliers/', SupplierView.as_view(), name='suppliers'),
    path('ingredients/', IngredientView.as_view(), name='ingredients'),
    path('meals/', MealView.as_view(), name='meals'),
]
