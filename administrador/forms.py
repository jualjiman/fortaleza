# -*- coding: utf-8 -*-
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': '¿Cuál es su nombre?','class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '¿Cuál es su email?','class':'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '¿En qué le puedo ayudar?','class':'form-control'}))

class BusquedaForm(forms.Form):
    pista = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'¿Qué estas buscando?'}))