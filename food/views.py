from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Supplier, Ingredient, Meal
from .serializers import SupplierSerializer, IngredientSerializer, MealSerializer
from .permissions import IsSupplierOrReadOnly

# Create your views here.


class SupplierView(APIView):
    permission_classes = [IsSupplierOrReadOnly]

    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientView(APIView):
    permission_classes = [IsSupplierOrReadOnly]

    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealView(APIView):
    permission_classes = [IsSupplierOrReadOnly]

    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


