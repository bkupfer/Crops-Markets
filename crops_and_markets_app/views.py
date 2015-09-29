# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from models import *
from forms import *

############
# Neutral pages
@login_required
def about(request):
	return render_to_response("about.html", [], context_instance=RequestContext(request))


def access_denied(request):
	return render_to_response("access_denied.html", [], context_instance=RequestContext(request))


@login_required
def home(request):
	return render_to_response("home.html", locals(), context_instance=RequestContext(request))


@csrf_protect
def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('home')
		else:
			messages.error(request, "Nombre de usuario o contraseña incorrecto.")
			# print("invalid user/password combination.")

	return render_to_response("login.html", locals(), context_instance=RequestContext(request))


# def logout(request):
#	auth.logout(request)
#	return redirect(login)

# Semillas SZ - HQ information
#semillas_sz.address = "V-25, Los Lagos Region, Chile"
#semillas_sz.lat = -41.11949
#semillas_sz.lng = -73.05709


############
# Crops
@login_required
def add_crop(request):
	owner_form = CropOwnerForm(request.POST or None)
	company_form = CompanyCropFrom(request.POST or None)
	crop_form = CropForm(request.POST or None)

	if request.method == "POST":
		if owner_form.is_valid() and company_form.is_valid() and crop_form.is_valid():
			# owner information
			owner = owner_form.cleaned_data['old_owner']
			print owner
			if owner is None:
				name = owner_form.cleaned_data['first_name'].title()
				last_name = owner_form.cleaned_data['last_name'].title()
				number_1 = owner_form.cleaned_data['contact_number_1']
				number_2 = owner_form.cleaned_data['contact_number_2']
				email = owner_form.cleaned_data['email']
				position = owner_form.cleaned_data['position'].title()
				#obs_owner = owner_form.cleaned_data['observations']

				# company information
				company = None
				company_member = company_form.cleaned_data['company_member']
				if company_member:
					company = company_form.cleaned_data['excisting_company']
					if company is None:
						company_name = company_form.cleaned_data['name'].title()
						company_rut = company_form.cleaned_data['rut']

						company = CompanyCrop(name=company_name, rut=company_rut)
						company.save()

				owner = CropOwner(first_name=name, last_name=last_name, contact_number_1=number_1, contact_number_2=number_2,
					email=email, position=position, company=company)
				owner.save()

			# crop information
			# geographical information
			region = crop_form.cleaned_data['region']
			province = None
			commune = None
			try:
				province = Province.objects.get(name= request.POST['province_trick'])
				commune = Commune.objects.get(name= request.POST['commune'])
			except:
				pass

			address = crop_form.cleaned_data['address']
			lat = crop_form.cleaned_data['latitude']
			lng = crop_form.cleaned_data['longitude']

			# terrain characteristics information
			has = crop_form.cleaned_data['has']

			bwater = crop_form.cleaned_data['water']
			bsoil = crop_form.cleaned_data['soil']
			btopo = crop_form.cleaned_data['topography']
			btemp = crop_form.cleaned_data['temperatures']

			cwater = crop_form.cleaned_data['water_cmnt']
			csoil = crop_form.cleaned_data['soil_cmnt']
			ctopo = crop_form.cleaned_data['topography_cmnt']
			ctemp = crop_form.cleaned_data['temperatures_cmnt']

			obs = crop_form.cleaned_data['observations'].strip(' \t\n\r')

			crop = Crop(region=region, province=province, commune=commune, address=address, latitude=lat, longitude=lng, has=has,
				water=bwater, soil=bsoil, topography=btopo, temperatures=btemp,
				water_cmnt=cwater, soil_cmnt=csoil, topography_cmnt=ctopo, temperatures_cmnt=ctemp,
				observations=obs)
			crop.save()
			crop.crop_owner.add(owner)

			# if we get to this point
			messages.success(request, "Predio agregado exitosamente.")
		else:
			messages.error(request, "Error en el formulario.")
			

	return render_to_response("crops/add_crop.html", locals(), context_instance=RequestContext(request))


@login_required
def crops(request):
	return render_to_response("crops/crops.html", locals(), context_instance=RequestContext(request))


