from django.db import models
from django.utils.encoding import smart_text

# ######## #
# Crops	
# class Marker(models.Model):
#	name = models.CharField(max_length=100)
#	latitude = models.FloatField()
#	longitud = models.FloatField()
#
#	def __str__(self):
#		return self.name
#
# ###


# ######## #
# Markets
class Client(models.Model):
	type_of_client = models.ForeignKey('TypeOfClient')

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	contact_number_1 = models.IntegerField(blank=True, null=True)
	contact_number_2 = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	observations = models.TextField(blank=True, null=True)

	comercial_info = models.ForeignKey('ComercialInfo') # check if this foreign key should be here, or it should be all the way down into comercialInfo

	def __str__(self):
		return self.first_name + " " + self.last_name


class TypeOfClient(models.Model):
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type
		

class ComercialInfo(models.Model): # should it be renamed to -ComercialInformation- ?
	zone = models.CharField(max_length=256, blanck=True, null=True)
	volume = models.CharField(max_length=256, blank=True, null=True)
	varieties = models.CharField(max_length=256, blank=True, null=True)
	# agregar: tamanno, zona, que ha comprado previamente, etc etc...

	def __str__(self):
		return "comercial info nr " . __str__(self.pk)


class GeographicInfo(models.Model):
	latitude = models.FloatField() 
	longitud = models.FloatField()

	def __str__(self):
		return 'geographic information'