from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.room_number



class Item(models.Model):
    ITEM_TYPES = [
        ("SERVER", "Server"),
        ("PRINTER", "Printer"),
        ("CIRCUIT", "Circuit"),
        ("FURNITURE", "Furniture"),
        ("OTHER", "Other"),
    ]
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    serial_number = models.CharField(max_length=16, 
    validators=[RegexValidator(regex=r'^[A-Za-z0-9]{16}$', message='Serial number must be 16 alphanumeric characters.')])
    demirbas_number = models.CharField(max_length=8, unique=True, 
    validators=[RegexValidator(regex=r'^\d{8}$', message='Demirbas number must be 8 digits.')])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} ({self.demirbas_number})"
