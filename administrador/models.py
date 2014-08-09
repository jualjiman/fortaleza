 # -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from datetime import date, datetime

# Create your models here.

# categorias = (
# 	('AC', u'Acabados'),
# 	('MD', u'Maderas'),
# )

class Slider(models.Model):
	imagen = ImageField(upload_to = "sliders")
	titulo = models.CharField(max_length=60)
	texto = models.CharField(max_length=150, blank = True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

class Categoria(models.Model):
	nombre = models.CharField(max_length=60)
	descripcion = models.TextField(blank = True)
	activo = models.BooleanField(default=True)
	votos = models.IntegerField(default=0, editable=False)

	def __str__(self):
		return self.nombre

class Acabado(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField(blank = True)
	imagen = ImageField(upload_to = "acabados")
	activo = models.BooleanField(default=True)
	votos = models.IntegerField(default=0, editable=False)

	def __str__(self):
		return self.titulo

class Madera(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField(blank = True)
	imagen = ImageField(upload_to = "maderas")
	activo = models.BooleanField(default=True)
	votos = models.IntegerField(default=0, editable=False)

	def __str__(self):
		return self.titulo

class Mueble(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	imagenPortada = ImageField(upload_to = "muebles")
	imagen1 = ImageField(upload_to = "muebles", blank=True)
	imagen2 = ImageField(upload_to = "muebles",blank=True)
	imagen3 = ImageField(upload_to = "muebles",blank=True)
	imagen4 = ImageField(upload_to = "muebles",blank=True)
	categoria = models.ForeignKey(Categoria)

	# cuando necesites colocar dos veces una integridad referencial hacia un mismo modelo, necesitas colocar un nombre para 
	# relacionarlo, django coloca uno cuando es una sola FK pero al ser dos, no se puede repetir y no sabe como ponerle

	# acabado = models.ForeignKey(AcabadosYMaderas, related_name='mueble_acabado', blank = True, null = True)
	# madera = models.ForeignKey(AcabadosYMaderas, related_name= 'mueble_madera', blank = True, null = True)
	acabado = models.ForeignKey(Acabado, blank = True, null = True)
	madera  = models.ForeignKey(Madera, blank = True, null = True)
	activo = models.BooleanField(default=True)
	votos = models.IntegerField(default=0, editable=False)

	def __str__(self):
		return self.titulo


class Contacto(models.Model):
	nombre = models.CharField(max_length=60,blank=True)
	telefono = models.CharField(max_length=30,blank=True)
	movil = models.CharField(max_length=30,blank=True)
	direccion = models.TextField(blank=True)
	email = models.EmailField(blank=True)
	activo = models.BooleanField(default=True)
	notas = models.TextField(blank=True)

	def __str__(self):
		return self.nombre

class Mensaje(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField()
	mensaje = models.TextField()
	fecha = models.DateTimeField(default=datetime.now(),editable=False)

	def __str__(self):
		return self.nombre

class Busqueda(models.Model):
	palabra = models.CharField(max_length=100)
	repeticiones = models.IntegerField(default=1)

	def __str__(self):
		return self.palabra





