# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

# Create your views here.

def home(request):
	# gte = greater equal that
	# lte = lower equal that
	# gt = greater that
	# lt = lower that
	sliders = Slider.objects.filter(activo = True)
	categorias = Categoria.objects.annotate(Count('mueble')).filter(mueble__count__gt = 0, activo = True)
	muebles = Mueble.objects.filter(activo = True).order_by("votos")[:6]
	searchform = BusquedaForm()

	return render(request,"index.html",{"sliders": sliders, "categorias":categorias,"muebles":muebles,'searchform': searchform,})

def catalogo_muebles_idc(request, idc):

	categoria = get_object_or_404(Categoria, pk = idc, activo = True)
	categorias = Categoria.objects.annotate(Count('mueble')).filter(mueble__count__gt = 0, activo = True).order_by("votos")
	muebles = Mueble.objects.filter(categoria_id = idc, activo = True)

	cat = Categoria.objects.get(pk = idc)
	cat.votos += 1
	cat.save()

	searchform = BusquedaForm()

	return render(request,"catalogo-muebles.html",{
		"categorias": categorias,
		"muebles": muebles,
		"idcs" : idc,
		"categoria": categoria,
		"searchform": searchform,})

def catalogo_muebles(request):
	# muebles = Categoria.objects.all().order_by("votos") aqui regreso todos los objetos de categoria  ordenados por votos
	categorias = Categoria.objects.annotate(Count('mueble')).filter(mueble__count__gt = 0, activo = True).order_by("votos") #aqui retorno todos los objetos de categoria ordenados por vistas, pero tambien incluyo una antotacion por cada instancia donde deposito el numero de muebles por categoria, y los filtro obteniendo solo los que tienen mas de 1 mueble
	# despues puedo accederlo desde "mueble__count"
	# categorias = gettingProductsOfCatalogCategories(categorias) de esta manera me evito utilizar un metodo aparte que hace lo mismo
	searchform = BusquedaForm()

	if categorias.count() > 0:
		idc = categorias[0].id
		muebles = Mueble.objects.filter(categoria_id = idc, activo = True)

		categoria = Categoria.objects.get(pk=idc, activo = True)
	else:
	    idc = 0
	    muebles = None
	    categoria = None
	
	return render(request,"catalogo-muebles.html",{"categorias": categorias,"muebles": muebles, 'categoria':categoria,'idcs' : idc,'searchform': searchform})

# def gettingProductsOfCatalogCategories(muebles):
# 	for categoria in muebles:
# 		productos = Mueble.objects.filter(categoria_id = categoria.id).count()
# 		categoria.count = productos
# 	return muebles

def catalogo_acabados(request):
	acabados = Acabado.objects.filter(activo = True)
	maderas  = Madera.objects.filter(activo = True)
	searchform = BusquedaForm()

	return render(request,"catalogo-acabados.html",{"acabados": acabados,"maderas": maderas,'searchform': searchform})

def mueble(request,idc,idp):
	mueble = get_object_or_404(Mueble,pk=idp)
	sugerencias = Mueble.objects.filter(categoria_id = idc,activo = True).exclude(pk=idp).order_by("votos")[:6]
	sug = True #es una sujerencia
	searchform = BusquedaForm()
	
	if sugerencias.count() == 0:
		sugerencias = Mueble.objects.filter(activo = True).exclude(pk=idp).order_by("votos")[:6]
		sug = False #solamente le estas mostrando los demas

	return render(request,"mueble.html",{"mueble": mueble,"sugerencias":sugerencias,'sug':sug,'searchform': searchform})

