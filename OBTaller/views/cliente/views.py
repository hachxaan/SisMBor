
# **********************************************************************************************************************
# **********************************************************************************************************************
# C A T A L O G O   -    CLIETE
# **********************************************************************************************************************
# **********************************************************************************************************************
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from OBTaller.forms import ClienteForm
from OBTaller.mixins import ValidatePermissionRequiredMixin
from OBTaller.models import Cliente

# **********************************************************************************************************************
# **********************************************************************************************************************
class ClienteListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Cliente
    template_name ='catalogos/Cliente/list.html'
    # permission_required = 'OBTaller.view_cliente'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cliente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Clientes'
        context['create_url'] = reverse_lazy('OBTaller:cliente_create')
        context['list_url'] = reverse_lazy('OBTaller:cliente_list')
        context['entity'] = 'Categorias'
        context['catalogos']='menu-is-opening menu-open'
        context['clientes']='active'
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
class ClienteCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name ='catalogos/Cliente/create.html'
    success_url = reverse_lazy('OBTaller:cliente_list')
    # permission_required = 'OB. add_cliente'
    url_redirect = success_url

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
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
    
class ClienteUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'catalogos/Cliente/create.html'
    success_url = reverse_lazy('OBTaller:cliente_list')
    # permission_required = 'erp.change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_cliente=self.kwargs.get( 'id_cliente' )
        return get_object_or_404( Cliente , id_cliente=id_cliente )

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
        context['title'] = 'Editar Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

# **********************************************************************************************************************
# **********************************************************************************************************************

class ClienteDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'catalogos/Cliente/delete.html'
    success_url = reverse_lazy('OBTaller:cliente_list')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_cliente=self.kwargs.get( 'id_cliente' )
        return get_object_or_404( Cliente , id_cliente=id_cliente )

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
        context['title'] = 'Eliminar cliente del catálogo'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        return context