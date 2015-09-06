# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_text

# ######## #
# General 
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
			return "geographical information"


# ######## #
# Crops	


# Markets
class Client(models.Model):
	type_of_client = models.ForeignKey('TypeOfClient')

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

	volume = models.CharField(max_length=256, blank=True, null=True)
	varieties = models.CharField(max_length=256, blank=True, null=True) # change to multiple select fields. limited set of options.
	# todo: add; size, historial, timestamps, etc. // aditional information // what kind of information is really needed here? 

	def __str__(self):
		return "comercial info: " + str(self.client)


class TypeOfClient(models.Model):
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type

