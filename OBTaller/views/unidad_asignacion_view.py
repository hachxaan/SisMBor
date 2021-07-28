import random
import string

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView

from OBTaller.mixins import ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, ValidatePermissionRequiredMixin
from OBTaller.models import WUnidadAsignacion, Personal, Unidad, UnidadAsignacion, Cliente, WCombustibleTicket, \
    UnidadCombustible, WPeajeTicket, UnidadPeaje
from OBTaller.operador.forms import UnidadCombustibleForm, UnidadPeajeForm
from appMainSite.const import TPERSONAL_OPERADOR_UNIDAD

class UnidadCombustibleTicketView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, TemplateView):
    template_name = 'operacion/unidad_tickets_combustible.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # id_unidad_asigna
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'searchdata':
                data = []
                id_unidad_asigna = request.POST['id_unidad_asigna']

                for i in WCombustibleTicket.objects.filter(id_unidad_asigna=id_unidad_asigna):
                # for i in WUnidadAsignacion.objects.filter( Q(sit_code=1) | Q(sit_code=0)):
                    item = i.toJSON()
                    data.append(item)
            # if action == 'asigna_personal':
            #     data = self.pAsignaUnidad(request)


        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )
    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )

        id_unidad = self.request.GET.get('id_unidad')
        id_unidad_asigna = self.request.GET.get('id_unidad_asigna')

        qryWUnidadAsignacion = WUnidadAsignacion.objects.get(id_unidad_asigna=id_unidad_asigna)
        sit_code = qryWUnidadAsignacion.sit_code
        status = qryWUnidadAsignacion.status
        context['status_desc'] = status
        if (sit_code == 0):
            context['status_tipo'] = 'warning'
        if (sit_code == 1):
            context['status_tipo']='info'
        if (sit_code == 2):
            context['status_tipo']='success'

        qryUnidad = Unidad.objects.get(id_unidad=id_unidad)


        context['id_unidad_asigna'] = qryWUnidadAsignacion.id_unidad_asigna
        context['id_unidad'] = qryWUnidadAsignacion.id_unidad
        context['entrada'] = qryWUnidadAsignacion.id_unidad_asigna
        context['placa'] = qryUnidad.placa
        context['nombre_operador'] = qryWUnidadAsignacion.nombre_operador
        context['total_combustible'] = qryWUnidadAsignacion.total_combustible_s
        context['cliente'] = qryWUnidadAsignacion.nombre_empresa
        context['fh_asignacion'] = qryWUnidadAsignacion.fh_asignacion
        context['fh_entrega'] = qryWUnidadAsignacion.fh_entrega
        context['sit_code'] = qryWUnidadAsignacion.sit_code


        fieldsColums = []
        titleFields = []

        fieldsColums.append({"data": 'id_unidad_combustible'})
        fieldsColums.append({"data": 'fh_ticket'})
        fieldsColums.append({"data": 'tx_referencia'})
        fieldsColums.append({"data": 'cantidad'})
        fieldsColums.append({"data": 'imp_ticket_s'})
        fieldsColums.append({"data": 'img_ticket'})
        fieldsColums.append({"data": 'fh_registro'})

        # for fieldname in WCombustibleTicket._meta.fields:
        #     fieldsColums.append({"data": fieldname.name})
        unida_medida_combustible = qryUnidad.get_unida_medida_combustible_display()
        titleFields.append({"field_title": 'Entrada', "width": '3'})
        titleFields.append({"field_title": 'Fecha Ticket', "width": '15'})
        titleFields.append({"field_title": 'Título/Referencia', "width": '20'})
        titleFields.append({"field_title": 'Cantidad ' + unida_medida_combustible, "width": '10'})
        titleFields.append({"field_title": 'Importe', "width": '10'})
        titleFields.append({"field_title": 'Foto', "width": '5'})
        titleFields.append({"field_title": 'Fecha Registro', "width": '15'})

        context['fieldsColums'] = fieldsColums
        context['titleFields'] = titleFields
        context['operacion'] = 'menu-is-opening menu-open'
        context['unidad_asignacion'] = 'active'

        return context


