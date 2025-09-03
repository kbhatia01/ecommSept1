from django.db import models
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
        ]


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(stock__gte=0), name="stock_stock_greater_than0"
            )
        ]


