from django.shortcuts import render

def home(request):
    return render (request, 'core/home.html')

def narrativas(request):
    return render (request, 'core/narrativas.html')

def espacos(request):
    return render (request, 'core/espacos.html')

def corpos(request):
    return render (request, 'core/corpos.html')

def espacocontem(request):
    return render (request, 'core/espacos_contem.html')

def grupos(request):
    return render (request, 'core/grupos.html')

def musica(request):
    return render (request, 'core/musica.html')
