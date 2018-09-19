# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime, timedelta,datetime


from django.db import models
import datetime
# Create your models here.

from django.db.models import signals
from datetime import datetime, timedelta,date




@python_2_unicode_compatible
class Receta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField(verbose_name=u'Preparación', help_text=u'El proceso de preparación')
    imagen = models.ImageField(upload_to='recetas', verbose_name=u'Imágen')
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)

    def __str__(self):
        return self.titulo


@python_2_unicode_compatible
class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text=u'Tú comentario', verbose_name='Comentario')

    def __str__(self):
        return self.texto
class Agente(models.Model):
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    nombre= models.CharField(max_length=1000,blank=True,null=True)
    apellido= models.CharField(max_length=1000,blank=True,null=True)
    telefono= models.CharField(max_length=1000,blank=True,null=True)
    id_interprete= models.CharField(max_length=1000,blank=True,null=True)

    def __unicode__(self):
        return self.nombre



class Datos(models.Model):
    fecha = models.DateTimeField(default=datetime.today(),editable=False)
    id_cuota=models.CharField(max_length=100)
    agente= models.ForeignKey('Agente',blank=True, null=True)    
    monto= models.CharField( max_length=100, blank=True, null=True)
    #ticket = models.FileField(upload_to = 'ticket',)
    ticket= models.FileField(upload_to='static/',blank=True, null=True)
    #ticket= models.CharField(max_length=1000,blank=True,null=True)
    total= models.CharField(max_length=1000,blank=True,null=True)
    

    # comments= models.CharField(max_length=1000,blank=True,null=True)
    # time_inter= models.CharField(max_length=1000,blank=True,null=True)



