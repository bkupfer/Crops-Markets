from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

# from crops_and_markets_app.models import *
from models import *

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

		if user:
			return redirect('home')

		else:
			print("error validating form -- form not valid")

	return render_to_response("login.html", locals(), context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return redirect(login)

# Crops
def crops(request):
	return render_to_response("crops/crops.html", locals(), context_instance=RequestContext(request))

def info(request):
	name = "Frutillar"
	owner = "Don Graph"

	return render_to_response("crops/info.html", locals(), context_instance=RequestContext(request))

def paddock_detail(request):

	return render_to_response("crops/paddock_detail.html", locals(), context_instance=RequestContext(request))

# Markets
def markets(request):
	return render_to_response("markets/markets.html", locals(), context_instance=RequestContext(request))


