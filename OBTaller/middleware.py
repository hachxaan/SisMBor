from OBTaller.models import Parametros


class StatusMenu:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, _, response):
        Parametro = Parametros.objects.get(cve_parametro='status_menu')
        response.context_data['status_menu'] = Parametro.valor
        return response
