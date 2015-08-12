from django.db import models
from django.utils.encoding import smart_text

# Crops
class Marker(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.FloatField()
	longitud = models.FloatField()

	def __str__(self):
		return self.name


# Markets
class Client(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	contact_number_1 = models.IntegerField(blank=True, null=True)
	contact_number_2 = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	observations = models.TextField(blank=True, null=True)
	# agregar: tamanno, zona, que ha comprado previamente, etc etc...

	def __str__(self):
		return self.first_name + " " + self.last_name