class UnidadPeajeTicketView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, TemplateView):
    template_name = 'operacion/unidad_tickets_peaje.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'searchdata':
                data = []
                id_unidad_asigna = request.POST['id_unidad_asigna']
                for i in WPeajeTicket.objects.filter(id_unidad_asigna=id_unidad_asigna):
                    item = i.toJSON()
                    data.append(item)

        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )
    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )

        id_unidad = self.request.GET.get('id_unidad')
        id_unidad_asigna = self.request.GET.get('id_unidad_asigna')

        qryWUnidadAsignacion = WUnidadAsignacion.objects.get(id_unidad_asigna=id_unidad_asigna)
        sit_code = qryWUnidadAsignacion.sit_code
        status = qryWUnidadAsignacion.status
        context['status_desc'] = status
        if (sit_code == 0):
            context['status_tipo'] = 'warning'
        if (sit_code == 1):
            context['status_tipo']='info'
        if (sit_code == 2):
            context['status_tipo']='success'

        qryUnidad = Unidad.objects.get(id_unidad=id_unidad)


        context['id_unidad_asigna'] = qryWUnidadAsignacion.id_unidad_asigna
        context['id_unidad'] = qryWUnidadAsignacion.id_unidad
        context['entrada'] = qryWUnidadAsignacion.id_unidad_asigna
        context['placa'] = qryUnidad.placa
        context['nombre_operador'] = qryWUnidadAsignacion.nombre_operador
        context['total_peaje_s'] = qryWUnidadAsignacion.total_peaje_s
        context['cliente'] = qryWUnidadAsignacion.nombre_empresa
        context['fh_asignacion'] = qryWUnidadAsignacion.fh_asignacion
        context['fh_entrega'] = qryWUnidadAsignacion.fh_entrega
        context['sit_code'] = qryWUnidadAsignacion.sit_code


        fieldsColums = []
        titleFields = []

        fieldsColums.append({"data": 'id_unidad_peaje'})
        fieldsColums.append({"data": 'fh_ticket'})
        fieldsColums.append({"data": 'tx_referencia'})
        # fieldsColums.append({"data": 'cantidad'})
        fieldsColums.append({"data": 'imp_ticket_s'})
        fieldsColums.append({"data": 'img_ticket'})
        fieldsColums.append({"data": 'fh_registro'})

        # for fieldname in WCombustibleTicket._meta.fields:
        #     fieldsColums.append({"data": fieldname.name})
        # unida_medida_combustible = qryUnidad.get_unida_medida_combustible_display()
        titleFields.append({"field_title": 'Entrada', "width": '3'})
        titleFields.append({"field_title": 'Fecha Ticket', "width": '15'})
        titleFields.append({"field_title": 'Título/Referencia', "width": '20'})
        # titleFields.append({"field_title": 'Cantidad ' + unida_medida_combustible, "width": '10'})
        titleFields.append({"field_title": 'Importe', "width": '10'})
        titleFields.append({"field_title": 'Foto', "width": '5'})
        titleFields.append({"field_title": 'Fecha Registro', "width": '15'})

        context['fieldsColums'] = fieldsColums
        context['titleFields'] = titleFields
        context['operacion'] = 'menu-is-opening menu-open'
        context['unidad_asignacion'] = 'active'

        return context

