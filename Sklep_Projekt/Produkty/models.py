from django.db import models

IDEA_STATUS= (
    ('pending','Waiting for review'),
    ('accepted','Accepted'),
    ('done','Done'),
    ('rejected','Rejected')
)

class Produkty(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'dużY'),
        (MEDIUM, 'średni'),
        (SMALL, 'małY'),
)
    nazwa = models.CharField(verbose_name='Elektornika', max_length=30)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=15, decimal_places=2)




class Meta:
    verbose_name = "Kategoria"
    verbose_name_plural = "Kategorie"


def __unicode__(self):
    return self.name

class Firma(models.Model):
    nazwa = models.CharField(max_length=120)
    NIP = models.CharField(max_length=10)
    miasto = models.CharField(max_length=30)
    opis = models.TextField(verbose_name='Treść')



    def __unicode__(self):
        return self.title
