from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=3)
    inStock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
