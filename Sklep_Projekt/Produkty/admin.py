from django.contrib import admin
from django.utils.html import format_html
from .models import Produkty, Firma


class ProduktyAdmin(admin.ModelAdmin):
    list_display = ['LeagueName']

admin.site.register(Produkty)

class FirmaAdmin(admin.ModelAdmin):
    list_display = ['LeagueName']

admin.site.register(Firma)