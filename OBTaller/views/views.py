from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from OBTaller.forms import UnidadForm
from OBTaller.models import WcUnidad, ConceptoCategoria, TipoServicio, Parametros, \
    ConceptoTipoMarca, UnidadMedida, WcUnidadNeu


def addConceptoCategoria(request):
    if request.method == 'POST':
        id_tipo_concepto=request.POST['id_tipo_concepto']
        desc_categoria=request.POST['desc_categoria']
        try:
            data = {}
            rocordLast = ConceptoCategoria.objects.create( id_tipo_concepto=id_tipo_concepto,
                                                           desc_categoria=desc_categoria )
            data={'id_categoria': rocordLast.id_categoria,
                 'desc_categoria': rocordLast.desc_categoria}

        except Exception as e:
            data['error']=str( e )
            data['info_datos']=desc_categoria
        return JsonResponse( data )


def addConceptoMarca(request):
    if request.method == 'POST':
        id_tipo_concepto=request.POST['id_tipo_concepto']
        desc_marca=request.POST['desc_marca']
        try:
            data = {}
            rocordLast = ConceptoTipoMarca.objects.create( id_tipo_concepto=id_tipo_concepto,
                                                           desc_marca=desc_marca )
            data={'id_marca': rocordLast.id_marca,
                 'desc_marca': rocordLast.desc_marca}

        except Exception as e:
            data['error']=str( e )
            data['info_datos']=desc_marca
        return JsonResponse( data )


def addUnidadMedida(request):
    if request.method == 'POST':
        desc_unidad_medida=request.POST['desc_unidad_medida']
        abreb_unidad_medida=request.POST['abreb_unidad_medida']
        try:
            data = {}
            rocordLast = UnidadMedida.objects.create( desc_unidad_medida=desc_unidad_medida,
                                                      abreb_unidad_medida=abreb_unidad_medida )
            data={'id_unidad_medida': rocordLast.id_unidad_medida,
                  'desc_unidad_medida': rocordLast.desc_unidad_medida +' ('+ rocordLast.abreb_unidad_medida +')'}

        except Exception as e:
            data['error']=str( e )
            data['info_datos']=desc_unidad_medida
        return JsonResponse( data )

def addTipoServicio(request):
    if request.method == 'POST':

        desc_tipo_servicio=request.POST['desc_tipo_servicio']
        try:
            data = {}
            rocordLast = TipoServicio.objects.create(desc_tipo_servicio=desc_tipo_servicio)
            data={'id_tipo_servicio': rocordLast.id_tipo_servicio,
                 'desc_tipo_servicio': rocordLast.desc_tipo_servicio}

        except Exception as e:
            data['error']=str( e )
            data['info_datos']=desc_tipo_servicio
        return JsonResponse( data )

def SetParametros(request):
    if request.method == 'POST':
        data={}
        try:
            action=request.POST['action']
            if action == 'SetParametro':
                valor=request.POST['valor']
                cve_parametro=request.POST['cve_parametro']
                data=[]
                parametro=Parametros.objects.get(cve_parametro=cve_parametro)
                parametro.valor=valor
                parametro.save()
        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )


def getInfoUnidad(request):

    if request.method == 'POST':
        data={}
        try:
            action=request.POST['action']
            placa=request.POST['placa']
            if action == 'searchdata':
                data=[]
                owner = request.POST['owner']
                if (owner=='order-nueva'):
                    for i in WcUnidad.objects.filter(placa=placa):
                        data.append(i.toJSON())
                if (owner == 'neumaticos-admin'):
                    for i in WcUnidadNeu.objects.filter( placa=placa ):
                        data.append( i.toJSON() )

        except Exception as e:
            data = {}
            data['error']=str( e )

        return JsonResponse( data, safe=False )


def login(request):
    return render(request, 'registration/login.html')


def index(request):
    return render(request, 'index.html')


def panel(request):
    return render(request, 'panel.html')


def EsDemo(request):
    if request.method == 'POST':
        session=request.user.groups.all().values( 'name' )
        nombre=session[0]['name']
        data={"esDemo": (nombre == 'Demo') }
    return JsonResponse( data, safe=False )


def operacion(request):
    return render(request, 'orden/orden-operacion.html')






