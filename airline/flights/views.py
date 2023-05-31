from django.shortcuts import render
from . models import Flight,Pasenger
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request,"flights/index.html",{'flights': Flight.objects.all()})


def flight(request, flight_id):
    flight =Flight.objects.get(id = flight_id)
    return render(request, "flights/flight.html",
                   {'flight': flight,
                    'passengers':flight.passengers.all(),
                    "non_passengers":Pasenger.objects.exclude(flights =flight).all()})

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id = flight_id)
        passenger = Pasenger.objects.get(id = int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))
