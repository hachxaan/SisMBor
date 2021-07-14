from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from OBTaller.models import Parametros, Reportes
from appMainSite.const import urlsOperador


class StatusMenu:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        urlCurrent = request.path
        is_static = urlCurrent.find('static') >= 0
        # if not is_static:
        #     if not request.user.is_authenticated:
        #         return response
        #     else:
        #         es_operador = request.user.es_operador
        #         if es_operador:
        #             if response.url != '/registro/':
        #                 return HttpResponseRedirect(reverse('index_operador'))
        #             else:
        #                 return response



        #         else:
        #             if urlCurrent in urlsOperador:
        #                 if not request.user.is_authenticated:
        #                     return HttpResponseRedirect(reverse('OBTaller:login'))
        #                 else:
        #                     return HttpResponseRedirect(reverse('OBTaller:panel-operacion'))
        #             else:
        #                 return response
        #
        #
        #
        #         else:
        #             return response


        return response


    # def process_request(self, request):
    #     redirect('/inventario_neumaticos/')

    def process_template_response(self, _, response):
        Parametro = Parametros.objects.get(cve_parametro='status_menu')
        response.context_data['status_menu'] = Parametro.valor
        # # if not self.request.user.is_staff:
        # algo = False
        # is_staff = True
        # urlCurrent = response.template_name[0]
        # urlOperador = reverse('OBTaller:inventario_neumaticos_list')
        # is_urlOperador = urlCurrent.find( urlOperador[1:50] ) >= 0
        # if is_staff and not is_urlOperador:
        #     return HttpResponseRedirect(reverse('login_operador'))
                # redirect(reverse("OBTaller:inventario_neumaticos_list"))
        #     # return reverse('OBTaller:inventario_neumaticos_list')
        #     return HttpResponseRedirect(reverse("OBTaller:inventario_neumaticos_list"))
                # HttpResponseRedirect(urlOperador)
        return response


class MenuReportes:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, _, response):
        datasetReportes = Reportes.objects.filter(activo='1')
        response.context_data['datasetReportes'] = datasetReportes
        return response
