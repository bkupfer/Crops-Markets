from django.contrib import admin
from . import models

# general
admin.site.register(models.GeoMarker)

# crops
# admin.site.register(models.Marker)

# markets
admin.site.register(models.Client)
admin.site.register(models.TypeOfClient)
admin.site.register(models.ComercialInfo)
