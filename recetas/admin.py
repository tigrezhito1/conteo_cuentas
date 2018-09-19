from .models import Receta, Comentario
from django.contrib import admin

from django.contrib import admin
#from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import os.path
import json
import requests
from django.contrib.admin.filters import DateFieldListFilter

#from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import *

admin.site.register(Receta)
admin.site.register(Comentario)

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','id_cuota','agente','monto','ticket')


