from django.contrib.auth.decorators import login_required
import datetime as dt

from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from OBTaller import forms
from OBTaller.models import WCuentaAbierta, Orden, WConceptosMain, OrdenDetalle, Concepto, WOrdenDetalle, Personal


def UpdSitOrden(request):
    if request.method == 'POST':
        folio=request.POST.get( 'folio' )
        status=request.POST.get( 'status' )
        context={}
        try:
            Orden.objects.filter( folio=folio ).update( status=status )
            context['folio']=folio
        except Exception as e:
            context['error']=str( e )
        return JsonResponse( context, safe=False )


def OrdenNuevaView(request):
    # request['manobra']='active'
    context={}
    context['nueva_orden']='active'
    if request.method == 'GET':
        if request.GET.get( 'placa' ):
            context['placa']=request.GET.get( 'placa' )
        else:
            context['placa']=''
    return render( request, 'orden/orden-nueva.html', context )


class OrdenListaEditar( ListView ):
    model=WConceptosMain
    template_name='orden/orden-editar.html'
    # personal=Personal.objects.all();
    @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs )

    def post(self, request, *args, **kwargs):
        data={}
        try:
            folio=request.POST['folio']
            dataSet=Orden.objects.filter( folio=folio ).values( 'status' )
            status=dataSet[0]['status']
            if (status < 2):
                action=request.POST['action']
                if action == 'searchdata':

                    id_tipo_concepto = request.POST['id_tipo_concepto']
                    data=[]
                    print({"id_tipo_concepto": id_tipo_concepto})
                    for i in WConceptosMain.objects.filter(id_tipo_concepto=id_tipo_concepto):
                        item=i.toJSON()
                        data.append( item )
                if action == 'addItem':
                    result=self.pInsOrdenDetalle( request )

                if action == 'delItem':
                    result=self.pDelOrdenDetalle( request )

                if action == 'addTxReferencia':
                    result=self.pUpdTxReferencia( request )

                if action == 'addNoSerie':
                    result=self.pUpdNoSerie( request )

                if action == 'addPersonal':
                    result=self.pUpdPersonal( request )

                if action == 'addsOrden':
                    result=self.pAddsOrden( request )

                if action == 'OrdenDetalle':
                    data=[]

                    for i in WOrdenDetalle.objects.filter(folio=folio, sit_code='PE'):
                        item=i.toJSON()
                        data.append( item )
                    # else:
                    #     data.append({ 'error':'Esta orden ya no se puede editar'})
            else:
                data['error']='Esta orden ya no se puede editar'

        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

    def pAddsOrden(self, request ):
        folio=request.POST['folio']

        for addsOrdem in OrdenDetalle.objects.filter( folio=folio ):
            addsOrdem.sit_code='AC'
            addsOrdem.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pUpdTxReferencia(self, request ):
        id_orden_detalle=request.POST['id_orden_detalle']
        tx_referencia=request.POST['tx_referencia']
        delOrdenDetalle=OrdenDetalle.objects.get( id_orden_detalle=id_orden_detalle )
        delOrdenDetalle.tx_referencia=tx_referencia
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pUpdNoSerie(self, request ):
        id_orden_detalle=request.POST['id_orden_detalle']
        no_serie=request.POST['no_serie']
        delOrdenDetalle=OrdenDetalle.objects.get( id_orden_detalle=id_orden_detalle )
        delOrdenDetalle.no_serie=no_serie
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pUpdPersonal(self, request ):
        id_orden_detalle=request.POST['id_orden_detalle']
        id_personal=request.POST['id_personal']
        delOrdenDetalle=OrdenDetalle.objects.get( id_orden_detalle=id_orden_detalle )
        delOrdenDetalle.id_personal=id_personal
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data


    def pDelOrdenDetalle(self, request):
        data={}
        id_orden_detalle=request.POST['id_orden_detalle']
        delOrdenDetalle = OrdenDetalle.objects.get(id_orden_detalle=id_orden_detalle)
        delOrdenDetalle.sit_code = 'CA'
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pInsOrdenDetalle(self, request):
        data={}

        stock=request.POST['stock']
        # try:
        data=[]
        if (stock == 0):

            data['error']='Sin Stock. Agregue stock en Inventario.'
        else:
            folio=request.POST['folio']
            id_concepto=request.POST['id_concepto']
            id_personal=request.POST['id_personal']
            no_serie=request.POST['no_serie']

            consecutivo=OrdenDetalle.objects.filter( folio=folio ).count()
            if (consecutivo > 0):
                MaxCons=OrdenDetalle.objects.filter( folio=folio ).aggregate( Max( 'consecutivo' ) )
                consecutivo=MaxCons['consecutivo__max']

            dataSet=Concepto.objects.filter( id_concepto=id_concepto ).values( 'stock', 'precio_compra',
                                                                               'precio_venta' );
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
                cve_usu_alta=request.user.username,
                fh_registro=dt.datetime.today(),
                sit_code='PE')
            InsOrdenDetalle.save()
            data={"psSTR_RESP": 'OK', "consecutivo": consecutivo, "stock": stock}

        return data


    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        context['title']='Agregar conceptos a orden'
        context['escritorio']='active'
        context['personal']= Personal.objects.all();
        return context


