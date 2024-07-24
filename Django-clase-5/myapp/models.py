from django.db import models

# Create your models here.

class Person(models.Model):
    document_number = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Customer(models.Model):
    document_number = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    residence_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.document_number} {self.first_name} {self.last_name}"

class Product(models.Model):
    product_code = models.CharField(unique=True, max_length=10)
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(unique=True, max_length=20)
    observations = models.TextField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.product_code} {self.product_name} {self.brand} {self.model} {self.stock}"
    
