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
	return render_to_response("about.html", locals(), context_instance=RequestContext(request))

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
		# else:
			# print("invalid user/password combination.")
            
        return render_to_response("login.html", locals(), context_instance=RequestContext(request))

# def logout(request):
#	auth.logout(request)
#	return redirect(login)

def access_denied(request):
    #return redirect("access_denied");
    return render_to_response("access_denied.html", [], context_instance=RequestContext(request))


############
# Crops
@login_required
def crops(request):
	return render_to_response("crops/crops.html", locals(), context_instance=RequestContext(request))

@login_required
def crop_map(request):
	return render_to_response("crops/crop_map.html", locals(), context_instance=RequestContext(request))

@login_required
def crop_info(request):
	name = "Frutillar"
	owner = "Don Graph"
	return render_to_response("crops/crop_info.html", locals(), context_instance=RequestContext(request))

@login_required
def paddock_detail(request):
	return render_to_response("crops/paddock_detail.html", locals(), context_instance=RequestContext(request))


############
# Markets
@login_required
def markets(request):
	return render_to_response("markets/markets.html", locals(), context_instance=RequestContext(request))

@login_required
def market_map(request):
#	clients = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Actual"))
#	potential = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Potencial"))
	geomarkers = GeoMarker.objects.all()

	return render_to_response("markets/market_map.html", locals(), context_instance=RequestContext(request))

@login_required
def market_table(request):
	clients = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Actual"))
	return render_to_response("markets/market_table.html", locals(), context_instance=RequestContext(request))

@login_required
def market_table_potential(request):
	clients = Client.objects.filter(type_of_client=TypeOfClient.objects.get(type="Potencial"))
	return render_to_response("markets/market_table_potential.html", locals(), context_instance=RequestContext(request))

@login_required
def market_info(request):
	if request.method == "GET" and 'id' in request.GET:
		id = request.GET['id']
		client = Client.objects.get(pk = id)
		geo_info  = GeoMarker.objects.get(client = id)
		comercial_info = ComercialInfo.objects.get(client = id)

	return render_to_response("markets/market_info.html", locals(), context_instance=RequestContext(request))

@login_required
def add_market(request):
	client_form = ClientForm(request.POST or None)
	geographical_form = GeoMarkerForm(request.POST or None)
	comercial_info_form = ComercialInformationForm(request.POST or None)

	if request.method == 'POST':
		if client_form.is_valid() and geographical_form.is_valid() and comercial_info_form.is_valid():
			# client information
			type_of_client = client_form.cleaned_data['type_of_client']
			first_name = client_form.cleaned_data['first_name']
			last_name = client_form.cleaned_data['last_name']
			number_1 = client_form.cleaned_data['contact_number_1']
			number_2 = client_form.cleaned_data['contact_number_2']
			email = client_form.cleaned_data['email']
			obs = client_form.cleaned_data['observations']

			new_client = Client(type_of_client=type_of_client, first_name=first_name, last_name=last_name, contact_number_1=number_1, 
				contact_number_2=number_2, email=email, observations=obs)
			new_client.save()

			# geographical information
			zone = geographical_form.cleaned_data['zone']
			latitude = geographical_form.cleaned_data['latitude']
			longitude = geographical_form.cleaned_data['longitude']

			new_geomarker = GeoMarker(client=new_client, zone=zone, latitude=latitude, longitude=longitude)
			new_geomarker.save() 

			# comercial information
			volume = comercial_info_form.cleaned_data['volume']
			varieties = comercial_info_form.cleaned_data['varieties']

			new_comercial_info = ComercialInfo(client=new_client, volume=volume, varieties=varieties)
			new_comercial_info.save()

			messages.success(request, 'Cliente agregado exitosamente.')

	return render_to_response("markets/add_market.html", locals(), context_instance=RequestContext(request))

