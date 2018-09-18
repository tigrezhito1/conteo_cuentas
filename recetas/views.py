# coding:utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ComentarioForm, ContactoForm, RecetaForm
from .models import *

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect

from .forms import *
from datetime import datetime, date, time, timedelta
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



from django.contrib.auth.views import login
#.....

from django.template import RequestContext
import xlrd
from django.db.models import Count,Sum


from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate
import os
import requests
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required



from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime, timedelta,date
from django.db.models import Count




@login_required(login_url="/usuarios//")

def datitos(request):

    if request.method=='POST':

        age= Agente.objects.get(usuario=request.user)

        lla = Datos(agente=age)




        form = DatoForm(request.POST, instance=lla)
        

    
        if form.is_valid():

            form.save()

# <<<<<<< HEAD
        # formulario = InterpreteForm()
        # llamadas=Interprete.objects.all()
        # filter=fecha__lte=datetime.datetime.today()
        # context = {'datos': formulario,'llamada':llamadas}
        
# =======

# >>>>>>> 1e795392b627130f02172a9199e9ef0bb6662856
    
        return HttpResponseRedirect("/datitos/")


    if request.method=='GET':

        #interprete = Interprete.objects.all()
        #context = {'datos': interprete}
        
        a= Agente.objects.get(usuario=request.user)

        print 'Agente',a

        lla = Datos.objects.filter(agente=a).order_by('-id')

        print 'Llamada',lla


        formulario = DatoForm()

        
        

        laSuma = 0
        for i in Datos.objects.filter(agente_id=a):
            laSuma = laSuma +int(i.monto) 
            print 'lo logre carajo....',laSuma

            Cuotas= Datos.objects.filter(agente_id=a).count()
            print 'locoooo',Cuotas

   
        context = {'datos': formulario,'dato':lla,'agente':a,'suma':laSuma,'cuotas':Cuotas}
        

        
  
       
    

        return render(request, 'recetas_inicio.html',context)



  



# @login_required(login_url='/ingreso')
# def cerrar(request):
#     logout(request)
#     return HttpResponseRedirect('/')

def comentario_nuevo(request):
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_comentarioform.html', context)

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            try:
                correo.send()
            except Exception as e:
                print('No fue posible enviar el mensaje, revisar la configuración')
                print(e)
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_contactoform.html',context)



def ingreso(request):

    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password']

        print 'estos son los usurios _poeue no entra?',username,password
        user = authenticate(username=username, password=password)
        if user is not None:

            print 'porque me manda a ingresar??',login(request, user)



            return HttpResponseRedirect('/datitos/')

        else:


            return render(request, 'login.html',{'error': 'No existe este usuario'})

    if request.method=='GET':

        return render(request, 'login.html') 


def salir(request):

    
    # id =request.user.id
    # nivel = AuthUser.objects.get(id=id).nivel.id
    
    # if nivel == 3:
    #     agente = Agentes.objects.get(user=id)
    #     agente.estado_id=1
    #     agente.est_ag_predictivo = 0
    #     agente.save()
    #     Estadocambio(user_id=id,estado_id=1).save()

    logout(request)
    
    return HttpResponseRedirect("/ingreso/") 


def inicio(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas_inicio.html', context)




# def ingresar(request):
#     if not request.user.is_anonymous():
#         return HttpResponseRedirect('/privado')
#     if request.method == 'POST':
#         formulario = AuthenticationForm(request.POST)
#         if formulario.is_valid:
#             usuario = request.POST['username']
#             clave = request.POST['password']
#             acceso = authenticate(username=usuario, password=clave)
#             if acceso is not None:
#                 if acceso.is_active:
#                     login(request, acceso)
#                     return HttpResponseRedirect('/privado')
#                 else:
#                     return render(request, 'noactivo.html')
#             else:
#                 return render(request, 'nousuario.html')
#     else:
#         formulario = AuthenticationForm()
#     context = {'formulario': formulario}
#     return render(request, 'ingresar.html', context)

@login_required(login_url='/ingreso/')
def privado(request):
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, 'privado.html', context)

def receta(request, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    comentarios = Comentario.objects.filter(receta=dato)
    context = {'receta': dato, 'comentarios': comentarios}
    return render(request, 'recetas_receta.html', context)

def receta_nueva(request):
    if request.method=='POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_recetaform.html', context)


def recetas(request):
    recetas = Receta.objects.all()
    context = {'datos': recetas}
    return render(request, 'recetas_lista_recetas.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    context = {'recetas': recetas, 'usuarios':usuarios}
    return render(request, 'recetas_usuarios.html', context)

def usuario_nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    context = {'formulario': formulario}
    return render(request, 'nuevousuario.html', context)

def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
