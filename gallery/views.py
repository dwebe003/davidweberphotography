# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def gallery(request):
    return render(request, 'gallery/home.html')

# Create your views here.
