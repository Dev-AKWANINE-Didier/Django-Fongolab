from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, null=True)
    
    
    def __str__(self):
        return f"{self.first_name} - {self.email}"
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
