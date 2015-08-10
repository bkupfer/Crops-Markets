from django.contrib import admin

# Register your models here.
from . import models

# crops
admin.site.register(models.Marker)

# markets
admin.site.register(models.Client)

