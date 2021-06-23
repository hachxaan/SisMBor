
# **********************************************************************************************************************
# **********************************************************************************************************************
# C A T A L O G O   -    INVENTARIO MEUMATICOS
# **********************************************************************************************************************
# **********************************************************************************************************************
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from OBTaller.forms import InventarioNeumaticosForm, InventarioNeumaticosFormEdit
from appMainSite import const
from OBTaller.mixins import ValidatePermissionRequiredMixin
from OBTaller.models import WConceptosMain, Concepto, WsTipoSalida

# **********************************************************************************************************************
# **********************************************************************************************************************



class InventarioNeumaticosView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = WConceptosMain
    template_name ='inventario_neumaticos/list.html'
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
                for i in WConceptosMain.objects.filter(id_tipo_concepto= const.TCONCEPTO_NEUMATICOS):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Generales
        context['title'] = 'inventario_neumaticos/Neumaticos'
        context['create_url'] = reverse_lazy('OBTaller:inventario_neumaticos_create')
        context['list_url'] = reverse_lazy('OBTaller:inventario_neumaticos_list')
        context['entity'] = 'Neumaticos'

        context['inventarios']='menu-is-opening menu-open'
        context['neumaticos']='active'
        # Invenrtario
        context['label_nuevo'] = 'Agregar nuevo neumático'
        context['id_tipo_concepto'] = const.TCONCEPTO_NEUMATICOS
        data=[]
        for i in WsTipoSalida.objects.all():
            data.append( i.toJSON() )
        context['tipos_salida'] = data
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
class InventarioNeumaticosCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Concepto
    form_class = InventarioNeumaticosForm
    template_name ='inventario_neumaticos/create.html'
    success_url = reverse_lazy('OBTaller:inventario_neumaticos_list')
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
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inventario / Neumáticos'
        context['entity'] = 'Neumáticos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['inventarios'] = 'menu-is-opening menu-open'
        context['neumaticos']='active'
        context['id_tipo_concepto'] = const.TCONCEPTO_NEUMATICOS
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
    
class InventarioNeumaticosUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Concepto
    form_class = InventarioNeumaticosFormEdit
    template_name = 'inventario_neumaticos/create.html'
    success_url = reverse_lazy('OBTaller:inventario_neumaticos_list')
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
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Repusto'
        context['entity'] = 'Repuesto   '
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['catalogos']='menu-is-opening menu-open'
        context['inventarios'] = 'menu-is-opening menu-open'
        context['neumaticos']='active'
        context['id_tipo_concepto']= const.TCONCEPTO_NEUMATICOS
        context['edit_stock']='ready'
        return context

# **********************************************************************************************************************
# **********************************************************************************************************************

class InventarioNeumaticosDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Concepto
    template_name = 'inventario_neumaticos/delete.html'
    success_url = reverse_lazy('OBTaller:inventario_neumaticos_list')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_concepto=self.kwargs.get( 'id_concepto' )
        return get_object_or_404( Concepto , id_concepto=id_concepto )

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Neumatico'
        context['entity'] = 'Neumaticos'
        context['list_url'] = self.success_url
        context['inventarios']='menu-is-opening menu-open'
        context['neumaticos']='active'
        return context