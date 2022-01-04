from django.urls import path
from .views import add_film, lista_filmow, film_main

app_name = 'film'
urlpatterns = [
    path('lista_filmow', lista_filmow, name='lista_filmow'),
    path('add_film', add_film, name='add_film'),
    path('film_main', film_main, name='film_main')

]