import calendar
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField, Avg
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from OBTaller.mixins import ValidaPerfilMixin, ValidaTemp1, ValidaTemp2
from OBTaller.models import VwrPeajeXDia, VwrPeajeXMes, VwrPeajeXAno, VwrPeajeXAnoAcumulado, VwrPeajeXMesAcumulado, \
    VwrPeajeXDiaAcumulado, UnidadPeaje


class DashboardPeajeGraficaView( TemplateView ):
    template_name = 'sensor.html'

    def get(self, request, tipo, id_unidad, filtro):
        data = {}
        try:
            if tipo == 'mensual_promedio':
                data = self.getMensual(id_unidad, filtro, 'prom')
            if tipo == 'mensual_acumulado':
                data = self.getMensual(id_unidad, filtro, 'acum')


            if tipo == 'diario_promedio':
                data = self.getDiario(id_unidad, filtro, 'prom')
            if tipo == 'diario_acumulado':
                data = self.getDiario(id_unidad, filtro, 'acum')

            # else:
                # data['error'] = 'CONFIG[sensor_name]'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def getDiario(self, id_unidad, ano_mes, tipo):
        data = {}
        try:
            ano_mes_split = ano_mes.split('-')
            ano = ano_mes_split[0]
            mes = ano_mes_split[1]
            dia_fin = calendar.monthrange(int(ano), int(mes))[1]
            dias = []
            rdata = []
            for dia in range(1, dia_fin):

                # dia_grap = datetime.strptime(f'{dia}/{mes}/{ano}', '%d/%m/%Y')
                # row.append(dia_grap)
                dias.append(dia)
                if tipo == 'prom':
                    total = UnidadPeaje.objects.filter(fh_ticket__year=ano,
                                                       fh_ticket__month=mes,
                                                       fh_ticket__day=dia,
                                                       id_unidad=id_unidad).aggregate(
                        r=Coalesce(Avg('imp_ticket', output_field=FloatField()), 0.0)).get('r')
                if tipo == 'acum':
                    total = UnidadPeaje.objects.filter(fh_ticket__year=ano,
                                                       fh_ticket__month=mes,
                                                       fh_ticket__day=dia,
                                                       id_unidad=id_unidad).aggregate(
                        r=Coalesce(Sum('imp_ticket', output_field=FloatField()), 0.0)).get('r')


                rdata.append(float(total))

            data['data'] = rdata
            data['dias'] = dias


        except Exception as e:
            data = {}
            data['error'] = str(e)
        return data


    def getMensual(self, id_unidad, ano, tipo):

        data = []
        try:
            for mes in range(1, 13):
                if tipo == 'prom':
                    total = UnidadPeaje.objects.filter(fh_ticket__year=ano, fh_ticket__month=mes, id_unidad=id_unidad).aggregate(r=Coalesce(Avg('imp_ticket', output_field=FloatField()), 0.0  ) ).get('r')
                if tipo == 'acum':
                    total = UnidadPeaje.objects.filter(fh_ticket__year=ano, fh_ticket__month=mes, id_unidad=id_unidad).aggregate(r=Coalesce(Sum('imp_ticket', output_field=FloatField()), 0.0  ) ).get('r')
                data.append(float(total))
        except Exception as e:
            data={}
            data['error']=str(e)
        return data