@login_required
def crop_info(request):
	if request.method == "GET" and 'id' in request.GET:
		id = request.GET['id']
		crop = Crop.objects.get(pk=id)
		owner = crop.crop_owner.first()
		comp = owner.company

	return render_to_response("crops/crop_info.html", locals(), context_instance=RequestContext(request))


@login_required
def crop_map(request):
	geomarkers = Crop.objects.all()
	return render_to_response("crops/crop_map.html", locals(), context_instance=RequestContext(request))


@login_required
def crop_table(request):
	crops = Crop.objects.all()
	return render_to_response("crops/crop_table.html", locals(), context_instance=RequestContext(request))


@login_required
def paddock_detail(request):
	return render_to_response("crops/paddock_detail.html", locals(), context_instance=RequestContext(request))


############
# Markets
@login_required
def add_market(request):
	client_form = ClientForm(request.POST or None)
	geographical_form = GeoMarkerForm(request.POST or None)
	# comercial_info_form = ComercialInformationForm(request.POST or None)
	company_form = CompanyMarketForm(request.POST or None)

	if request.method == 'POST':
		if client_form.is_valid() and geographical_form.is_valid() and company_form.is_valid():
			# client information
			type_of_client = client_form.cleaned_data['type_of_client']
			first_name = client_form.cleaned_data['first_name'].title()
			last_name = client_form.cleaned_data['last_name'].title()
			number_1 = client_form.cleaned_data['contact_number_1']
			number_2 = client_form.cleaned_data['contact_number_2']
			email = client_form.cleaned_data['email']
			position = client_form.cleaned_data['position'].title()
			obs = client_form.cleaned_data['observations'].strip(' \t\n\r')

			# company information
			company = company_form.cleaned_data['excisting_company']
			if company is None:
				company_name = company_form.cleaned_data['name'].title()
				company_rut = company_form.cleaned_data['rut']
				if company_name != "":
					company = CompanyMarket(name=company_name, rut=company_rut)
					company.save()

			new_client = Client(type_of_client=type_of_client, first_name=first_name, last_name=last_name, contact_number_1=number_1, 
				contact_number_2=number_2, email=email, position=position, observations=obs, company=company)
			new_client.save()

			# geographical information
			region = geographical_form.cleaned_data['region']
			province = None
			commune = None
			try:
				province = Province.objects.get(name= request.POST['province_trick'])
				commune = Commune.objects.get(name= request.POST['commune'])
			except:
				pass

			address = geographical_form.cleaned_data['address']
			latitude = geographical_form.cleaned_data['latitude']
			longitude = geographical_form.cleaned_data['longitude']

			new_geomarker = GeoMarker(client=new_client, region=region, province=province, commune=commune, address=address, latitude=latitude, longitude=longitude)
			new_geomarker.save()

			# all done -- success
			messages.success(request, "Cliente agregado exitosamente.")
		else:
			messages.error(request, "Error en el formulario.")

	return render_to_response("markets/add_market.html", locals(), context_instance=RequestContext(request))


@login_required
def add_sale(request):
	sale_form = TransactionForm(request.POST or None)
	sale_detail_formset = SaleDetailFormSet(request.POST or None, prefix="form")

	if request.method == 'GET':
		client_id = request.GET['id']
		client = Client.objects.get(pk=client_id)

	if request.method == 'POST':
		client_id = request.GET['id']
		if sale_form.is_valid() and sale_detail_formset.is_valid():
			user = request.user
			date = sale_form.cleaned_data['date']
			type_of_transaction = sale_form.cleaned_data['type_of_transaction']
			obs = sale_form.cleaned_data['observations'].strip(' \t\n\r')
			
			new_sale = Sale(user=user, client=Client.objects.get(pk=client_id), type_of_transaction=type_of_transaction, date=date, observations=obs)
			new_sale.save()

			for sale_detail in sale_detail_formset:
				price = sale_detail.cleaned_data['price']
				volume = sale_detail.cleaned_data['volume']
				variety = sale_detail.cleaned_data['variety']

				sdetail = SaleDetail(sale=new_sale, price=price, volume=volume, variety=variety)
				sdetail.save()

			# success
			messages.success(request, 'Venta de agregada con éxtio.')
		else:
			messages.error(request, 'Error en el formulario.')

	return render_to_response("markets/add_sale.html", locals(), context_instance=RequestContext(request))


