from django.db import models
from django.contrib.auth.models import User

# Модель User в последствии используется в регистрации
class Account(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
# Модель Product который ипользуется в последствии в товарах и в самой корзине
class Product(models.Model):
    name = models.CharField(max_length=150)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Модель Cart сама корзина
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

