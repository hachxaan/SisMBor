from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from OBTaller.models import WCuentaAbierta, Orden


def UpdSitOrden(request):
    if request.method == 'POST':
        folio = request.POST.get('folio')
        status = request.POST.get( 'status' )
        context = {}
        try:
            Orden.objects.filter( folio=folio ).update( status=status )
            context['folio'] = folio
        except Exception as e:
            context['error'] = str( e )
        return JsonResponse( context, safe=False )

def OrdenNuevaView(request):
    # request['manobra']='active'
    context = {}
    context['nueva_orden']='active'
    if request.method == 'GET':
        if request.GET.get('placa'):
            context['placa'] = request.GET.get('placa')
        else:
            context['placa'] =''
    return render( request, 'orden/orden-nueva.html', context )



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
                print(data)
            else:
                data['error']='Ha ocurrido un error'
        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        context['title']='Ordenes de taller activas'
        context['escritorio']='active'
        return context