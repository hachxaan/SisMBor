import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from OBTaller.mixins import ValidaTemp2, ValidaTemp1, ValidaPerfilMixin, ValidatePermissionRequiredMixin
from OBTaller.models import WCombustibleTicket, WUnidadAsignacion, UnidadCombustible, UnidadAsignacion, Unidad, \
    OperadorSession, UnidadPeaje, WPeajeTicket
from OBTaller.operador.forms import UnidadCombustibleForm, UnidadPeajeForm
from appMainSite import settings
from appMainSite.settings import BASE_DIR


class IndexOperadorView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, TemplateView):
    template_name = 'operacion/registro/index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )
        session_key = self.request.session.session_key
        dataSetOperadorSession = OperadorSession.objects.filter(session_key=session_key).values('id_unidad_asigna')
        id_unidad_asigna = dataSetOperadorSession[0]['id_unidad_asigna']
        Tickets_com = WCombustibleTicket.objects.filter(id_unidad_asigna=id_unidad_asigna)
        Tickets_pej = WPeajeTicket.objects.filter(id_unidad_asigna=id_unidad_asigna)
        Asignacion = WUnidadAsignacion.objects.get(id_unidad_asigna=id_unidad_asigna)
        context['nombre_operador'] = Asignacion.nombre_operador
        context['placa'] = Asignacion.placa
        context['Tickets_com'] = Tickets_com
        context['Tickets_pej'] = Tickets_pej
        context['id_unidad_asigna'] = id_unidad_asigna
        # context['cod_acceso'] = Asignacion.cod_accesos
        context['MEDIA_ROOT'] = settings.BASE_URL_MEDIA

        return context

# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadCombustibleCreateView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = UnidadCombustible
    form_class = UnidadCombustibleForm
    template_name = 'operacion/registro/create_combustible.html'
    success_url = reverse_lazy('operador:index_operador')
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
        # id_unidad_asigna = self.request

        # cod_acceso = self.request.post["cod_acceso"]
        # qryUnidadAsignacion = UnidadAsignacion.objects.get(cod_acceso=cod_acceso)
        # id_unidad_asigna = qryUnidadAsignacion.id_unidad_asigna
        # cod_acceso = qryUnidadAsignacion.cod_acceso

        session_key = self.request.session.session_key
        dataSetOperadorSession = OperadorSession.objects.filter(session_key=session_key).values('id_unidad_asigna')
        id_unidad_asigna = dataSetOperadorSession[0]['id_unidad_asigna']

        Asignacion = WUnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        qryUnidad = Unidad.objects.get(id_unidad=Asignacion[0]['id_unidad'])
        context['unida_medida_combustible'] = qryUnidad.get_unida_medida_combustible_display()
        context['id_unidad_asigna'] = id_unidad_asigna
        # context['cod_acceso'] = cod_acceso
        # context['catalogos'] = 'menu-is-opening menu-open'
        # context['personal'] = 'active'
        return context


# **********************************************************************************************************************
# **********************************************************************************************************************

class UnidadCombustibleUpdateView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = UnidadCombustible
    form_class = UnidadCombustibleForm
    template_name = 'operacion/registro/create_combustible.html'
    success_url = reverse_lazy('operador:index_operador')
    # permission_required = 'OB. add_personal'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_unidad_combustible=self.kwargs.get( 'id_unidad_combustible' )
        return get_object_or_404( UnidadCombustible , id_unidad_combustible=id_unidad_combustible )

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
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
        context['title'] = 'Editar Ticket Combustible'
        context['entity'] = 'Combustible'
        context['list_url'] = self.success_url
        context['action'] = 'edit'

        session_key = self.request.session.session_key
        dataSetOperadorSession = OperadorSession.objects.filter(session_key=session_key).values('id_unidad_asigna')
        id_unidad_asigna = dataSetOperadorSession[0]['id_unidad_asigna']

        Asignacion = WUnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        qryUnidad = Unidad.objects.get(id_unidad=Asignacion[0]['id_unidad'])
        context['unida_medida_combustible'] = qryUnidad.get_unida_medida_combustible_display()
        context['id_unidad_asigna'] = id_unidad_asigna
        # context['cod_acceso'] = cod_acceso
        # context['catalogos'] = 'menu-is-opening menu-open'
        # context['personal'] = 'active'
        return context


