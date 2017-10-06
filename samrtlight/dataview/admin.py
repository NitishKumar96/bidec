# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Area,LampInfo,RunningLog,datalog

admin.site.register(Area)
admin.site.register(LampInfo)
admin.site.register(RunningLog)
admin.site.register(datalog)
