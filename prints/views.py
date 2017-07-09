# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def prints(request):
    return render(request, 'prints/home.html')

def marrakesh(request):
    return render(request, 'prints/marrakesh.html')

def camels_wadi_rum(request):
    return render(request, 'prints/camels_wadi_rum.html')

def fes(request):
    return render(request, 'prints/fes.html')

def strasbourg(request):
    return render(request, 'prints/strasbourg.html')

def eiffel(request):
    return render(request, 'prints/eiffel.html')

def wadi_rum(request):
    return render(request, 'prints/wadi_rum.html')

def bangkok(request):
    return render(request, 'prints/bangkok.html')

def atlas(request):
    return render(request, 'prints/atlas.html')

def angkor_wat(request):
    return render(request, 'prints/angkor_wat.html')

def mekong(request):
    return render(request, 'prints/mekong.html')

def louvre(request):
    return render(request, 'prints/louvre.html')

def wat_pho(request):
    return render(request, 'prints/wat_pho.html')

# Create your views here.
