import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db import connection
from django.views.generic import ListView, DetailView

from OBTaller.mixins import ValidatePermissionRequiredMixin, ValidaTemp2, ValidaTemp1, ValidaPerfilMixin
from OBTaller.models import Reportes


class ReportesView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView, DetailView):
    model = Reportes
    template_name ='reportes_list.html'
    # permission_required = 'OBTaller.view_unidad'


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_reporte=self.kwargs.get( 'id_reporte' )
        return get_object_or_404( Reportes , id_reporte=id_reporte )

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # request.session['reporte_id'] = 52
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                id_reporte = request.POST['id_reporte']
                reporte = Reportes.objects.get(id_reporte=id_reporte)
                vista = reporte.vista
                ID = 0
                cursor = connection.cursor()
                cursor.execute('''SELECT * FROM ''' + vista)
                vwr_dataset = cursor.fetchall()
                indexField = 0

                for i in vwr_dataset:
                    ID += 1
                    item = {}
                    item['id'] = ID
                    for field in cursor.description:
                        fieldname = field[0].lower()
                        dato = i[indexField]
                        item[fieldname] = dato
                        indexField += 1
                    indexField=0
                    data.append(item)

            else:
                data = {}
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_reporte = self.kwargs.get('id_reporte')
        reporte = Reportes.objects.get(id_reporte=id_reporte)
        titulo_reporte = reporte.titulo_reporte
        filename = reporte.nom_file

        context['title'] = reporte.titulo_reporte+' / '+reporte.desc_reporte
        context['entity'] = 'Reportes.'

        context['reportes'] = 'menu-is-opening menu-open'
        # context[reporte.vista] = 'active'

        # --------------------------------------
        fieldsColums = []
        titleFields = []
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM '''+reporte.vista)
        width = 100 / len(cursor.description)
        for field in cursor.description:
            if field[0].lower() != 'id':
                fieldsColums.append({"data": field[0].lower()})
                titleFields.append({"field_title": field[0]})


        context['titulo_reporte'] = titulo_reporte
        context['filename'] = filename
        context['width'] = width
        context['id_reporte'] = id_reporte
        context['fieldsColums'] = fieldsColums
        context['titleFields'] = titleFields

        return context