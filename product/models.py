from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    inStock = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}, {self.inStock}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
