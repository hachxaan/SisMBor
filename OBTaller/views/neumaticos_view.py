from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import JsonResponse
import datetime as dt
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from OBTaller.models import VwNeumaticosPosicion, WConceptosMain, Orden, Concepto, UnidadNeumatico, OrdenDetalle
from appMainSite.const import TCONCEPTO_NEUMATICOS


class NeumaticosAdmin( ListView ):
    template_name = 'neumaticos/neumaticos-admin.html'
    model = VwNeumaticosPosicion

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:

            action=request.POST['action']
            if action == 'searchdata':
                placa = request.POST['placa']
                data = []
                # for i in VwNeumaticosPosicion.objects.all():
                for i in VwNeumaticosPosicion.objects.filter(placa=placa):
                    item = i.toJSON()
                    data.append(item)
            if action == 'getNeumaticosStock':
                data = []
                for i in WConceptosMain.objects.filter(id_tipo_concepto=TCONCEPTO_NEUMATICOS):
                    item = i.toJSON()
                    data.append(item)
            if action == 'setNeumaticoAsignacion':
                data = []
                data = self.pInsUnidadNeumatico(request)

            # else:
            #     data['error']='Esta orden ya no se puede editar'
        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

    def pInsOrdenDetalle(self, folio, id_concepto, no_serie, username):
        data={}
        id_personal=0
        consecutivo=OrdenDetalle.objects.filter( folio=folio ).count()
        if (consecutivo > 0):
            MaxCons=OrdenDetalle.objects.filter( folio=folio ).aggregate( Max( 'consecutivo' ) )
            consecutivo=MaxCons['consecutivo__max']

        dataSet=Concepto.objects.filter( id_concepto=id_concepto ).values( 'stock', 'precio_compra',
                                                                           'precio_venta' )
        precio_compra=dataSet[0]['precio_compra']
        precio_venta=dataSet[0]['precio_venta']
        stock=dataSet[0]['stock']

        InsOrdenDetalle=OrdenDetalle(
            folio=folio,
            consecutivo=consecutivo + 1,
            cantidad=1,
            id_concepto=id_concepto,
            id_personal=id_personal,
            no_serie=no_serie,
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            cve_usu_alta=username,
            fh_registro=dt.datetime.today(),
            sit_code='PE')
        InsOrdenDetalle.save()

        lasterOrdenDetalle = OrdenDetalle.objects.latest('id_orden_detalle')
        print(lasterOrdenDetalle.id_orden_detalle)

        updOrdenDetalle = OrdenDetalle.objects.get(id_orden_detalle=lasterOrdenDetalle.id_orden_detalle)
        updOrdenDetalle.sit_code = 'AC'
        updOrdenDetalle.save()
        data={"psSTR_RESP": 'OK', "consecutivo": consecutivo, "stock": stock}

        return data

    def pInsUnidadNeumatico(self, request):
        data={}
        folio=request.POST['folio']
        dataSet = Orden.objects.filter(folio=folio).values('status',
                                                           'id_unidad',
                                                           'kilometraje' )
        id_unidad = dataSet[0]['id_unidad']
        posicion = request.POST['posicion']
        if UnidadNeumatico.objects.filter(id_unidad=id_unidad, posicion=posicion).exists():
            data['error'] = 'Ya existe neumático en esta posición, seleccione actualizar neumático.'
        else:
            status = dataSet[0]['status']
            if (status in [0, 1]):
                id_concepto = request.POST['id_concepto']
                neumatocoStock = Concepto.objects.get(id_concepto=id_concepto)
                if (neumatocoStock.stock > 0):

                    kilometraje = dataSet[0]['kilometraje']

                    no_serie=request.POST['no_serie']
                    tx_referencia=request.POST['tx_referencia']
                    cve_usu_alta = request.user.username
                    fh_alta = dt.datetime.today()
                    sit_code = 0

                    InsUnidadNeumatico = UnidadNeumatico(
                        id_unidad=id_unidad,
                        posicion=posicion,
                        fh_alta=fh_alta,
                        cve_usu_alta=cve_usu_alta,
                        kilometraje=kilometraje,
                        folio=folio,
                        tx_referencia=tx_referencia,
                        id_concepto=id_concepto,
                        no_serie=no_serie,
                        sit_code=sit_code)

                    InsUnidadNeumatico.save()
                    self.pInsOrdenDetalle(folio, id_concepto, no_serie, cve_usu_alta)
                    data = {"psSTR_RESP": 'OK'}

                else:
                    data['error'] = 'Sin Stock. Agregue stock en Inventario de Neumáticos.'
            else:
                data['error'] = 'Se requiere que la orden esté en proceso.'

        return data

    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )

        if self.request.GET.get('placa'):
            context['placa'] = self.request.GET.get('placa')
        else:
            context['placa'] = ''
        context['neumaticos_admin'] = 'active'

        return context

# def NeumaticosAdmin(request):
#     context = {}
#
#     if request.method == 'GET':
#         if request.GET.get('placa'):
#             context['placa'] = request.GET.get('placa')
#
#             id_tipo_eje = 0
#             for dataSet in VwNeumaticosPosicion.objects.filter(id_tipo_eje = id_tipo_eje):
#                 print(dataSet.cons)
#
#
#         else:
#             context['placa'] = ''
#
#     context['neumaticos'] = 'active'
#
#     return render( request, 'neumaticos/neumaticos-admin.html',context)