
# **********************************************************************************************************************
# **********************************************************************************************************************
# C A T A L O G O   -    CLIETE
# **********************************************************************************************************************
# **********************************************************************************************************************
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from OBTaller.forms import UnidadForm
from OBTaller.mixins import ValidatePermissionRequiredMixin
from OBTaller.models import Unidad, WbUnidad, WbUnidadNeu


# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Unidad
    template_name ='catalogos/Unidad/list.html'
    # permission_required = 'OBTaller.view_unidad'

    @method_decorator(csrf_exempt)
    # @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        # self.object=self.get_object()
        return super().dispatch( request, *args, **kwargs )

    def get_object(self):
        id_unidad=self.kwargs.get( 'id_unidad' )
        return get_object_or_404( Unidad , id_unidad=id_unidad )

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Unidad.objects.all():
                    data.append(i.toJSON())
            else:
                if action == 'searchdata_buscador':
                    data=[]
                    b_todas = request.POST['b_todas']
                    if (b_todas == 'b_todas'):
                        for i in WbUnidadNeu.objects.all():
                            data.append(i.toJSON())
                    else:
                        for i in WbUnidad.objects.all():
                            data.append(i.toJSON())
                else:
                    data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Unidades'
        context['create_url'] = reverse_lazy('OBTaller:unidad_create')
        context['list_url'] = reverse_lazy('OBTaller:unidad_list')
        context['entity'] = 'Categorias'
        context['catalogos']='menu-is-opening menu-open'
        context['unidades']='active'
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
class UnidadCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Unidad
    form_class = UnidadForm
    template_name ='catalogos/Unidad/create.html'
    success_url = reverse_lazy('OBTaller:unidad_list')
    # permission_required = 'OB. add_cliente'


    url_redirect=success_url

    @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Unidad'
        context['entity'] = 'Unidades'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['catalogos']='menu-is-opening menu-open'
        context['unidades']='active'
        context['esorden']= 'dsadsadas'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
                data['placa'] = form.data['placa']
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


# **********************************************************************************************************************
# **********************************************************************************************************************
    
class UnidadUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'catalogos/Unidad/create.html'
    success_url = reverse_lazy('OBTaller:unidad_list')
    # permission_required = 'erp.change_category'
    url_redirect = success_url

    @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch( request, *args, **kwargs )

    def get_object(self):
        id_unidad=self.kwargs.get( 'id_unidad' )
        return get_object_or_404( Unidad , id_unidad=id_unidad )

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
        context['title'] = 'Editar Unidad'
        context['entity'] = 'Unidades'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['catalogos']='menu-is-opening menu-open'
        context['unidades']='active'
        return context

# **********************************************************************************************************************
# **********************************************************************************************************************

class UnidadDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Unidad
    template_name = 'catalogos/Unidad/delete.html'
    success_url = reverse_lazy('OBTaller:unidad_list')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_unidad=self.kwargs.get( 'id_unidad' )
        return get_object_or_404( Unidad , id_unidad=id_unidad )

    @method_decorator( login_required )
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().dispatch( request, *args, **kwargs )

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar unidad del catálogo'
        context['entity'] = 'Unidades'
        context['list_url'] = self.success_url
        context['catalogos']='menu-is-opening menu-open'
        context['unidades']='active'
        return context