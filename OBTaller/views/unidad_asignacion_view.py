from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from OBTaller.models import UnidadAsignacion


class UnidadAsignacionView(TemplateView):
    template_name = 'operacion/unidad_asignacion.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'searchdata':
                data = []
                for i in UnidadAsignacion.objects.filter(sit_code=1):
                    item = i.toJSON()
                    data.append(item)


            # if action == 'setNeumaticoAsignacion':
            #     data = []
            #     data = self.pInsUnidadNeumatico(request)
            # if action == 'pDesinstalaNeumatico':
            #     data = []
            #     data = self.pDesinstalaNeumatico(request)

            # else:
            #     data['error']='Esta orden ya no se puede editar'
        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )


    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        # if self.request.GET.get('placa'):

        fieldsColums = []
        titleFields = []
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM unidad_asignacion''')
        width = 100 / len(cursor.description)
        for field in cursor.description:
            if field[0].lower() != 'id':
                fieldsColums.append({"data": field[0].lower()})
                titleFields.append({"field_title": field[0]})

        context['width'] = width
        context['fieldsColums'] = fieldsColums
        context['titleFields'] = titleFields

        return context