class OrdenListaDetalle( ListView ):
    model=WConceptosMain
    template_name='orden/orden-detalle.html'
    # personal=Personal.objects.all();
    @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs )

    def post(self, request, *args, **kwargs):
        data={}
        try:
            folio=request.POST['folio']
            action=request.POST['action']
            if action == 'searchdata':

                id_tipo_concepto = request.POST['id_tipo_concepto']
                data=[]
                print({"id_tipo_concepto": id_tipo_concepto})
                for i in WConceptosMain.objects.filter(id_tipo_concepto=id_tipo_concepto):
                    item=i.toJSON()
                    data.append( item )
            if action == 'addItem':
                result=self.pInsOrdenDetalle( request )

            if action == 'delItem':
                result=self.pDelOrdenDetalle( request )

            if action == 'addTxReferencia':
                result=self.pUpdTxReferencia( request )

            if action == 'addNoSerie':
                result=self.pUpdNoSerie( request )

            if action == 'addPersonal':
                result=self.pUpdPersonal( request )

            if action == 'addsOrden':
                result=self.pAddsOrden( request )

            if action == 'OrdenDetalle':
                data=[]
                for i in WOrdenDetalle.objects.filter(folio=folio, sit_code='AC'):
                    item=i.toJSON()
                    data.append( item )

        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

    def pAddsOrden(self, request ):
        folio=request.POST['folio']

        for addsOrdem in OrdenDetalle.objects.filter( folio=folio ):
            addsOrdem.sit_code='AC'
            addsOrdem.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pUpdTxReferencia(self, request ):
        id_orden_detalle=request.POST['id_orden_detalle']
        tx_referencia=request.POST['tx_referencia']
        delOrdenDetalle=OrdenDetalle.objects.get( id_orden_detalle=id_orden_detalle )
        delOrdenDetalle.tx_referencia=tx_referencia
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pUpdNoSerie(self, request ):
        id_orden_detalle=request.POST['id_orden_detalle']
        no_serie=request.POST['no_serie']
        delOrdenDetalle=OrdenDetalle.objects.get( id_orden_detalle=id_orden_detalle )
        delOrdenDetalle.no_serie=no_serie
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pUpdPersonal(self, request ):
        id_orden_detalle=request.POST['id_orden_detalle']
        id_personal=request.POST['id_personal']
        delOrdenDetalle=OrdenDetalle.objects.get( id_orden_detalle=id_orden_detalle )
        delOrdenDetalle.id_personal=id_personal
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data


    def pDelOrdenDetalle(self, request):
        data={}
        id_orden_detalle=request.POST['id_orden_detalle']
        delOrdenDetalle = OrdenDetalle.objects.get(id_orden_detalle=id_orden_detalle)
        delOrdenDetalle.sit_code = 'CA'
        delOrdenDetalle.save()
        data={"psSTR_RESP": 'OK'}
        return data

    def pInsOrdenDetalle(self, request):
        data={}

        stock=request.POST['stock']
        # try:
        data=[]
        if (stock == 0):

            data['error']='Sin Stock. Agregue stock en Inventario.'
        else:
            folio=request.POST['folio']
            id_concepto=request.POST['id_concepto']
            id_personal=request.POST['id_personal']
            no_serie=request.POST['no_serie']

            consecutivo=OrdenDetalle.objects.filter( folio=folio ).count()
            if (consecutivo > 0):
                MaxCons=OrdenDetalle.objects.filter( folio=folio ).aggregate( Max( 'consecutivo' ) )
                consecutivo=MaxCons['consecutivo__max']

            dataSet=Concepto.objects.filter( id_concepto=id_concepto ).values( 'stock', 'precio_compra',
                                                                               'precio_venta' );
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
                cve_usu_alta=request.user.username,
                fh_registro=dt.datetime.today(),
                sit_code='PE')
            InsOrdenDetalle.save()
            data={"psSTR_RESP": 'OK', "consecutivo": consecutivo, "stock": stock}

        return data


    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        context['title']='Agregar conceptos a orden'
        context['escritorio']='active'
        context['personal']= Personal.objects.all();
        folio= self.request.GET['folio']
        dataSet = WCuentaAbierta.objects.filter(folio=folio).values('status', 'placa', 'cliente', 'kilometraje' )
        context['placa'] =dataSet[0]['placa']
        context['cliente'] =dataSet[0]['cliente']
        context['kilometraje'] =dataSet[0]['kilometraje']
        context['status'] =dataSet[0]['status']


        return context


class WCuentaAbiertaListView( ListView ):
    model=WCuentaAbierta
    template_name='orden/orden-operacion.html'

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
                    data.append( item )
                    position+=1

            else:
                data['error']='Ha ocurrido un error'
        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        context['title']='Ordenes de taller activas'
        context['escritorio']='active'
        context['icono']='fa-desktop'
        return context
