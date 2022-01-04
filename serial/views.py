from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SerialForm
from django.contrib import messages
from .models import Serial


def serial_main(request):

    return render(request, 'serial_main.html')

def lista_seriali(request):

    seriale = Serial.objects.all().order_by('-data_obejrzenia')
    contex = {'seriale': seriale}

    # return HttpResponse('jakis tam tekst')
    return render(request, 'lista_seriali.html', contex)

def add_serial(request):

    serial_form = SerialForm(request.POST or None, request.FILES or None)

    if serial_form.is_valid():
        serial = serial_form.save(commit=False)
        serial.save()
        name_serial = serial.title

        messages.success(request, f"Serial '{name_serial}' został dodany do biblioteki")
        return redirect('http://127.0.0.1:8000/serial/serial_main')
    print('nieprawidłowy')
    return render(request, 'add_serial.html', {'form': serial_form})