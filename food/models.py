from django.db import models

# Create your models here.
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, related_name='ingredients', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    restock_threshold = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.name} ({self.stock_quantity} units)"

class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, related_name='meals')
    preparation_time = models.DurationField()

    def __str__(self):
        return self.name