@login_required
def add_reservation(request):
	reservation_form = SaleForm(request.POST or None)
	reservation_detail_formset = SaleDetailFormSet(request.POST or None, prefix="form")

	if request.method == 'GET':
		client_id = request.GET['id']
		client = Client.objects.get(pk=client_id)

	if request.method == 'POST':
		client_id = request.GET['id']
		if reservation_form.is_valid() and reservation_detail_formset.is_valid():
			user = request.user
			date = reservation_form.cleaned_data['date']
			obs = reservation_form.cleaned_data['observations'].strip(' \t\n\r')
			
			new_reservation = Sale(user=user, client=Client.objects.get(pk=client_id), reservation=True, date=date, observations=obs)
			new_reservation.save()

			for reservation_detail in reservation_detail_formset:
				price = reservation_detail.cleaned_data['price']
				volume = reservation_detail.cleaned_data['volume']
				variety = reservation_detail.cleaned_data['variety']

				rdetail = SaleDetail(sale=new_reservation, price=price, volume=volume, variety=variety)
				rdetail.save()

			# success
			messages.success(request, 'Reserva de agregada con éxtio.')
		else:
			messages.error(request, 'Error en el formulario.')

	return render_to_response("markets/add_reservation.html", locals(), context_instance=RequestContext(request))


@login_required
def markets(request):
	return render_to_response("markets/markets.html", locals(), context_instance=RequestContext(request))


@login_required
def market_info(request):
	if request.method == "GET" and 'id' in request.GET:
		id = request.GET['id']
		client = Client.objects.get(pk = id)
		geo_info = GeoMarker.objects.get(client = id) # change to filter. this should allow multiple locations.
		#comercial_info = ComercialInformation.objects.filter(client = id)

		if client.type_of_client.type == "Actual":
			sales = Sale.objects.filter(client=client, type_of_transaction=2) # ventas

			n = len(sales)
			if n != 0:
				total_price = 0
				total_volume = 0
				varieties = {}
				
				for sale in sales:
					for s in sale.saledetail_set.all():
						total_price += s.price
						total_volume += s.volume
						if s.variety not in varieties:
							varieties[s.variety] = s.volume
						else:
							varieties[s.variety] += s.volume

				for var in varieties:
					varieties[var] = "{0:.2f}".format(100.0 * varieties[var] / total_volume)
				avg_price = total_price / n
				avg_volume = total_volume / n
			else:
				avg_price = avg_volume = 0


	return render_to_response("markets/market_info.html", locals(), context_instance=RequestContext(request))


@login_required
def market_map(request):
#	clients = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Actual"))
#	potential = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Potencial"))
	geomarkers = GeoMarker.objects.all()

	return render_to_response("markets/market_map.html", locals(), context_instance=RequestContext(request))


@login_required
def market_table(request):
	clients = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Actual"))
	#total_sales = 0
	#for client in clients:
	#	client_sales = client.sale_set.filter(type_of_transaction=TypeOfTransaction.objects.get(type="Venta"))

	return render_to_response("markets/market_table.html", locals(), context_instance=RequestContext(request))


@login_required
def market_table_potential(request):
	potential_table = True
	clients = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Potencial"))
	return render_to_response("markets/market_table.html", locals(), context_instance=RequestContext(request))


@login_required
def sales_detail(request):
	if request.method == 'GET':
		sale_id = request.GET['id']
		sale = Sale.objects.get(pk=sale_id)
		sale_details = sale.saledetail_set.all()
		previous_id = sale.client.pk
	return render_to_response("markets/sales_detail.html", locals(), context_instance=RequestContext(request))


@login_required
def sales_history(request):
	if request.method == 'GET':
		id = request.GET['id']
		client = Client.objects.get(pk = id)
		sales = Sale.objects.filter(client = id)

		for sale in sales:
			sale.total_volume = 0
			sale.varieties = {}
			for sd in sale.saledetail_set.all():
				sale.total_volume += sd.volume
				if sd.variety not in sale.varieties:
					sale.varieties[sd.variety] = sd.volume
				else:
					sale.varieties[sd.variety] += sd.volume
			
			for var in sale.varieties:
				sale.varieties[var] = "{0:.2f}".format(100.0 * sale.varieties[var] / sale.total_volume)


	return render_to_response("markets/sales_history.html", locals(), context_instance=RequestContext(request))

