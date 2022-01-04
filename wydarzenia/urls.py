from django.urls import path
from .views import lista_wydarzen, add_wydarzenie, wydarzenia_main, lista_wydarzen_filtr_prywatne, lista_wydarzen_filtr_sluzbowe, lista_wydarzen_filtr_programowanie

app_name = 'wydarzenia'
urlpatterns = [
    path('lista_wydarzen', lista_wydarzen, name='lista_wydarzen'),
    path('lista_wydarzen_filtr_prywatne', lista_wydarzen_filtr_prywatne, name='lista_wydarzen_filtr_prywatne'),
    path('lista_wydarzen_filtr_sluzbowe', lista_wydarzen_filtr_sluzbowe, name='lista_wydarzen_filtr_sluzbowe'),
    path('lista_wydarzen_filtr_programowanie', lista_wydarzen_filtr_programowanie, name='lista_wydarzen_filtr_programowanie'),
    path('add_wydarzenie', add_wydarzenie, name='add_wydarzenie'),
    path('wydarzenia_main', wydarzenia_main, name='wydarzenia_main')
]