class DashboardPeajeView(ValidaPerfilMixin, ValidaTemp1, ValidaTemp2, TemplateView):
    template_name = 'dashboard/dashboard_peaje.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'searchdata':
                vista = request.POST['vista']
                if vista == 'diario':
                    data = []
                    id_unidad = request.POST['id_unidad']
                    filtro = request.POST['filtro'].split('-')
                    ano = int(filtro[0])
                    mes = int(filtro[1])
                    for i in VwrPeajeXDia.objects.filter(id_unidad=id_unidad,
                                                         fh_ticket__year=ano,
                                                         fh_ticket__month=mes
                                                         ):
                        item = i.toJSON()
                        data.append(item)
                if vista == 'mensual':
                    data = []
                    id_unidad = request.POST['id_unidad']
                    filtro = request.POST['filtro']
                    for i in VwrPeajeXMes.objects.filter(id_unidad=id_unidad,
                                                         mes__contains=filtro):
                        item = i.toJSON()
                        data.append(item)
                if vista == 'anual':
                    id_unidad = request.POST['id_unidad']
                    if VwrPeajeXAno.objects.filter(id_unidad=id_unidad).exists():
                        data = []
                        for i in VwrPeajeXAno.objects.filter(id_unidad=id_unidad):
                            item = i.toJSON()
                            data.append(item)
                    else:
                        data['msgInfo'] = 'No hay registros para la unidad seleccionada'

                if vista == 'diario_acum':
                    data = []
                    id_unidad = request.POST['id_unidad']
                    filtro = request.POST['filtro'].split('-')
                    ano = int(filtro[0])
                    mes = int(filtro[1])
                    for i in VwrPeajeXDiaAcumulado.objects.filter(id_unidad=id_unidad,
                                                                 fh_ticket__year=ano,
                                                                 fh_ticket__month=mes
                                                                 ):
                        item = i.toJSON()
                        data.append(item)

                if vista == 'mensual_acum':
                    data = []
                    id_unidad = request.POST['id_unidad']
                    for i in VwrPeajeXMesAcumulado.objects.filter(id_unidad=id_unidad):
                        item = i.toJSON()
                        data.append(item)

                if vista == 'anual_acum':
                    id_unidad = request.POST['id_unidad']
                    if VwrPeajeXAnoAcumulado.objects.filter(id_unidad=id_unidad).exists():
                        data = []
                        for i in VwrPeajeXAnoAcumulado.objects.filter(id_unidad=id_unidad):
                            item = i.toJSON()
                            data.append(item)
                    else:
                        data['info'] = 'No hay registros para la unidad seleccionada'

            if action == 'totales':
                data={}
                id_unidad = request.POST['id_unidad']
                promedio = UnidadPeaje.objects.filter(id_unidad=id_unidad).aggregate(Avg('imp_ticket'))
                data['promedio'] = "S./{:,.2f}".format(round(promedio['imp_ticket__avg'], 2))
                promedio = UnidadPeaje.objects.filter(id_unidad=id_unidad).aggregate(Sum('imp_ticket'))
                data['acumulado'] = "S./{:,.2f}".format(round(promedio['imp_ticket__sum'], 2))


            #     Book.objects.all().aggregate(Avg('price'))
        except Exception as e:
            data = {}
            data['error']=str( e )
        print(data)
        return JsonResponse( data, safe=False )
    def get_context_data(self, **kwargs):
        context=super().get_context_data( **kwargs )

        """ D I A R I O - PROMEDIO """
        fieldsColumsDiario = []
        titleFieldsDiario = []
        fieldsColumsDiario.append({"data": 'fh_ticket', 'class':'text-center'})
        fieldsColumsDiario.append({"data": 'promedio', 'class':'text-right'})
        titleFieldsDiario.append({"field_title": 'Fecha', "width": '40'})
        titleFieldsDiario.append({"field_title": 'Promedio', "width": '60'})
        context['fieldsColumsDiario'] = fieldsColumsDiario
        context['titleFieldsDiario'] = titleFieldsDiario

        """ M E N S U A L - PROMEDIO"""
        fieldsColumsMes = []
        titleFieldsMes = []
        fieldsColumsMes.append({"data": 'mes', 'class':'text-center'})
        fieldsColumsMes.append({"data": 'promedio','class':'text-right'})
        titleFieldsMes.append({"field_title": 'Mes', "width": '50'})
        titleFieldsMes.append({"field_title": 'Promedio', "width": '70'})
        context['fieldsColumsMes'] = fieldsColumsMes
        context['titleFieldsMes'] = titleFieldsMes

        """ A N U A L - PROMEDIO"""
        fieldsColumsAno = []
        titleFieldsAno = []
        fieldsColumsAno.append({"data": 'ano', 'class':'text-center'})
        fieldsColumsAno.append({"data": 'promedio', 'class':'text-right'})
        titleFieldsAno.append({"field_title": 'Año', "width": '20'})
        titleFieldsAno.append({"field_title": 'Promedio', "width": '80'})
        context['fieldsColumsAno'] = fieldsColumsAno
        context['titleFieldsAno'] = titleFieldsAno

        """ D I A R I O - ACUMULADO """
        fieldsColumsDiarioAcum = []
        titleFieldsDiarioAcum = []
        fieldsColumsDiarioAcum.append({"data": 'fh_ticket', 'class':'text-center'})
        fieldsColumsDiarioAcum.append({"data": 'acumulado', 'class':'text-right'})
        titleFieldsDiarioAcum.append({"field_title": 'Fecha', "width": '40'})
        titleFieldsDiarioAcum.append({"field_title": 'Acumulado', "width": '60'})
        context['fieldsColumsDiarioAcum'] = fieldsColumsDiarioAcum
        context['titleFieldsDiarioAcum'] = titleFieldsDiarioAcum

        """ M E N S U A L - ACUMULADO """
        fieldsColumsMesAcum = []
        titleFieldsMesAcum = []
        fieldsColumsMesAcum.append({"data": 'mes', 'class':'text-center'})
        fieldsColumsMesAcum.append({"data": 'acumulado','class':'text-right'})
        titleFieldsMesAcum.append({"field_title": 'Mes', "width": '50'})
        titleFieldsMesAcum.append({"field_title": 'Acumulado', "width": '70'})
        context['fieldsColumsMesAcum'] = fieldsColumsMesAcum
        context['titleFieldsMesAcum'] = titleFieldsMesAcum

        """ A N U A L - ACUMULADO """
        fieldsColumsAnoAcum = []
        titleFieldsAnoAcum = []
        fieldsColumsAnoAcum.append({"data": 'ano', 'class':'text-center'})
        fieldsColumsAnoAcum.append({"data": 'acumulado', 'class':'text-right'})
        titleFieldsAnoAcum.append({"field_title": 'Año', "width": '20'})
        titleFieldsAnoAcum.append({"field_title": 'Acumulado', "width": '80'})
        context['fieldsColumsAnoAcum'] = fieldsColumsAnoAcum
        context['titleFieldsAnoAcum'] = titleFieldsAnoAcum


        context['operacion'] = 'menu-is-opening menu-open'
        context['unidad_peaje'] = 'active'

        return context



