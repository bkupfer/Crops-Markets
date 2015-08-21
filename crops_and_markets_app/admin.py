from django.contrib import admin
from . import models

# general

# crops
# admin.site.register(models.Marker)

# markets
admin.site.register(models.Client)
admin.site.register(models.TypeOfClient)
admin.site.register(models.ComercialInfo)
admin.site.register(models.GeographicInfo)
