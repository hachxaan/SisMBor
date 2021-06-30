import json
import os
import datetime as dt
from datetime import timedelta
from distutils import debug


from django.contrib.gis.db.backends import mysql

from django.db import connection
from django.db.models.functions import datetime
from django.utils.datetime_safe import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appMainSite.settings')

from appMainSite.wsgi import *


from django.http import JsonResponse
from django.test import TestCase
from OBTaller.models import *
# Create your tests here.


cursor = connection.cursor()
cursor.execute('''SELECT * FROM vwr_servicio_unidad''')
resp = cursor.fetchall()
fieldsColums = []
titleFields = []
DESC = cursor.description
for field in DESC:
    fieldsColums.append({"data": field[0].lower()})
    titleFields.append({"field_title": field[0]})



# for row in resp:
#     print(row)
#     jsonObj = json.dumps(row)
#     print(jsonObj)
#
# print(resp)



################################################################################
################################################################################
# STORE PROCEDURE RESPUESTA
#
# placa = 'ABCD-1234'
# peKILOMETRAJE = 100
# peCVE_USU_ALTA = 'DEBUG'
# peNOMBRE_ENTREGA =  'pruebas...'
# peTX_REFERENCIA = ''
# psCOD_RESP = 0
# psSTR_RESP = 'old'
# # cursor=connection.cursor()
#
# try:
#     # cursor = connections["default"].cursor()
#     cursor =  connection.cursor()
#     try:
#         data = {}
#         kilometraje_int = int(peKILOMETRAJE)
#         if (kilometraje_int < 25000):
#             peKILOMETRAJE_PQ = 25000
#         else:
#             RetVecesVal = round(kilometraje_int / 25000)
#             peKILOMETRAJE_PQ = RetVecesVal * 25000
#
#
#         DataSet = Unidad.objects.filter(placa=placa).values( 'id_unidad')
#         peID_UNIDAD = DataSet[0]['id_unidad']
#
#         parameters = [peID_UNIDAD, peKILOMETRAJE, peKILOMETRAJE_PQ, peCVE_USU_ALTA, peNOMBRE_ENTREGA, peTX_REFERENCIA, psCOD_RESP, psSTR_RESP]
#         results = cursor.callproc('StpInsertaOrden', parameters)
#         cursor.execute('SELECT @_StpInsertaOrden_6, @_StpInsertaOrden_7')
#         resp = cursor.fetchall()
#         psCOD_RESP = resp[0][0]
#         psSTR_RESP = resp[0][1]
#
#         data = {'psCOD_RESP': psCOD_RESP, 'psSTR_RESP': psSTR_RESP}
#         # print(data)
#     except Exception as e:
#         data['error'] = str(e)
# finally:
#     cursor.close()

























#
#
# kilometraje = 74900
# if (kilometraje < 25000):
#     kilometraje = 25000
# else:
#     RetVecesVal = round(kilometraje/25000)
#     kilometraje = RetVecesVal * 25000
#
#
# print({"kilometraje":kilometraje})
#
#
# vFieldFilter = {
#     '{0}'.format('m'+str(kilometraje)): '1'
# }
#
# dataSet = WListaMantenimiento.objects.filter(**vFieldFilter).values('id_concepto')
# for i in WListaMantenimiento.objects.filter(**vFieldFilter):
#     print(i.id_concepto)



#
# folio = 70
# peCANTIDAD = 1
# id_concepto = 5
# id_personal = 0
# peNO_SERIE = "A0012241045"
# peTX_REFERENCIA = 'una referencia bla ble bli'
# peCVE_USUARIO = 'TESTER'
#
#
# cursor=connection.cursor()
# psSTR_RESP = 'psSTR_RESP'
# try:
#     data ={}
#     try:
#         cursor.callproc('StpInsOrdenDetalle', [folio, peCANTIDAD, id_concepto, id_personal, peNO_SERIE, peTX_REFERENCIA, peCVE_USUARIO,psSTR_RESP])
#
#         results=cursor.fetchall()
#
#         for row in results:
#             psSTR_RESP=row[0]
#
#
#
#         cursor.execute('SELECT @psSTR_RESP')
#         results = cursor.fetchone()
#         # print({"results":results})
#         # results =  psSTR_RESP.getValue()
#         dato = 'test9000'
#         # for result in cursor.stored_results():
#         #     print(result.fetchall())
#
#
#         data = {'dato': dato}
#     except Exception as e:
#         data['error'] = str(e)
#         print(data)
# finally:
#     cursor.close()
# print( JsonResponse(data,  safe=False) )

# IN peFOLIO int,
# IN peCANTIDAD int,
# IN peID_CONCEPTO int,
# IN peID_PERSONAL INT,
# IN peNO_SERIE varchar(512),
# IN peTX_REFERENCIA varchar(1024),
# IN peCVE_USUARIO varchar(45),
# OUT psSTR_RESP  TEXT