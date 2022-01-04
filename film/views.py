from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.contrib import messages
def film_main(request):

    return render(request, 'film_main.html')

def lista_filmow(request):
    filmy = Film.objects.all().order_by('-data_obejrzenia')
    contex = {'filmy': filmy}

    return render(request, 'lista_filmow.html', contex)
def add_film(request):
    film_form = FilmForm(request.POST or None)

    if film_form.is_valid():
        film = film_form.save(commit=False)
        film.save()
        name_film = film.title

        messages.success(request, f"Film '{name_film}' został dodany do biblioteki")
        return redirect('/film/film_main')

    return render(request, 'add_film.html', {'form': film_form})