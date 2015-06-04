from django.shortcuts import render, render_to_response, RequestContext

# Neutral pages
def home(request):
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))

def about(request):
    return render_to_response("about.html", locals(), context_instance=RequestContext(request))


# Crops
def crops(request):
    return render_to_response("crops/crops.html", locals(), context_instance=RequestContext(request))

def info(request):
    name = "Frutillar"
    owner = "Don Graph"

    return render_to_response("crops/info.html", locals(), context_instance=RequestContext(request))

# Markets
def markets(request):
    return render_to_response("markets/markets.html", locals(), context_instance=RequestContext(request))


