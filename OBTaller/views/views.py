from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from OBTaller.forms import UnidadForm
from OBTaller.models import WCuentaAbierta, Unidad, WcUnidad, ConceptoCategoria, TipoServicio, Cliente


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




def OrdenNuevaView(request):
    # request['manobra']='active'



    context = {}
    context['nueva_orden'] = 'active'
    return render( request, 'orden/orden-nueva.html', context )

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data( **kwargs )
    #     context['title']='Ordenes de taller activas'
    #     # context['inventario']='active'
    #     context['escritorio']='active'
    #     # context['catalogos']='menu-is-opening menu-open'
    #     # context['unidades']='active'
    #     # context['create_url']=reverse_lazy( 'CBR:cbrenca_nueva' )
    #     # context['list_url']=reverse_lazy( 'CBR:cbrenca-list' )
    #     return context


def getInfoUnidad(request):


    if request.method == 'POST':
        data={}
        try:
            action=request.POST['action']
            placa=request.POST['placa']
            if action == 'searchdata':
                data=[]
                for i in WcUnidad.objects.filter( placa=placa ):
                    data.append( i.toJSON() )


        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )


#
# class UnidadView( LoginRequiredMixin, ListView ):
#     template_name='catalogos/unidad-list.html'
#     context_object_name='unidad_list'
#
#     def get_object(self):
#         id_unidad=self.kwargs.get( 'id_unidad' )
#         return get_object_or_404( WcUnidad , id_unidad=id_unidad )
#
#     def get_queryset(self):
#         return WcUnidad.objects.all()
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data( **kwargs )
#         context['catalogos']='menu-is-opening menu-open'
#         context['unidades']='active'
#         # context['cliente']=
#         return context
#
#
# class UnidadDetailView( DetailView ):
#     model=Unidad
#     template_name='catalogos/unidad-detail.html'
#
#     def get_object(self):
#         id_unidad=self.kwargs.get( 'id_unidad' )
#         return get_object_or_404( Unidad, id_unidad=id_unidad )
#
# def Unidadcreate(request):
#     if request.method == 'POST':
#         form = UnidadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('OBTaller:unidad-list')
#     form = UnidadForm()
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data( **kwargs )
#         return context
#
#     return render(request, 'catalogos/unidad-create.html', {'form': form})
#
# def Unidadedit(request, id_unidad, template_name='catalogos/unidad-edit.html'):
#     unidad = get_object_or_404(Unidad, id_unidad=id_unidad)
#     form = UnidadForm(request.POST or None, instance=unidad)
#
#
#     if form.is_valid():
#         form.save()
#         return redirect('OBTaller:unidad-list')
#     return render(request, template_name, {'form':form})
#
# def Unidaddelete(request, id_unidad, template_name='catalogos/confirm_delete.html'):
#     unidad = get_object_or_404(Unidad, id_unidad=id_unidad)
#     if request.method=='POST':
#         unidad.delete()
#         return redirect('OBTaller:unidad-list')
#     return render(request, template_name, {'object':unidad})









def login(request):
    return render(request, 'registration/login.html')


def index(request):
    return render(request, 'index.html')


def panel(request):
    return render(request, 'panel.html')



def operacion(request):
    return render(request, 'orden/orden-operacion.html')



class WCuentaAbiertaListView( ListView ):
    model=WCuentaAbierta
    template_name='orden/orden-operacion.html'

    # @method_decorator( csrf_exempt )
    @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs )

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'searchdata':
                data=[]
                position=1
                for i in WCuentaAbierta.objects.all():
                    item=i.toJSON()
                    # item['ID']=position
                    # item['archivobco']=i.archivobco.name
                    # item['archivoerp']=i.archivoerp.name
                    data.append( item )
                    position+=1
                print(data)
            else:
                data['error']='Ha ocurrido un error'
        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        context['title']='Ordenes de taller activas'
        # context['inventario']='active'
        context['escritorio']='active'
        # context['catalogos']='menu-is-opening menu-open'
        # context['unidades']='active'
        # context['create_url']=reverse_lazy( 'CBR:cbrenca_nueva' )
        # context['list_url']=reverse_lazy( 'CBR:cbrenca-list' )
        return context


