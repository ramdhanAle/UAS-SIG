from django.shortcuts import render, redirect
from .models import Lokasi

def peta(request):
    data = Lokasi.objects.all()
    return render(request, 'peta.html', {'data': data})

def index(request):
    return redirect('peta/')