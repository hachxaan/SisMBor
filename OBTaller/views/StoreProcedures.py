from django.db import connection
from django.http import JsonResponse

from OBTaller.models import Unidad


def StpInsOrden(request):
    placa = request.POST.get('placa')
    kilometraje = request.POST.get('kilometraje')
    username = request.user.username
    nombre_entrega = request.POST.get('nombre_entrega')
    tx_referencia = ''
    pscod_resp = 0
    ps_strresp = ''
    cursor = connection.cursor()
    try:
        try:
            kilometraje_int = int(kilometraje)
            if kilometraje_int < 25000:
                kilometraje_pq = 25000
            else:
                retvecesval = round(kilometraje_int / 25000)
                kilometraje_pq = retvecesval * 25000

            dataset = Unidad.objects.filter(placa=placa).values('id_unidad')
            id_unidad = dataset[0]['id_unidad']
            cursor.callproc('StpInsertaOrden', [id_unidad, kilometraje, kilometraje_pq, username, nombre_entrega,
                            tx_referencia, ps_strresp])

            # cursor.execute('SELECT @StpInsertaOrden')
            results = cursor.fetchall()
            # results =  psSTR_RESP.getValue()

            for row in results:
                ps_strresp = row[0]
                # psSTR_RESP = row[1]

            data = {'psCOD_RESP': pscod_resp, 'psSTR_RESP': ps_strresp}
        except Exception as e:
            data['error'] = str(e)
    finally:
        cursor.close()
    return JsonResponse(data,  safe=False)


def StpInsBitInventario(request):

    id_concepto = request.POST.get('id_concepto')
    cve_operacion = request.POST.get('cve_operacion')
    username = request.user.username
    cantidad = request.POST.get('cantidad')
    precio = request.POST.get('precio')
    tx_referencia = request.POST.get('tx_referencia')
    folio = '0'
    id_orden_detalle = 0
    id_trans_inventario = 0
    cod_resp = 0
    str_resp = ''
    cursor = connection.cursor()
    try:
        try:

            cursor.callproc('StpInsBitInventario',
                            [id_concepto,
                             cve_operacion,
                             username,
                             cantidad,
                             precio,
                             tx_referencia,
                             folio,
                             id_orden_detalle,
                             id_trans_inventario,
                             cod_resp,
                             str_resp
                             ])

            # cursor.execute('SELECT @StpInsertaOrden')
            results = cursor.fetchall()
            # results =  psSTR_RESP.getValue()

            for row in results:
                cod_resp = row[0]
                # psSTR_RESP = row[1]

            data = {'psCOD_RESP': cod_resp, 'psSTR_RESP': str_resp}
        except Exception as e:
            data['error'] = str(e)
    finally:
        cursor.close()
    return JsonResponse(data,  safe=False)
