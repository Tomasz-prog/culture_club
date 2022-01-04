from django.urls import path
from .views import lista_seriali, serial_main, add_serial

app_name = 'serial'
urlpatterns = [
    path('lista_seriali/', lista_seriali, name='lista_seriali'),
    path('add_serial', add_serial, name='add_serial'),
    path('serial_main', serial_main , name='serial_main')
]