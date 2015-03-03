from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
	list_display = ('titulo','texto','activo','imagen_slider',)
	search_fields = ['titulo','texto',]

	def imagen_slider(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_slider.allow_tags = True

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre','activo','votos','num_muebles_categoria',)
	search_fields = ['nombre',]

	def num_muebles_categoria(self,obj):
		 return Mueble.objects.filter(categoria=obj.id).count()

class MuebleAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','activo','votos','imagen_mueble',)
	search_fields = ['titulo','descripcion',]

	def imagen_mueble(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagenPortada,'100x60', crop='center').url #format='PNG', quality=99

	imagen_mueble.allow_tags = True

class AcabadosAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','activo','votos','imagen_acabado',)
	search_fields = ['titulo','descripcion','categoria',]

	def imagen_acabado(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_acabado.allow_tags = True

class MaderasAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','activo','votos','imagen_madera',)
	search_fields = ['titulo','descripcion','categoria',]

	def imagen_madera(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_madera.allow_tags = True

class ContactoAdmin(admin.ModelAdmin):
	list_display = ('nombre','telefono','rfc','email','activo',)
	search_fields = ['nombre','email','rfc']

class MensajeAdmin(admin.ModelAdmin):
	list_display = ('nombre','email','fecha',)
	search_fields = ['nombre','email',]

class BusquedaAdmin(admin.ModelAdmin):
	list_display = ('palabra','repeticiones',)
	search_fields = ['nombre',]

admin.site.register(Slider,SliderAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Mensaje,MensajeAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Mueble,MuebleAdmin)
admin.site.register(Madera,MaderasAdmin)
admin.site.register(Acabado,AcabadosAdmin)
admin.site.register(Busqueda,BusquedaAdmin)
