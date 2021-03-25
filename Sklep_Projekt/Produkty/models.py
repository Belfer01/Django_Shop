from django.db import models

class Produkty(models.Model):
    nazwa = models.CharField(verbose_name='Elektornika', max_length=30)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=15, decimal_places=2)


class Firma(models.Model):
    nazwa = models.CharField(max_length=120)
    adres =
    opis = models.TextField(blank=True)

