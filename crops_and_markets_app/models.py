from django.db import models
from django.utils.encoding import smart_text

class Marker(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.FloatField()
	longitud = models.FloatField()

	def __str__(self):
		return self.name

