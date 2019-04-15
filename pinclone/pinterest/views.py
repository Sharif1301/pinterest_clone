# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pin

def index(request):
	contex = {'pins_list': Pin.objects.all()}
	return render(request, 'pinterest/index.html', contex)
