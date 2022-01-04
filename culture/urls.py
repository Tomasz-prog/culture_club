from django.contrib import admin
from django.urls import path, include
from .views import glowna
from ksiazka.views import ksiazka
from serial.views import serial_main

app_name = 'culture'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ksiazka/', ksiazka),
    path('serial/', include('serial.urls')),
    path('film/', include('film.urls')),
    path('wydarzenia/', include('wydarzenia.urls')),

    path('', glowna),
]
