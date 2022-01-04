from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from .forms import EventForm
from django.contrib import messages

def lista_wydarzen(request):
    wydarzenia = Event.objects.all().order_by('-data_wydarzenia')
    contex = {'wydarzenia': wydarzenia}
    return render(request, 'lista_wydarzen.html', contex)

def lista_wydarzen_filtr_prywatne(requests):
    return render(requests, 'lista_wydarzen.html', {'wydarzenia': Event.objects.filter(rodzaj=0)})
def lista_wydarzen_filtr_sluzbowe(requests):
    return render(requests, 'lista_wydarzen.html', {'wydarzenia': Event.objects.filter(rodzaj=1)})
def lista_wydarzen_filtr_programowanie(requests):
    return render(requests, 'lista_wydarzen.html', {'wydarzenia': Event.objects.filter(rodzaj=2)})

def add_wydarzenie(request):
    event_form = EventForm(request.POST or None)

    if event_form.is_valid():
        event = event_form.save(commit=False)
        event.save()
        messages.success(request, "Wydarzenie zostało dodane do biblioteki.")
        return redirect('/wydarzenia/wydarzenia_main')

    return render(request, 'add_wydarzenie.html', {'form': event_form})


def wydarzenia_main(request):
    return render(request, 'wydarzenia_main.html')

