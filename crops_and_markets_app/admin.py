from django.contrib import admin
from . import models

# general

# crops
admin.site.register(models.Crop)
admin.site.register(models.CropOwner)
admin.site.register(models.Paddock)

# markets
admin.site.register(models.Client)
admin.site.register(models.ComercialInfo)
admin.site.register(models.GeoMarker)
admin.site.register(models.TypeOfClient)
