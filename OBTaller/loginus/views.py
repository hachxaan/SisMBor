from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView

from OBTaller.models import Unidad, UnidadAsignacion, OperadorSession


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
                return redirect(reverse_lazy('index_operador'))
            else:
                return redirect(reverse_lazy('OBTaller:panel_web'))
        return super().dispatch(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'loginus_oper':
                cod_acceso=request.POST['cod_acceso']
                if (cod_acceso != '' and len(cod_acceso) == 6) :
                    codigo_activo = UnidadAsignacion.objects.filter(cod_acceso=cod_acceso, sit_code=1).exists()
                    if codigo_activo:
                        # form = AuthenticationForm(request.POST)
                        username = 'operador'
                        password = 'acceso.123'
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            if user.is_active:
                                login(request, user)
                                session_key = self.request.session.session_key
                                # qryUnidadAsignacion = UnidadAsignacion.objects.get(cod_acceso=cod_acceso, sit_code=1)
                                dataSetUnidadAsignacion = UnidadAsignacion.objects.get(cod_acceso=cod_acceso, sit_code=1)
                                insOperadorSession = OperadorSession(
                                    session_key=session_key,
                                    # id_unidad_asigna=qryUnidadAsignacion.id_unidad_asigna
                                    id_unidad_asigna=dataSetUnidadAsignacion
                                )
                                insOperadorSession.save()

                                data['id_unidad_asigna'] = dataSetUnidadAsignacion.id_unidad_asigna
                                data['cod_acceso'] = cod_acceso.cod_acceso
                                # return redirect(reverse('indexl', kwargs={"session_auth_hash": session_auth_hash}))
                                # return redirect(reverse('login_operador'))
                        else:
                            return redirect(reverse('login_operador'))
                    # self.request.GET.get('id_unidad_asigna')

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