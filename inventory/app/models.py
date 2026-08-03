from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=10, unique=True)
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.room_name



class Item(models.Model):
    MALZEME_ADI = [
        ("SERVER", "Server"),
        ("PRINTER", "Printer"),
        ("CIRCUIT", "Circuit"),
        ("FURNITURE", "Furniture"),
        ("OTHER", "Other"),
    ]
    bakanlik_adi = models.CharField(max_length=100)
    daire_adi = models.CharField(max_length=100, null=True, blank=True)
    malzeme_adi = models.CharField(max_length=20, choices=MALZEME_ADI)
    kiymet = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ayniyat_no = models.CharField(max_length=10, null=True,
    validators=[RegexValidator(regex=r'^\d{6}$', message='Ayniyat number must be 6 digits.')])
    fatura_no = models.CharField(max_length=10, null=True,
    validators=[RegexValidator(regex=r'^\d{6}$', message='Fatura number must be 6 digits.')])
    demirbas_no = models.CharField(max_length=17, unique=True, null=True,
    validators=[RegexValidator(regex=r'^\d{17}$', message='Demirbas number must be 17 digits.')])

    room = models.ForeignKey(Room, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="items"
    )

    aciklama = models.TextField(blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.aciklama} ({self.demirbas_no}) {self.kiymet} TL"
