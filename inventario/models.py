from django.db import models

class Products(models.Model):
    ean = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