# **********************************************************************************************************************
# **********************************************************************************************************************

class UnidadCombustibleDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = UnidadCombustible
    template_name = 'operacion/registro/delete_combustible.html'
    success_url = reverse_lazy('operador:index_operador')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_unidad_combustible=self.kwargs.get( 'id_unidad_combustible' )
        return get_object_or_404( UnidadCombustible, id_unidad_combustible=id_unidad_combustible )

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Ticket Combustible'
        context['entity'] = 'Combustible'
        context['list_url'] = self.success_url

        return context


# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadPeajeCreateView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = UnidadPeaje
    form_class = UnidadPeajeForm
    template_name = 'operacion/registro/create_peaje.html'
    success_url = reverse_lazy('operador:index_operador')
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

        session_key = self.request.session.session_key
        dataSetOperadorSession = OperadorSession.objects.filter(session_key=session_key).values('id_unidad_asigna')
        id_unidad_asigna = dataSetOperadorSession[0]['id_unidad_asigna']
        qryUnidadAsignacion = UnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        id_unidad = qryUnidadAsignacion[0]['id_unidad']
        # Asignacion = WUnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        # qryUnidad = Unidad.objects.get(id_unidad=Asignacion[0]['id_unidad'])
        # context['unida_medida_combustible'] = qryUnidad.get_unida_medida_combustible_display()
        context['id_unidad_asigna'] = id_unidad_asigna
        context['id_unidad'] = id_unidad
        # context['cod_acceso'] = cod_acceso
        # context['catalogos'] = 'menu-is-opening menu-open'
        # context['personal'] = 'active'
        return context


# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadPeajeUpdateView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = UnidadPeaje
    form_class = UnidadPeajeForm
    template_name = 'operacion/registro/create_peaje.html'
    success_url = reverse_lazy('operador:index_operador')
    # permission_required = 'OB. add_personal'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_unidad_peaje=self.kwargs.get( 'id_unidad_peaje' )
        return get_object_or_404( UnidadPeaje , id_unidad_peaje=id_unidad_peaje )

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
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
        context['title'] = 'Editar Ticket Peaje'
        context['entity'] = 'Peaje'
        context['list_url'] = self.success_url
        context['action'] = 'edit'

        session_key = self.request.session.session_key
        dataSetOperadorSession = OperadorSession.objects.filter(session_key=session_key).values('id_unidad_asigna')
        id_unidad_asigna = dataSetOperadorSession[0]['id_unidad_asigna']

        # Asignacion = WUnidadAsignacion.objects.filter(id_unidad_asigna=id_unidad_asigna).values('id_unidad')
        # qryUnidad = Unidad.objects.get(id_unidad=Asignacion[0]['id_unidad'])
        # context['unida_medida_combustible'] = qryUnidad.get_unida_medida_combustible_display()
        context['id_unidad_asigna'] = id_unidad_asigna
        # context['cod_acceso'] = cod_acceso
        # context['catalogos'] = 'menu-is-opening menu-open'
        # context['personal'] = 'active'
        return context


# **********************************************************************************************************************
# **********************************************************************************************************************

class UnidadPeajeDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = UnidadPeaje
    template_name = 'operacion/registro/delete_peaje.html'
    success_url = reverse_lazy('operador:index_operador')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_unidad_peaje=self.kwargs.get( 'id_unidad_peaje' )
        return get_object_or_404( UnidadPeaje, id_unidad_peaje=id_unidad_peaje )

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Ticket PEaje'
        context['entity'] = 'Peaje'
        context['list_url'] = self.success_url

        return context

