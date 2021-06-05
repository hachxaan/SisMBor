from django.db import connection
from django.http import JsonResponse


def StpInsOrden(request):
    peID_UNIDAD = request.POST.get('id_unidad')
    peKILOMETRAJE = request.POST.get('kilometraje')
    peCVE_USU_ALTA = request.user.username;
    peNOMBRE_ENTREGA =  request.POST.get('nombre_entrega')
    peTX_REFERENCIA = ''
    cursor=connection.cursor()
    psCOD_RESP = 0
    psSTR_RESP = ''
    try:
        try:
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
