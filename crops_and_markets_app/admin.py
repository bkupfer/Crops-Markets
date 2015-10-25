from django.contrib import admin
from . import models

# general
admin.site.register(models.Region)
admin.site.register(models.Province)
admin.site.register(models.Commune)
admin.site.register(models.PotatoVariety)

# crops
admin.site.register(models.CompanyCrop)
admin.site.register(models.Crop)
admin.site.register(models.CropOwner)
admin.site.register(models.CropImage)

# markets
admin.site.register(models.Client)
admin.site.register(models.CompanyMarket)
admin.site.register(models.GeoMarker)
admin.site.register(models.Sale)
admin.site.register(models.SaleDetail)
admin.site.register(models.TypeOfClient)

# relateds
admin.site.register(models.Related)