class UnidadAsignacionView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, TemplateView):
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
                for i in WUnidadAsignacion.objects.all():
                # for i in WUnidadAsignacion.objects.filter( Q(sit_code=1) | Q(sit_code=0)):
                    item = i.toJSON()
                    data.append(item)
            if action == 'asigna_personal':
                data = self.pAsignaUnidad(request)
            if action == 'gen_code_asignacion':
                data = self.pEntregaUnidad(request)
            if action == 'recibe_unidad':
                data = self.pRecibeUnidad(request)

        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )
    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        context['personal'] = Personal.objects.filter(id_tipo_personal = TPERSONAL_OPERADOR_UNIDAD)
        fieldsColums = []
        titleFields = []
        for fieldname in WUnidadAsignacion._meta.fields:
            fieldsColums.append({"data": fieldname.name})

        titleFields.append({"field_title": 'Entrado', "width": '3'})
        titleFields.append({"field_title": 'Placa', "width": '5'})
        titleFields.append({"field_title": 'Empresa', "width": '20'})
        titleFields.append({"field_title": 'Operador', "width": '15'})
        titleFields.append({"field_title": 'Acceso', "width": '5'})
        titleFields.append({"field_title": 'Estado', "width": '8'})
        titleFields.append({"field_title": 'Fecha Asignado', "width": '11'})
        titleFields.append({"field_title": 'Feche Entregado', "width": '11'})
        titleFields.append({"field_title": 'Total Combustible', "width": '12'})
        titleFields.append({"field_title": 'Total Peaje', "width": '12'})

        context['fieldsColums'] = fieldsColums
        context['titleFields'] = titleFields
        context['operacion'] = 'menu-is-opening menu-open'
        context['unidad_asignacion'] = 'active'

        return context

    def pEntregaUnidad(self, request):
        data = {}
        id_unidad_asigna = request.POST['id_unidad_asigna']

        NoEncotrado = True
        while NoEncotrado:
            cod_acceso = int(''.join(random.choice(string.digits) for x in range(6)))
            NoEncotrado = UnidadAsignacion.objects.filter(cod_acceso=cod_acceso).exists() or cod_acceso <= 99999

        updUnidadAsignacion = UnidadAsignacion.objects.get(id_unidad_asigna=id_unidad_asigna)
        updUnidadAsignacion.sit_code = 1
        updUnidadAsignacion.cod_acceso = cod_acceso
        updUnidadAsignacion.fh_asignacion = timezone.now()
        updUnidadAsignacion.save()

        data['ok'] = 'ok'
        return data

    def pRecibeUnidad(self, request):
        data = {}
        id_unidad_asigna = request.POST['id_unidad_asigna']
        cod_acceso = 0

        updUnidadAsignacion = UnidadAsignacion.objects.get(id_unidad_asigna=id_unidad_asigna)
        updUnidadAsignacion.sit_code = 2
        updUnidadAsignacion.cod_acceso = cod_acceso
        updUnidadAsignacion.fh_entrega = timezone.now()
        updUnidadAsignacion.save()

        data['ok']='ok'
        return data

    def pAsignaUnidad(self, request):
        data = {}
        placa = request.POST['placa']
        id_personal = request.POST['id_personal']
        tx_referencia = request.POST['tx_referencia']
        dtUnidad = Unidad.objects.filter(placa=placa).values('id_unidad')
        # if not Unidad.objects.filter(placa=placa).exists():
        if (len(dtUnidad) == 0):
            data['error'] = 'No existe unidad la placa ingresada [' + placa + '].'
        else:
            id_unidad = dtUnidad[0]['id_unidad']

            query = Q(sit_code=0)
            query.add(Q(sit_code=1), Q.OR)
            query.add(Q(id_unidad=id_unidad), Q.AND)

            if UnidadAsignacion.objects.filter(query).exists():
            # if UnidadAsignacion.objects.filter(id_unidad=id_unidad Q(sit_code=1) | Q(sis_code=0)).exists():
                qryUnidadAsignacion = UnidadAsignacion.objects.filter(query).values('id_personal')
                id_personal_inv = qryUnidadAsignacion[0]['id_personal']
                qryPersona = Personal.objects.filter(id_personal = id_personal_inv).values('nombre', 'apellido')
                nombre_operador_inv = qryPersona[0]['nombre'] + ' ' + qryPersona[0]['apellido']
                data['error'] = 'La unidad está actualmente asignada a [' + nombre_operador_inv + '].'
            else:
                query = Q(sit_code=0)
                query.add(Q(sit_code=1), Q.OR)
                query.add(Q(id_personal=id_personal), Q.AND)

                if UnidadAsignacion.objects.filter(query).exists():
                    qryUnidadAsignacion = UnidadAsignacion.objects.filter(query).values('id_unidad')
                    id_unidad_inv = qryUnidadAsignacion[0]['id_unidad']
                    qryUnidad = Unidad.objects.filter(id_unidad=id_unidad_inv).values('placa')
                    placa_inv = qryUnidad[0]['placa']
                    data['error'] = 'El operador seleccionado ya tienen una unidad asignada. Placa: ['+ placa_inv +']'
                else:
                    dtUnidad = Unidad.objects.get(id_unidad=id_unidad)
                    laPersona = Personal.objects.get(id_personal=id_personal)
                    InsUnidadAsignacion = UnidadAsignacion(
                        id_unidad=dtUnidad,
                        id_personal=laPersona,
                        cod_acceso=0,
                        sit_code=0  ,
                        )
                    InsUnidadAsignacion.save(force_insert=True)
                    data['ok'] = 'ok'
        return data



# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadCombustibleAdminCreateView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = UnidadCombustible
    form_class = UnidadCombustibleForm
    template_name = 'operacion/create_combustible_admin.html'
    success_url = reverse_lazy('OBTaller:unidad_combustible_ticket')
    # permission_required = 'OB. add_personal'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data = {}
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Ticket Combustible'
        context['entity'] = 'Combustible'
        context['list_url'] = self.success_url
        context['action'] = 'add'

        id_unidad_asigna = self.kwargs['id_unidad_asigna']

        Asignacion = WUnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        id_unidad = Asignacion[0]['id_unidad']
        qryUnidad = Unidad.objects.get(id_unidad=id_unidad)
        context['unida_medida_combustible'] = qryUnidad.get_unida_medida_combustible_display()
        context['id_unidad_asigna'] = id_unidad_asigna
        context['id_unidad'] = id_unidad
        context['list_url_comp'] = f'{self.success_url}?id_unidad_asigna={id_unidad_asigna}&id_unidad={id_unidad}'
        # context['list_url'] = '{}?id_unidad_asigna={}&id_unidad={}'.format(self.success_url, id_unidad_asigna, id_unidad)



        # context['cod_acceso'] = cod_acceso
        # context['catalogos'] = 'menu-is-opening menu-open'
        # context['personal'] = 'active'
        return context



# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadPeajeAdminCreateView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = UnidadPeaje
    form_class = UnidadPeajeForm
    template_name = 'operacion/create_combustible_admin.html'
    success_url = reverse_lazy('OBTaller:unidad_peaje_ticket')
    # permission_required = 'OB. add_personal'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data = {}
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Ticket Peaje'
        context['entity'] = 'Peaje'
        context['list_url'] = self.success_url
        context['action'] = 'add'

        id_unidad_asigna = self.kwargs['id_unidad_asigna']

        Asignacion = WUnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        id_unidad = Asignacion[0]['id_unidad']


        context['id_unidad_asigna'] = id_unidad_asigna
        context['id_unidad'] = id_unidad
        context['list_url_comp'] = f'{self.success_url}?id_unidad_asigna={id_unidad_asigna}&id_unidad={id_unidad}'
        # context['list_url'] = '{}?id_unidad_asigna={}&id_unidad={}'.format(self.success_url, id_unidad_asigna, id_unidad)



        # context['cod_acceso'] = cod_acceso
        # context['catalogos'] = 'menu-is-opening menu-open'
        # context['personal'] = 'active'
        return context


