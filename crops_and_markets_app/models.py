# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_text

# ######## #
# General
class Region(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name.encode('utf-8')

class Province(models.Model):
	name = models.CharField(max_length=100)
	region = models.ForeignKey('Region')
	def __str__(self):
		return self.name.encode('utf-8')

class Commune(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey('Province')
	def __str__(self):
		return self.name.encode('utf-8')


class PotatoVariety(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name.encode('utf-8')


# ######## #
# Crops	
class CompanyCrop(models.Model):
	name = models.CharField(max_length=100)
	rut = models.CharField(max_length=20, blank=True, null=True)


# crops geomarker
class Crop(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	crop_owner = models.ForeignKey('CropOwner', blank=True, null=True)

	# geographical information
	region = models.ForeignKey('Region', blank=True, null=True)
	province = models.ForeignKey('Province', blank=True, null=True)
	commune = models.ForeignKey('Commune', blank=True, null=True)

	# specific geographical information
	address = models.CharField(max_length=256, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	#distance_to_hq	# refered to the distance to hq. this could be automatically calculated
					# (lat, lng) of sz >> (xx, yy) 

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
			return str(self.crop_owner) + ": " + str(self.address)
		else:
			return str(self.crop_owner)


class CropOwner(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	company = models.ForeignKey('CompanyCrop')

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	contact_number_1 = models.IntegerField(blank=True, null=True)
	contact_number_2 = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	observations = models.TextField(blank=True, null=True)


class Paddock(models.Model):
	crop = models.ForeignKey('Crop')
	# -- information --


# ######## #
# Markets
class Client(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	type_of_client = models.ForeignKey('TypeOfClient')

	# contact information
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	contact_number_1 = models.IntegerField(blank=True, null=True)
	contact_number_2 = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	charge = models.CharField(max_length=100, blank=True, null=True)

	observations = models.TextField(blank=True, null=True)

	# company information
	company = models.ForeignKey('CompanyMarket', blank=True, null=True)

	def __str__(self):
		return self.first_name.encode('utf-8') + " " + self.last_name.encode('utf-8')


class ComercialInformation(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	client = models.ForeignKey('Client')
	volume = models.IntegerField(blank=True, null=True) # aka. size
	varieties = models.ForeignKey('PotatoVariety') # change to multiple select from PotatoVarieties.
	price = models.IntegerField(blank=True, null=True)
	# todo: add; size, historial, timestamps, etc. // aditional information // what kind of information is really needed here? 

	def __str__(self):
		return "comercial info: " + str(self.client)


class CompanyMarket(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	rut = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name.encode('utf-8')

class GeoMarker(models.Model):
	client = models.ForeignKey('Client')

	region = models.ForeignKey('Region', blank=True, null=True)
	province = models.ForeignKey('Province', blank=True, null=True)
	commune = models.ForeignKey('Commune', blank=True, null=True)

	address = models.CharField(max_length=256, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)

	def __str__(self):
		if self.address is not None:
			return str(self.client) + ": " + str(self.address)
		else:
			return str(self.client)


class TypeOfClient(models.Model):
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type

