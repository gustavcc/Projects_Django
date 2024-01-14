from django.shortcuts import render
from .models import Corte

def home(request):
    return render(request, 'paginas/home.html')

def cortes(request):
    novo_corte = Corte()
    novo_corte.primeira = request.POST.get('primeira')
    novo_corte.segunda = request.POST.get('segunda')
    novo_corte.save()
    
    cortes = {
        'cortes': Corte.objects.all()
    }
    
    return render(request, 'paginas/dashboard.html',cortes)