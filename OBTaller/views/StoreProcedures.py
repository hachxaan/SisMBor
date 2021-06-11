from django.db import connection
from django.http import JsonResponse

from OBTaller.models import Unidad


def StpInsOrden(request):
    placa = request.POST.get('placa')
    peKILOMETRAJE = request.POST.get('kilometraje')
    peCVE_USU_ALTA = request.user.username;
    peNOMBRE_ENTREGA =  request.POST.get('nombre_entrega')
    peTX_REFERENCIA = ''
    psCOD_RESP = 0
    psSTR_RESP = ''
    cursor=connection.cursor()
    try:
        try:
            DataSet = Unidad.objects.filter(placa=placa).values( 'id_unidad')
            peID_UNIDAD = DataSet[0]['id_unidad']
            cursor.callproc('StpInsertaOrden', [peID_UNIDAD, peKILOMETRAJE, peCVE_USU_ALTA, peNOMBRE_ENTREGA, peTX_REFERENCIA, psSTR_RESP])

            # cursor.execute('SELECT @StpInsertaOrden')
            results = cursor.fetchall()
            # results =  psSTR_RESP.getValue()

            for row in results:
                psCOD_RESP = row[0]
                # psSTR_RESP = row[1]

            data = {'psCOD_RESP': psCOD_RESP, 'psSTR_RESP': psSTR_RESP}
        except Exception as e:
            data['error'] = str(e)
    finally:
        cursor.close()
    return JsonResponse(data,  safe=False)

def StpInsBitInventario(request):

    peID_CONCEPTO = request.POST.get('id_concepto')
    peCVE_OPERACION = request.POST.get('cve_operacion')
    peCVE_USUARIO = request.user.username;
    peCANTIDAD = request.POST.get('cantidad')
    pePRECIO_COMPRA = request.POST.get('precio')
    peTX_REFERENCIA = request.POST.get('tx_referencia')
    peFOLIO='0'
    peID_ORDEN_DETALLE=0
    psID_TRANS_INVENTARIO = 0
    psCOD_RESP = 0
    psSTR_RESP = ''
    cursor=connection.cursor()
    try:
        try:

            cursor.callproc('StpInsBitInventario',
                            [peID_CONCEPTO,
                             peCVE_OPERACION,
                             peCVE_USUARIO,
                             peCANTIDAD,
                             pePRECIO_COMPRA,
                             peTX_REFERENCIA,
                             peFOLIO,
                             peID_ORDEN_DETALLE,
                             psID_TRANS_INVENTARIO,
                             psCOD_RESP,
                             psSTR_RESP
                             ])

            # cursor.execute('SELECT @StpInsertaOrden')
            results = cursor.fetchall()
            # results =  psSTR_RESP.getValue()

            for row in results:
                psCOD_RESP = row[0]
                # psSTR_RESP = row[1]

            data = {'psCOD_RESP': psCOD_RESP, 'psSTR_RESP': psSTR_RESP}
        except Exception as e:
            data['error'] = str(e)
    finally:
        cursor.close()
    return JsonResponse(data,  safe=False)
