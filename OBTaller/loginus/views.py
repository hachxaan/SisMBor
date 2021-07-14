from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView

from OBTaller.models import Unidad, UnidadAsignacion


class LoginFromView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     password = request.POST['password']
    #     username = request.POST['username']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['temp'] = 'X'
        return  context

class LoginOperador(TemplateView):
    template_name = 'loginoperador.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.es_operador:
                return redirect(reverse('index_operador'))
            else:
                return redirect(reverse('OBTaller:panel_web'))
        return super().dispatch(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'loginus_oper':
                codeacces=request.POST['codeacces']
                if (codeacces != '' and len(codeacces) == 6) :

                    codigo_activo = UnidadAsignacion.objects.filter(cod_acceso=codeacces, sit_code=1).exists()
                    if codigo_activo:
                        # form = AuthenticationForm(request.POST)
                        username = 'operador'
                        password = 'acceso.123'
                        user = authenticate(username=username, password=password)
                        if user:
                            if user.is_active:
                                login(request, user)
                                return redirect(reverse('index_operador'))
                        else:
                            return redirect(reverse('login_operador'))


                    else:

                        data['error'] = 'La clave ya no está activa'
                        return render(request, self.template_name, data)

                    # validar que exista el código activo
                    # Si es válido:
                        # Login de usuario Operador
                        # Notificar al contexto para sessionStorage.setItem('code_oper', {{}})
                else:
                    data['error'] = 'La clave debe ser de 6 digitos'
        except Exception as e:
            data = {}
            data['error']=str( e )
        return JsonResponse( data, safe=False )