def imgProducto(request):
	if request.is_ajax():
	    id_producto = request.POST['idp']
	    num_img = request.POST['nim'] #1 principal, 2 imagen1, 3 imagen2, 4 imagen3, 5 imagen4

	    producto = Mueble.objects.get(pk=id_producto, activo = True)

	    if num_img == "1":
	    	producto.imagen = producto.imagenPortada
	    elif num_img == "2":
	    	producto.imagen = producto.imagen1
	    elif num_img == "3":
	    	producto.imagen = producto.imagen2
	    elif num_img == "4":
	    	producto.imagen = producto.imagen3
	    elif num_img == "5":
	    	producto.imagen = producto.imagen4
	    else:
	    	producto.imagen = "Error al cargar la imagen"

	    return render(request, "imgProducto.html",{"producto":producto})
	else:
		return HttpResponse('Error al cargar la imagen')

def busqueda(request):
	if request.method == 'GET': # If the form has been submitted...
        # ContactForm BusquedaForm was defined in the previous section
        #FUNCIONA PERFECTAMENTE POR GET O POST
		searchform = BusquedaForm(request.GET) # A form bound to the POST data
		if searchform.is_valid(): # All validation rules pass
	        # Process the data in form.cleaned_data
	        # ...
			pista = searchform.cleaned_data['pista']
			if pista != u'':
				muebles = Mueble.objects.filter(Q(activo = True), Q(titulo__contains=pista) | Q(descripcion__contains=pista) | Q(acabado__titulo__contains=pista) | Q(madera__titulo__contains=pista))
				categorias = Categoria.objects.annotate(Count('mueble')).filter(mueble__count__gt = 0, activo = True, nombre__contains=pista).order_by("votos")
				acabados = Acabado.objects.filter(Q(activo = True), Q(titulo__contains=pista) | Q(descripcion__contains=pista))
				maderas  = Madera.objects.filter(Q(activo = True), Q(titulo__contains=pista) | Q(descripcion__contains=pista))

				try:
					pbusqueda = Busqueda.objects.get(palabra=pista)
					pbusqueda.repeticiones += pbusqueda.repeticiones
					pbusqueda.save()
				except Busqueda.DoesNotExist:
					pbusqueda = Busqueda(palabra=pista)
					pbusqueda.save()

				textoBusqueda = 'Resultados para "' + pista + '"'
				return render(request, 'busqueda.html', {
					"muebles":muebles,
					"categorias":categorias,
					"acabados":acabados,
					"maderas":maderas,
					"searchform":searchform,
					"textoBusqueda":textoBusqueda
				})
			else:
				return HttpResponseRedirect("/")
		else:
				return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")

def contacto(request):
	if request.is_ajax():
	    nombre = request.POST['name']
	    email = request.POST['email']
	    mensaje = request.POST['message']

	    msj = Mensaje(nombre=nombre, email=email,mensaje=mensaje)
	    msj.save()

	    send_simple_message()
	    return HttpResponse('Ok')
	else:
		form = ContactoForm()
		searchform = BusquedaForm()
		return render(request,"contacto.html",{"form": form,"searchform": searchform})

@csrf_exempt
def preferencias(request):
	if request.is_ajax():
	    prefs = request.POST['prefs'].split("-")

	    p1 = prefs[0]
	    p2 = prefs[1]
	    preferencias = Mueble.objects.filter(Q(id= p2) | Q(id = p1))

	    pf = Mueble.objects.get(id = p1)
	    pf.votos += 1
	    pf.save()

	    return render(request,"preferencias.html",{"preferencias": preferencias})
	else:
		return HttpResponseRedirect("/")

def send_simple_message():
	return requests.post(
        "https://api.mailgun.net/v2/sandbox58531cd99f8b406d9932f7ff5259395c.mailgun.org/messages",
        auth=("api", "key-1fe898bc8e3b6d509eb0af3801efa6f7"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox58531cd99f8b406d9932f7ff5259395c.mailgun.org>",
              "to": "Juan Alberto Jimenez Angel <jualjiman@gmail.com>",
              "subject": "Hello Juan Alberto Jimenez Angel",
              "text": "Congratulations Juan Alberto Jimenez Angel, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

