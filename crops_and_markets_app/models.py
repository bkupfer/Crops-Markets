# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
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

class Certificate(models.Model):
	certificate = models.CharField(max_length=20)
	def __str__(self):
		return self.certificate.encode('utf-8')
		

# class Segment(models.Model):
# 	segment = models.CharField(max_length=20)
# 	def __str__(self):
# 		return self.segment.encode('utf-8')


# ######## #
# Crops	
class CompanyCrop(models.Model):
	name = models.CharField(max_length=100)
	rut = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name.encode('utf-8')


class Crop(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	crop_owner = models.ManyToManyField('CropOwner')

	# geographical information
	region = models.ForeignKey('Region', blank=True, null=True)
	province = models.ForeignKey('Province', blank=True, null=True)
	commune = models.ForeignKey('Commune', blank=True, null=True)
	address = models.CharField(max_length=256, blank=True, null=True)

	# general characterisitcs
	has = models.PositiveSmallIntegerField(blank=True, null=True)

	# terrain characteristics 
	# Los factores claves son:
	# agua, calidad de tierra, topologia, clima no-heloso
	# edit: acceso

	# core characteristics -- as boolean and then text for observation/comments
	water = models.BooleanField()
	soil = models.BooleanField()
	topography = models.BooleanField()
	temperatures = models.BooleanField()
	access = models.BooleanField()

	# core characteristics comments
	water_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	soil_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	topography_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	temperatures_cmnt = models.CharField(max_length=1024, blank=True, null=True)
	access_cmnt = models.CharField(max_length=1024, blank=True, null=True)

	# secondary characteristics
	observations = models.TextField(blank=True, null=True)


class CropImage(models.Model):
	crop = models.ForeignKey('Crop')
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(max_length=255, upload_to='crop-media/')


class CropOwner(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	# crop -- there is a ManyToMany field relating crops with owners.
	# crop_owner.crop_set.all() -- this should give all the crops for this owner.
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	rut = models.CharField(max_length=20, blank=True, null=True)
	contact_number_1 = models.CharField(max_length=16, blank=True, null=True)
	contact_number_2 = models.CharField(max_length=16, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	position = models.CharField(max_length=100, blank=True, null=True)

	company = models.ForeignKey('CompanyCrop', null=True)

	def __str__(self):
		return self.first_name.encode('utf-8') + " " + self.last_name.encode('utf-8')


# ######## #
# Markets
class Client(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	type_of_client = models.ForeignKey('TypeOfClient')

	# contact information
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	rut = models.CharField(max_length=20, blank=True, null=True)
	contact_number_1 = models.CharField(max_length=16, blank=True, null=True)
	contact_number_2 = models.CharField(max_length=16, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	position = models.CharField(max_length=100, blank=True, null=True)
	observations = models.TextField(blank=True, null=True)

	# company information
	company = models.ForeignKey('CompanyMarket', null=True)

	def __str__(self):
		return self.first_name.encode('utf-8') + " " + self.last_name.encode('utf-8')


class CompanyMarket(models.Model):
	name = models.CharField(max_length=100)
	rut = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name.encode('utf-8')


class GeoMarker(models.Model):
	client = models.ForeignKey('Client')
	region = models.ForeignKey('Region', blank=True, null=True)
	province = models.ForeignKey('Province', blank=True, null=True)
	commune = models.ForeignKey('Commune', blank=True, null=True)
	address = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		if self.address is not None:
			return str(self.client) + ": " + str(self.address)
		else:
			return str(self.client)

	def get_address(self):
		address = ""
		if self.address is not None:
			address = address + self.address
			if self.region is not None:
				adress = address + ", " + self.region
			address = address + ", Chile"
		return address


class Sale(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	client = models.ForeignKey('Client')
	type_of_transaction = models.ForeignKey('TypeOfTransaction')
	date = models.DateField()
	observations = models.TextField(blank=True, null=True)

	def get_volume(self):
		total_volume = 0
		for detail in self.saledetail_set.all():
			total_volume += detail.volume
		return total_volume

	def get_price(self):
		total_price = 0
		for detail in self.saledetail_set.all():
			total_price += detail.price
		return total_price

	# return string with varieties separated by char ' '
	def get_varieties(self):
		varieties = ""
		for detail in self.saledetail_set.all():
			varieties += ' ' + str(detail.variety)
		return varieties


class SaleDetail(models.Model):
	sale = models.ForeignKey('Sale')
	volume = models.IntegerField()
	price = models.IntegerField()
	variety = models.ForeignKey('PotatoVariety')
	certificate = models.ForeignKey('Certificate')


class TypeOfClient(models.Model):
	type = models.CharField(max_length=8)

	def __str__(self):
		return self.type


class TypeOfTransaction(models.Model):
	type = models.CharField(max_length=8)

	def __str__(self):
		return self.type


# ######## #
# Related
class Related(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	rut = models.CharField(max_length=20, blank=True, null=True)
	contact_number_1 = models.CharField(max_length=16, blank=True, null=True)
	contact_number_2 = models.CharField(max_length=16, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	observations = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	# foregn key -- area

	def __str__(self):
		return self.first_name.encode('utf-8') + " " + self.last_name.encode('utf-8')


class RelatedArea(models.Model):
	area = models.CharField(max_length=100)

	def __str__(self):
		return self.area.encode('utf-8')

