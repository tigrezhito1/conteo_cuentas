# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Receta, Comentario
from django.forms import ModelForm
from django import forms
from .models import *

from views import *



class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tú correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)


class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'


class DatoForm(ModelForm):

	class Meta:
		model = Datos
		fields = '__all__'
		exclude=('agente','total')
		

		widgets = {

			
			'fecha': forms.TextInput(attrs={'class': 'form-control ','type':'text'}),
			'id_cuota': forms.TextInput(attrs={'class': 'form-control '}),
			'agente': forms.Select(attrs={'class': 'form-control ','type':'text'}),
			'monto': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
			
			#'ticket': forms.TextInput(attrs={'class': 'form-control ','type':'file'}),
			#'ticket': forms.FileField(attrs={label='Select a file'}),
			'total': forms.TextInput(attrs={'class': 'form-control '}),




			
			

			
		}
