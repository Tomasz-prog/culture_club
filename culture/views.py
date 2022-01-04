from django.shortcuts import render, HttpResponse

def glowna(request):

    return render(request, 'main.html')

