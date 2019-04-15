# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pinner
from .models import Board
from .models import Pin
from .models import Image

admin.site.register(Pinner)
admin.site.register(Board)
admin.site.register(Pin)
admin.site.register(Image)