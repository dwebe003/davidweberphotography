# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
    url(r'^page2', views.page2, name='page2'),
    url(r'^page3', views.page3, name='page3'),
    url(r'^page4', views.page4, name='page4'),
    url(r'^page5', views.page5, name='page5'),
    url(r'^page6', views.page6, name='page6'),
    url(r'^page7', views.page7, name='page7'),
    url(r'^page8', views.page8, name='page8'),
    url(r'^page9', views.page9, name='page9'),
    url(r'^page10', views.page10, name='page10'),
]
