
# **********************************************************************************************************************
# **********************************************************************************************************************
# C A T A L O G O   -    MANO DE OBRA
# **********************************************************************************************************************
# **********************************************************************************************************************
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from appMainSite import const
from OBTaller.forms import ManobraForm
from OBTaller.mixins import ValidatePermissionRequiredMixin
from OBTaller.models import WConceptosMain, Concepto


# **********************************************************************************************************************
# **********************************************************************************************************************
from appMainSite import settings
from appMainSite.const import TCONCEPTO_MANOBRA


class ManobraListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = WConceptosMain
    template_name ='catalogos/Manobra/list.html'
    # permission_required = 'OBTaller.view_unidad'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_concepto=self.kwargs.get( 'id_concepto' )
        return get_object_or_404( WConceptosMain , id_concepto=id_concepto )

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in WConceptosMain.objects.filter(id_tipo_concepto= const.TCONCEPTO_MANOBRA):
                    data.append(i.toJSON())
            else:
                data = {}
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Catálogos / Mano de Obra'
        context['create_url'] = reverse_lazy('OBTaller:manobra_create')
        context['list_url'] = reverse_lazy('OBTaller:manobra_list')
        context['entity'] = 'Mano de Obras'
        context['catalogos']='menu-is-opening menu-open'
        context['manobra']='active'
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
class ManobraCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Concepto
    form_class = ManobraForm
    template_name ='catalogos/Manobra/create.html'
    success_url = reverse_lazy('OBTaller:manobra_list')
    # permission_required = 'OB. add_unidad'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_concepto=self.kwargs.get( 'id_concepto' )
        return get_object_or_404( Concepto , id_concepto=id_concepto )

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
        context['title'] = 'Creación Mano de Obra'
        context['entity'] = 'Mano de obra'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['catalogos']='menu-is-opening menu-open'
        context['manobra']='active'
        context['id_tipo_concepto']=TCONCEPTO_MANOBRA

        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
    
class ManobraUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Concepto
    form_class = ManobraForm
    template_name = 'catalogos/Manobra/create.html'
    success_url = reverse_lazy('OBTaller:manobra_list')
    # permission_required = 'erp.change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_concepto=self.kwargs.get( 'id_concepto' )
        return get_object_or_404( Concepto , id_concepto=id_concepto )

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
        context['title'] = 'Editar Mano de obra'
        context['entity'] = 'Mano de obra'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['catalogos']='menu-is-opening menu-open'
        context['id_tipo_concepto']=TCONCEPTO_MANOBRA
        context['manobra']='active'
        return context

# **********************************************************************************************************************
# **********************************************************************************************************************

class ManobraDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Concepto
    template_name = 'catalogos/Manobra/delete.html'
    success_url = reverse_lazy('OBTaller:manobra_list')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_concepto=self.kwargs.get( 'id_concepto' )
        return get_object_or_404( Concepto, id_concepto=id_concepto )

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
        context['title'] = 'Eliminar Mano de Obra del catálogo'
        context['entity'] = 'Unidades'
        context['list_url'] = self.success_url
        context['catalogos']='menu-is-opening menu-open'
        context['manobra']='active'
        return context