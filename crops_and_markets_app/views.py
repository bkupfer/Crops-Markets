from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import auth
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

		else:
			print("invalid user/password combination.")

	return render_to_response("login.html", locals(), context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return redirect(login)


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
	return render_to_response("markets/market_map.html", locals(), context_instance=RequestContext(request))

@login_required
def market_table(request):
	clients = Client.objects.all()
	return render_to_response("markets/market_table.html", locals(), context_instance=RequestContext(request))

@login_required
def market_table_potential(request):
    clients = Client.objects.all()
    return render_to_response("markets/market_table_potential.html", locals(), context_instance=RequestContext(request))

@login_required
def market_info(request):
	if request.method == "GET" and 'id' in request.GET:
		id = request.GET['id']
        client = Client.objects.get(pk = id)

	return render_to_response("markets/market_info.html", locals(), context_instance=RequestContext(request))

@login_required
def add_market(request):
	# type_of_contact_form = TypeOfContactForm(request.POST or None)
	client_form = ClientForm(request.POST or None)
	# comercial_client_form = ComercialClientForm(request.POST or None)

	if request.method == 'POST':
		if client_form.is_valid():
			first_name = client_form.cleaned_data['first_name']
			last_name = client_form.cleaned_data['last_name']
			number_1 = client_form.cleaned_data['contact_number_1']
			number_2 = client_form.cleaned_data['contact_number_2']
			email = client_form.cleaned_data['email']
			obs = client_form.cleaned_data['observations']

			new_client = Client(first_name = first_name, last_name = last_name, contact_number_1 = number_1,
								contact_number_2 = number_2, email = email, observations = obs)
			new_client.save()

	return render_to_response("markets/add_market.html", locals(), context_instance=RequestContext(request))

