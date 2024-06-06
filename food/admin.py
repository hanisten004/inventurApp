from django.contrib import admin
from .models import Product, Kasten, KastenProduct, Location

admin.site.register(Product)
admin.site.register(Kasten)
admin.site.register(KastenProduct)
admin.site.register(Location)
