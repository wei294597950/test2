# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from test_app1.models import *
# Register your models here.

admin.site.register(logdelete)
admin.site.register(deletelog)
admin.site.register(restore)

admin.site.register(restoress)
