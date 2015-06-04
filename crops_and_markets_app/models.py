from django.db import models

class Marker(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitud = models.FloatField()

    def __unicode__(self):
        return self.name
