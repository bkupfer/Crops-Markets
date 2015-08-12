from django.contrib import admin
from . import models

# general

# crops
admin.site.register(models.Marker)

# markets
admin.site.register(models.Client)
