from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import *
from django.views import View
import googlemaps
from django.conf import settings 
from .forms import*
from datetime import datetime

# Create your views here.

class HomeView(ListView):
    template_name = "home.html"
    context_object_name = 'mydata'
    model = Location
    success_url = "/"


class MapView(View):
    template_name = "map.html"

    def get(self, request):
        key = settings.GOOGLE_API_KEY
        eligable_location = Location.objects.filter(place_id__isnull = False)
        location = []

        for a in eligable_location:
            data = {
                'lat': float(a.lat),
                'lng': float(a.lng),
                'name': a.name
            }
            location.append(data)
        context = {
            "key":key,
            "location":location
        }   
        return render(request, self.template_name, context) 
    

class GeocodingView(View):
    template_name = "geocoding.html"

    def get(self, request, pk):
        location = Location.objects.get(pk=pk)

        if location.lng and location.lat and location.place_id != None:
            lat = location.lat
            lng = location.lng
            place_id = location.place_id
            label = "from my API Call"

        elif location.address and str(location.country) and location.zipcode and location.city != None:
            address_string = str(location.address)+", "+str(location.zipcode)+", "+str(location.city)+", "+str(location.country)
            gmaps = googlemaps.Client(key = settings.GOOGLE_API_KEY)
            result = gmaps.geocode(address_string)[0]
            
            lat = result.get('geometry', {}).get('location', {}).get('lat', None)
            lng = result.get('geometry', {}).get('location', {}).get('lng', None)
            place_id = result.get('place_id', {})
            label = "from my database"

            location.lat = lat
            location.lng = lng
            location.place_id = place_id
            location.save()

        else:
            result = ""
            lat = ""
            lng = ""
            place_id = ""
            label = "No call Made"

        context = {"location": location,
                   'lat': lat,
                   'lng': lng,
                   'place_id': place_id,
                   'label': label
                   }        

        return render(request, self.template_name, context=context)


def add_location(request):
    SForm = LocationForm()
    if request.method == 'POST':
        SForm = LocationForm(request.POST, request.FILES)
        if SForm.is_valid():
            SForm.save()
            return redirect('folio1:home')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'xyz'}}>Reload</a>" """)
    else:
        return render(request, 'backpic.html', {'upload_location': SForm})