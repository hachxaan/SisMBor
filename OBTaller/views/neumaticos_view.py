from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from OBTaller.models import VwNeumaticosPosicion

class NeumaticosAdmin( ListView ):
    template_name = 'neumaticos/neumaticos-admin.html'
    model = VwNeumaticosPosicion

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            placa=request.POST['placa']
            action=request.POST['action']
            if action == 'searchdata':
                data = []
                # for i in VwNeumaticosPosicion.objects.all():
                for i in VwNeumaticosPosicion.objects.filter(placa=placa):
                    item = i.toJSON()
                    data.append(item)
            else:
                data['error']='Esta orden ya no se puede editar'
        except Exception as e:
            data['error']=str( e )
        return JsonResponse( data, safe=False )

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