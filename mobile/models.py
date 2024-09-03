from django.db import models
from colorfield.fields import ColorField



class Brand(models.Model):

    title = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.title


class Mobile(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    storage_capacity = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    color = ColorField()
    battery_capacity = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    sim_type = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    mobile_type = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = ("Mobile")
        verbose_name_plural = ("Mobiles")

    def __str__(self):
        return f"{self.brand.title} {self.model}"
