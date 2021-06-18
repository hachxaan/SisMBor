
import os
import datetime as dt
from datetime import timedelta
from distutils import debug


from django.contrib.gis.db.backends import mysql
from django.db.models.functions import datetime
from django.utils.datetime_safe import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appMainSite.settings')

from appMainSite.wsgi import *

from django.db import connection
from django.http import JsonResponse
from django.test import TestCase
from OBTaller.models import *
# Create your tests here.


# dataSet = Concepto.objects.filter( id_concepto=1 ).values('precio_compra', 'precio_venta');
# print(dataSet)
# print(dataSet[0]['precio_compra'])


kilometraje = 74900
if (kilometraje < 25000):
    kilometraje = 25000
else:
    RetVecesVal = round(kilometraje/25000)
    kilometraje = RetVecesVal * 25000


print({"kilometraje":kilometraje})


vFieldFilter = {
    '{0}'.format('m'+str(kilometraje)): '1'
}

dataSet = WListaMantenimiento.objects.filter(**vFieldFilter).values('id_concepto')
for i in WListaMantenimiento.objects.filter(**vFieldFilter):
    print(i.id_concepto)



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