from django.db import models
from django.core.validators import MinValueValidator
from colorfield.fields import ColorField



class Brand(models.Model):

    title = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.title


class Mobile(models.Model):

    SIM_TYPE_CHOICES = [
        ('Single SIM', 'Single SIM'),
        ('Dual SIM', 'Dual SIM'),
        ('eSIM', 'eSIM'),
    ]

    NETWORK_CHOICES = [
        ('2G', '2G'),
        ('3G', '3G'),
        ('4G', '4G'),
        ('5G', '5G'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.IntegerField()
    storage_capacity = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    color = ColorField()
    battery_capacity = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    sim_type = models.CharField(max_length=50, choices=SIM_TYPE_CHOICES)
    network = models.CharField(max_length=50, choices=NETWORK_CHOICES)
    mobile_type = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = ("Mobile")
        verbose_name_plural = ("Mobiles")

    def __str__(self):
        return f"{self.brand.title} {self.model}"
