# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.prints, name='prints'),
    url(r'^marrakesh', views.marrakesh, name='marrakesh'),
    url(r'^wadi_rum', views.wadi_rum, name='wadi_rum'),
    url(r'^camels_wadi_rum', views.camels_wadi_rum, name='camels_wadi_rum'),
    url(r'^fes', views.fes, name='fes'),
    url(r'^strasbourg', views.strasbourg, name='strasbourg'),
    url(r'^eiffel', views.eiffel, name='eiffel'),
    url(r'^bangkok', views.bangkok, name='bangkok'),
    url(r'^atlas', views.atlas, name='atlas'),
    url(r'^angkor_wat', views.angkor_wat, name='angkor_wat'),
    url(r'^mekong', views.mekong, name='mekong'),
    url(r'^louvre', views.louvre, name='louvre'),
    url(r'^wat_pho', views.wat_pho, name='wat_pho'),
                        
]
