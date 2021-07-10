from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView

from OBTaller.models import Unidad

class LoginFromView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['temp'] = 'X'
        return  context

class LoginOperador(TemplateView):
    template_name = 'loginoperador.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            codeacces=request.POST['codeacces']
            if (codeacces != '' and len(codeacces) == 6) :
                data['prueba'] = 'probando'
                # validar que exista el código activo
                # Si es válido:
                    # Login de usuario Operador
                    # Notificar al contexto para sessionStorage.setItem('code_oper', {{}})
            else:
                data['error'] = 'Verifica el código de 6 digitos'
        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )