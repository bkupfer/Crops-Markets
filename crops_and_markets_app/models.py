from django.db import models
from django.utils.encoding import smart_text


############
# Crops

class Marker(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.FloatField()
	longitud = models.FloatField()

	def __str__(self):
		return self.name


############
# Markets
class Client(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	email = models.EmailField()
	obs = models.CharField(max_length=1000)
	# tamanno, zona, que ha comprado previamente,

	def __str__(self):
		return self.pk