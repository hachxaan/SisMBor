
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
import datetime as dt

from OBTaller.forms import PersonalForm
from OBTaller.mixins import ValidatePermissionRequiredMixin
from OBTaller.models import Personal

# **********************************************************************************************************************
# **********************************************************************************************************************
class PersonalListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Personal
    template_name ='catalogos/Personal/list.html'
    # permission_required = 'OBTaller.view_personal'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Personal.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Personal'
        context['create_url'] = reverse_lazy('OBTaller:personal_create')
        context['list_url'] = reverse_lazy('OBTaller:personal_list')
        context['entity'] = 'Peronal en taller'
        context['catalogos']='menu-is-opening menu-open'
        context['personal']='active'
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
class PersonalCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Personal
    form_class = PersonalForm
    template_name ='catalogos/Personal/create.html'
    success_url = reverse_lazy('OBTaller:personal_list')
    # permission_required = 'OB. add_personal'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.instance.cve_usu_alta = request.user.username
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Personal'
        context['entity'] = 'Persona'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
# **********************************************************************************************************************
# **********************************************************************************************************************
    
class PersonalUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'catalogos/Personal/create.html'
    success_url = reverse_lazy('OBTaller:personal_list')
    # permission_required = 'erp.change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_personal=self.kwargs.get( 'id_personal' )
        return get_object_or_404( Personal , id_personal=id_personal )

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
        context['title'] = 'Editar Personal'
        context['entity'] = 'Persona'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

# **********************************************************************************************************************
# **********************************************************************************************************************

class PersonalDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Personal
    template_name = 'catalogos/Personal/delete.html'
    success_url = reverse_lazy('OBTaller:personal_list')
    # permission_required = 'erp.delete_category'
    url_redirect = success_url

    def get_object(self):
        id_personal=self.kwargs.get( 'id_personal' )
        return get_object_or_404( Personal, id_personal=id_personal )

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
        context['title'] = 'Eliminar personal del catálogo'
        context['entity'] = 'Persona'
        context['list_url'] = self.success_url
        return context