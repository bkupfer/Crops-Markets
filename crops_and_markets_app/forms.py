# -*- coding: utf-8 -*-
from django import forms
from crops_and_markets_app.models import *

# ######## #
# Crops
class CompanyCropFrom(forms.Form):
	# excisting company
	excisting_company = forms.ModelChoiceField(queryset=CompanyCrop.objects.all(), empty_label="Compañía", required=False, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	# new company
	name = forms.CharField(label='Nombre', max_length=256, required=False, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	rut = forms.CharField(label='Rut', max_length=20, required=False, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))

	class Meta:
		model = CompanyCrop

class CropForm(forms.Form):
	company = forms.ModelChoiceField(queryset=CropOwner.objects.all(), empty_label="Dueño", widget=forms.Select(attrs={'class':'form-control input-sm'}))

	region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Región", widget=forms.Select(attrs={'class':'form-control input-sm'}))
	#province = todo
	#commune = todo	
	address = forms.CharField(label='Direccion', max_length=256, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	latitude = forms.IntegerField(label='Latitud', required=False)
	longitude = forms.IntegerField(label='Longitud', required=False)

	class Meta:
		model = Crop


class CropOwnerForm(forms.Form):
	first_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	contact_number_1 = forms.IntegerField(label='Numero de contacto', required=False)
	contact_number_2 = forms.IntegerField(label='Numero de contacto 2', required=False)
	email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={"class": "form-control input-sm"}))
	charge = forms.CharField(label='Cargo', required=False, max_length=100, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))

	observations = forms.CharField(label='Observations', required=False, widget=forms.Textarea(attrs={"class": "form-control input-sm"})) #to add a placeholder, place this into Textarea() > attrs={'placeholder': u'Observaciones'}

	class Meta: 
		model = CropOwner


# ######## #
# Markets
class ClientForm(forms.Form):
	type_of_client = forms.ModelChoiceField(queryset=TypeOfClient.objects.all(), empty_label="Tipo de cliente", widget=forms.Select(attrs={'class':'form-control input-sm'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	contact_number_1 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control input-sm'}))
	contact_number_2 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control input-sm'}))
	email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={"class": "form-control input-sm"}))
	charge = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	observations = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control input-sm"})) # attrs={'placeholder': u'Observaciones'}

	class Meta:
		model = Client
		# exclude = ('campo_a', 'campo_b', 'campo_c')


#class ComercialInformationForm(forms.Form):
#	#volume = forms.CharField(max_length=256, required=False, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
#	#varieties = forms.CharField(max_length=256, required=False, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
#	#price (...)

#	class Meta:
#		model = ComercialInformation


class CompanyMarketForm(forms.Form):
	# excisting company
	excisting_company = forms.ModelChoiceField(queryset=CompanyMarket.objects.all(), empty_label="Compañía", required=False, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	# new company
	name = forms.CharField(label='Nombre', required=False, max_length=256, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	rut = forms.CharField(label='Rut', required=False, max_length=20, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))

	class Meta:
		model = CompanyMarket


class GeoMarkerForm(forms.Form):
	region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Región", widget=forms.Select(attrs={'class':'form-control input-sm'}))
	#province = todo
	#commune = todo
	address = forms.CharField(label='Direccion', max_length=256, required=False, widget=forms.TextInput(attrs={"class": "form-control input-sm"}))
	latitude = forms.IntegerField(required=False, widget=forms.TextInput(attrs={"type": "number", "class": "form-control input-sm"}))
	longitude = forms.IntegerField(required=False, widget=forms.TextInput(attrs={"type": "number", "class": "form-control input-sm"}))

	class Meta:
		model = GeoMarker


class SaleForm(forms.Form):
	price = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control input-sm'}))
	variety = forms.ModelChoiceField(queryset=PotatoVariety.objects.all(), empty_label="Variedad", widget=forms.Select(attrs={'class':'form-control input-sm'}))
	volume = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number', 'class':'form-control input-sm'}))
	observations = forms.CharField(label='Observations', required=False, widget=forms.Textarea(attrs={"class": "form-control input-sm"})) #to add a placeholder, place this into Textarea() > attrs={'placeholder': u'Observaciones'}

	class Meta: 
		model = Sale


class ReserveForm(forms.Form):

	class Meta:
		model = Reserve