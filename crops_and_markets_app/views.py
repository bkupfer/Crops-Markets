from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# from crops_and_markets_app.models import *
from models import *

############
# Neutral pages
def about(request):
	return render_to_response("about.html", locals(), context_instance=RequestContext(request))

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
	return render_to_response("markets/market_table.html", locals(), context_instance=RequestContext(request))

@login_required
def market_info(request):
	id = request.GET['id']
	return render_to_response("markets/market_info.html", locals(), context_instance=RequestContext(request))

@login_required
def add_market(request):
	return render_to_response("markets/add_market.html", locals(), context_instance=RequestContext(request))

