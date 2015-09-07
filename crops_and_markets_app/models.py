# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_text

# ######## #
# Crops	

# crops geomarker
class Crop(models.Model):
	crop_owner = models.ForeignKey('CropOwner')
	created = models.DateTimeField(auto_now_add=True)

	# geographical information 
	zone = models.CharField(max_length=256, blank=True, null=True)
	address = models.CharField(max_length=256, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	#distance # refered to the distance to hq. this could be automatically calculated

	# core characteristics -- as boolean and then text for observation/coments
	water = models.BooleanField()
	frost = models.BooleanField()
	terrain_characteristics = models.BooleanField()
	topography = models.BooleanField()

	# core characteristics coments
	water_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	frost_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	terrain_characteristics_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	topography_cmnt = models.CharField(max_length=1024, blank=True, null=True)

	# secondary characteristics
	observations = models.TextField(blank=True, null=True)

	def __str__(self):
		if self.zone is not None:
			return str(self.crop_owner) + ": " + str(self.zone)
		else:
			return str(self.crop_owner)


# crops 'clients'
# saves information of the crop owner
class CropOwner(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	owner_name = models.CharField(max_length=256, blank=True, null=True)
	# -- crop owner information --

class Paddock(models.Model):
	crop = models.ForeignKey('Crop')
	# -- information --


# ######## #
# Markets

class GeoMarker(models.Model):
	client = models.ForeignKey('Client')
	zone = models.CharField(max_length=256, blank=True, null=True)
	address = models.CharField(max_length=256, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)

	def __str__(self):
		if self.zone is not None:
			#return str(self.client) + ": " + self.zone
			return str(self.client) + ": " + str(self.zone)
		else:
			return str(self.client)


class Client(models.Model):
	type_of_client = models.ForeignKey('TypeOfClient')
	created = models.DateTimeField(auto_now_add=True)

	# contact information
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	contact_number_1 = models.IntegerField(blank=True, null=True)
	contact_number_2 = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	observations = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.first_name.encode('utf-8') + " " + self.last_name.encode('utf-8')


class ComercialInfo(models.Model): # should it be renamed to -ComercialInformation- ?
	client = models.ForeignKey('Client')
	volume = models.CharField(max_length=256, blank=True, null=True) # aka. size
	varieties = models.CharField(max_length=256, blank=True, null=True) # change to multiple select fields. limited set of options.
	# todo: add; size, historial, timestamps, etc. // aditional information // what kind of information is really needed here? 

	def __str__(self):
		return "comercial info: " + str(self.client)


class TypeOfClient(models.Model):
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type

