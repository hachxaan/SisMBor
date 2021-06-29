from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from OBTaller.mixins import ValidatePermissionRequiredMixin
from OBTaller.models import Reportes, UnidadNeumatico


class ReportesView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView, DetailView):
    model = Reportes
    template_name ='reportes_list.html'
    # permission_required = 'OBTaller.view_unidad'


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_reporte=self.kwargs.get( 'id_reporte' )
        return get_object_or_404( Reportes , id_reporte=id_reporte )

    # def get(self, request):
    #     test = request
    #     print(test)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                id_reporte = request.POST['id_reporte']
                # if id_reporte == '1':
                #     for i in UnidadNeumatico.objects.all():
                #         data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes'
        # context['create_url'] = reverse_lazy('OBTaller:manobra_create')
        # context['list_url'] = reverse_lazy('OBTaller:manobra_list')
        id_reporte = self.kwargs.get('id_reporte')
        reporte = Reportes.objects.get(id_reporte=id_reporte)


        context['entity'] = 'Reportes.'
        context['reportes'] = 'menu-is-opening menu-open'
        # context[reporte.vista] = 'active'

        # --------------------------------------
        context['id_reporte'] = id_reporte
        context['fieldsColums'] = [{"data": "id_posicion"},{"data": "fh_alta"}]
        context['titleFields'] = [{"field_title": "ID"},{"field_title": "Fecha Alta"}]

        return context