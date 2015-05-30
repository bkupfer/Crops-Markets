from django.shortcuts import render, render_to_response, RequestContext

def home(request):
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))
    
# Crops
def crops(request):
    return render_to_response("crops/crops.html", locals(), context_instance=RequestContext(request))
    
# Markets
def markets(request):
    return render_to_response("markets/markets.html", locals(), context_instance=RequestContext(request))
    