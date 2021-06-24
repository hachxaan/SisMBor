# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# import datetime as dt


from django.contrib.auth.models import User
from django.db import models
from django.forms import model_to_dict
from django.utils import timezone


class BitInventario(models.Model):
    id_trans_inventario = models.AutoField(db_column='ID_TRANS_INVENTARIO', primary_key=True)  
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32)  
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=8)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')  
    cve_usuario = models.CharField(db_column='CVE_USUARIO', max_length=8, blank=True, null=True)  
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  
    existencia = models.IntegerField(db_column='EXISTENCIA', blank=True, null=True)  
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2)  
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2)  
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=1024, blank=True, null=True)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'bit_inventario'


class BitVenta(models.Model):
    id_trans_venta = models.AutoField(db_column='ID_TRANS_VENTA', primary_key=True)  
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32)  
    imp_trans = models.DecimalField(db_column='IMP_TRANS', max_digits=18, decimal_places=2)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')  
    cve_usuario = models.CharField(db_column='CVE_USUARIO', max_length=8, blank=True, null=True)  
    id_personal = models.IntegerField(db_column='ID_PERSONAL', blank=True, null=True)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=128, blank=True, null=True)  
    id_trans_inventario = models.IntegerField(db_column='ID_TRANS_INVENTARIO', blank=True, null=True)  
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=8, blank=True, null=True)  
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  
    fuerzasalida = models.CharField(db_column='FUERZASALIDA', max_length=1, blank=True, null=True)  
    status = models.IntegerField(db_column='STATUS')  
    tipo_venta = models.CharField(db_column='TIPO_VENTA', max_length=16, blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'bit_venta'


class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='ID_CLIENTE', primary_key=True)  
    rup = models.CharField( verbose_name='R.U.P.', db_column='RUP', max_length=11, blank=True, null=True)  
    nombre_empresa = models.CharField(db_column='NOMBRE_EMPRESA', max_length=64, blank=True, null=True)  
    telefono_contacto = models.CharField(db_column='TELEFONO_CONTACTO', max_length=32, blank=True, null=True)  
    celular_contacto = models.CharField(db_column='CELULAR_CONTACTO', max_length=32, blank=True, null=True)  
    correo_electronico = models.CharField(db_column='CORREO_ELECTRONICO', max_length=32, blank=True, null=True)  
    direccion = models.CharField(db_column='DIRECCION', max_length=128, blank=True, null=True)  
    nombre = models.CharField(db_column='NOMBRE', unique=True, max_length=40, blank=True, null=True)  
    apellido = models.CharField(db_column='APELLIDO', max_length=40, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')


    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        managed = False
        db_table = 'cliente'




class ConceptoCategoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO')  
    desc_categoria = models.CharField(db_column='DESC_CATEGORIA', max_length=32)  

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_categoria
    class Meta:
        managed = False
        db_table = 'concepto_categoria'




class TipoServicio(models.Model):
    id_tipo_servicio = models.AutoField(db_column='ID_TIPO_SERVICIO', primary_key=True)  
    desc_tipo_servicio = models.CharField(db_column='DESC_TIPO_SERVICIO', max_length=45, blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.desc_tipo_servicio

    class Meta:
        managed = False
        db_table = 'tipo_servicio'

class ConceptoTipoMarca(models.Model):
    id_marca = models.AutoField(db_column='ID_MARCA', primary_key=True)
    desc_marca = models.CharField(db_column='DESC_MARCA', unique=True, max_length=64)
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO', blank=True, null=True)

    def __str__(self):
        return self.desc_marca

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'concepto_tipo_marca'


class PeriodoKm(models.Model):
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', primary_key=True)
    kilometraje = models.IntegerField(db_column='KILOMETRAJE')
    desc_periodo_km = models.CharField(db_column='DESC_PERIODO_KM', max_length=16, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.desc_periodo_km

    class Meta:
        managed = False
        db_table = 'periodo_km'



class UnidadMedida(models.Model):
    id_unidad_medida = models.AutoField(db_column='ID_UNIDAD_MEDIDA', primary_key=True)
    desc_unidad_medida = models.CharField(db_column='DESC_UNIDAD_MEDIDA', max_length=45, blank=True, null=True)
    abreb_unidad_medida = models.CharField(db_column='ABREB_UNIDAD_MEDIDA', max_length=45, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_unidad_medida + ' (' + self.abreb_unidad_medida +')'
    class Meta:
        managed = False
        db_table = 'unidad_medida'



class Concepto(models.Model):
    id_concepto=models.IntegerField( db_column='ID_CONCEPTO', primary_key=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', unique=True,max_length=32)  
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', unique=True, max_length=128)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO')  
    id_categoria = models.ForeignKey( ConceptoCategoria, models.DO_NOTHING, db_column='ID_CATEGORIA')  
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2)  
    id_unidad_medida = models.ForeignKey(UnidadMedida, models.DO_NOTHING,db_column='ID_UNIDAD_MEDIDA', blank=True, null=True)
    id_periodo_km = models.ForeignKey( PeriodoKm, models.DO_NOTHING, db_column='ID_PERIODO_KM', blank=True, null=True)  
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)  
    vida_util_hr = models.IntegerField(db_column='VIDA_UTIL_HR', blank=True, null=True)  
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=18, decimal_places=2, blank=True, null=True)  
    id_marca = models.ForeignKey(ConceptoTipoMarca, models.DO_NOTHING, db_column='ID_MARCA', blank=True, null=True)
    hora_hombre = models.DecimalField(db_column='HORA_HOMBRE', max_digits=9, decimal_places=2, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    no_serie = models.CharField(db_column='NO_SERIE', max_length=128, blank=True, null=True)  
    b_numero_serie = models.BooleanField(db_column='B_NUMERO_SERIE')
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2)  
    id_tipo_servicio = models.ForeignKey( TipoServicio, models.DO_NOTHING, db_column='ID_TIPO_SERVICIO', blank=True, null=True)
    b_agrega_conceptos = models.BooleanField(db_column='B_AGREGA_CONCEPTOS')
    stock=models.IntegerField( db_column='STOCK' )
    b_nserie_obligatorio=models.BooleanField( db_column='B_NSERIE_OBLIGATORIO' )

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_concepto
    class Meta:
        managed = False
        db_table = 'concepto'



class ConceptoKilometraje(models.Model):
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', primary_key=True, max_length=32)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE')  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'concepto_kilometraje'


class ConceptoTipo(models.Model):
    id_tipo_concepto = models.AutoField(db_column='ID_TIPO_CONCEPTO', primary_key=True)  
    desc_tipo_concepto = models.CharField(db_column='DESC_TIPO_CONCEPTO', max_length=32)  
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=16)  
    b_aplica_comision = models.CharField(db_column='B_APLICA_COMISION', max_length=1)  
    categoria = models.IntegerField(db_column='CATEGORIA', blank=True, null=True)  
    activo = models.IntegerField(db_column='ACTIVO')  
    b_personal = models.CharField(db_column='B_PERSONAL', max_length=1)  

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_tipo_concepto
    class Meta:
        managed = False
        db_table = 'concepto_tipo'





class Cuenta(models.Model):
    id_cuenta = models.AutoField(db_column='ID_CUENTA', primary_key=True)  
    folio = models.ForeignKey('Orden', models.DO_NOTHING, db_column='FOLIO')  
    descuento_cuenta = models.DecimalField(db_column='DESCUENTO_CUENTA', max_digits=18, decimal_places=4)  
    imp_total = models.DecimalField(db_column='IMP_TOTAL', max_digits=18, decimal_places=2)  
    tipo_pago = models.CharField(db_column='TIPO_PAGO', max_length=16, blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'cuenta'




class Operacion(models.Model):
    cve_operacion = models.CharField(db_column='CVE_OPERACION', primary_key=True, max_length=8)  
    desc_operacion = models.CharField(db_column='DESC_OPERACION', max_length=128, blank=True, null=True)  
    af_total_cuenta = models.CharField(db_column='AF_TOTAL_CUENTA', max_length=1, blank=True, null=True)  
    af_inventario = models.CharField(db_column='AF_INVENTARIO', max_length=1, blank=True, null=True)  
    gpo_operacion = models.CharField(db_column='GPO_OPERACION', max_length=16, blank=True, null=True)  
    af_caja = models.CharField(db_column='AF_CAJA', max_length=1, blank=True, null=True)  
    b_efectivo = models.CharField(db_column='B_EFECTIVO', max_length=1)  
    activo = models.IntegerField(db_column='ACTIVO')  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'operacion'


class Orden(models.Model):
    folio = models.AutoField(db_column='FOLIO', primary_key=True)  
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    kilometraje_pq = models.IntegerField(db_column='KILOMETRAJE_PQ', blank=True, null=True)
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_alta = models.DateTimeField(db_column='FH_ALTA')  
    fh_inicio = models.DateTimeField(db_column='FH_INICIO', blank=True, null=True)  
    fh_salida = models.DateTimeField(db_column='FH_SALIDA', blank=True, null=True)  
    nombre_entrega = models.CharField(db_column='NOMBRE_ENTREGA', max_length=128, blank=True, null=True)  
    status = models.IntegerField(db_column='STATUS')  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'orden'

class OrdenDetalle(models.Model):
    id_orden_detalle=models.IntegerField( db_column='ID_ORDEN_DETALLE', primary_key=True )
    folio = models.IntegerField(db_column='FOLIO')  # Field name made lowercase.
    consecutivo = models.IntegerField(db_column='CONSECUTIVO')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO')  # Field name made lowercase.
    id_personal=models.IntegerField( db_column='ID_PERSONAL' )  # Field name made lowercase.
    no_serie = models.CharField(db_column='NO_SERIE', max_length=512, blank=True, null=True)  # Field name made lowercase.
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=10, decimal_places=2)  # Field name made lowercase.
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')  # Field name made lowercase.
    sit_code = models.CharField(db_column='SIT_CODE', max_length=45)  # Field name made lowercase.


    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'orden_detalle'
        unique_together = (('folio', 'consecutivo'),)

class OrdenReferencias(models.Model):
    id_orden_referencia = models.AutoField(db_column='ID_ORDEN_REFERENCIA', primary_key=True)  
    folio = models.IntegerField(db_column='FOLIO')  
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=512, blank=True, null=True)  
    cve_usuario_alta = models.CharField(db_column='CVE_USUARIO_ALTA', max_length=45, blank=True, null=True)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'orden_referencias'



class Personal(models.Model):
    id_personal = models.AutoField(db_column='ID_PERSONAL', primary_key=True)  
    nombre = models.CharField(db_column='NOMBRE', unique=True, max_length=40, blank=True, null=True)  
    apellido = models.CharField(db_column='APELLIDO', max_length=40, blank=True, null=True)  
    # cve_usu_alta = models.ForeignKey(User, null=True, blank=True)
    cve_usu_alta = models.CharField(User, db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO',  default=timezone.now, blank=True, null=True)
    # , auto_now_add=True

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'personal'

class Unidad(models.Model):
    id_unidad = models.AutoField(db_column='ID_UNIDAD', primary_key=True)  
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ID_CLIENTE')  
    placa = models.CharField(db_column='PLACA', unique=True, max_length=16)  
    marca = models.CharField(db_column='MARCA', max_length=32, blank=True, null=True)  
    modelo = models.CharField(db_column='MODELO', max_length=32, blank=True, null=True)  
    motor = models.CharField(db_column='MOTOR', max_length=64, blank=True, null=True)  
    chasis = models.CharField(db_column='CHASIS', max_length=64, blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item



    class Meta:
        managed = False
        db_table = 'unidad'




class Usuario(models.Model):
    cve_usuario = models.CharField(db_column='CVE_USUARIO', primary_key=True, max_length=8)  
    nombre = models.CharField(db_column='NOMBRE', max_length=64, blank=True, null=True)  
    passw = models.CharField(db_column='PASSW', max_length=64, blank=True, null=True)  
    mail = models.CharField(db_column='MAIL', max_length=64, blank=True, null=True)  
    sit_usuario = models.CharField(db_column='SIT_USUARIO', max_length=5)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')  
    b_system = models.CharField(db_column='B_SYSTEM', max_length=5)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'usuario'


# **********************************************************************************************************************
#         vistas
# **********************************************************************************************************************
class WcUnidad(models.Model):
    id_unidad=models.IntegerField( db_column='ID_UNIDAD', primary_key=True )
    id_cliente=models.IntegerField( db_column='ID_CLIENTE' )
    placa=models.CharField( db_column='PLACA', max_length=16, db_collation='utf8_general_ci' )
    marca=models.CharField( db_column='MARCA', max_length=32, db_collation='utf8_general_ci', blank=True, null=True )
    modelo=models.CharField( db_column='MODELO', max_length=32, db_collation='utf8_general_ci', blank=True, null=True )
    motor=models.CharField( db_column='MOTOR', max_length=64, db_collation='utf8_general_ci', blank=True, null=True )
    chasis=models.CharField( db_column='CHASIS', max_length=64, db_collation='utf8_general_ci', blank=True, null=True )
    fh_registro=models.DateTimeField( db_column='FH_REGISTRO', blank=True, null=True )
    rup=models.CharField( db_column='RUP', max_length=11, db_collation='utf8_general_ci', blank=True, null=True )
    nombre_empresa=models.CharField( db_column='NOMBRE_EMPRESA', max_length=64, db_collation='utf8_general_ci',blank=True, null=True )
    telefono_contacto=models.CharField( db_column='TELEFONO_CONTACTO', max_length=32, db_collation='utf8_general_ci',blank=True, null=True )
    celular_contacto=models.CharField( db_column='CELULAR_CONTACTO', max_length=32, db_collation='utf8_general_ci',blank=True, null=True )
    correo_electronico=models.CharField( db_column='CORREO_ELECTRONICO', max_length=32, db_collation='utf8_general_ci',blank=True, null=True )
    direccion=models.CharField( db_column='DIRECCION', max_length=128, db_collation='utf8_general_ci', blank=True, null=True )
    nombre=models.CharField( db_column='NOMBRE', max_length=40, db_collation='utf8_general_ci', blank=True, null=True )
    apellido=models.CharField( db_column='APELLIDO', max_length=40, db_collation='utf8_general_ci', blank=True, null=True )
    cve_usu_alta=models.CharField( db_column='CVE_USU_ALTA', max_length=16, db_collation='utf8_general_ci', blank=True, null=True )
    fh_registro_cliente=models.DateTimeField( db_column='FH_REGISTRO_CLIENTE', blank=True, null=True )
    folio_current=models.IntegerField( db_column='FOLIO_CURRENT', blank=True, null=True )
    folio=models.IntegerField( db_column='FOLIO', blank=True, null=True )
    cve_usu_alta_cliente=models.CharField( db_column='CVE_USU_ALTA_CLIENTE', max_length=16, db_collation='utf8_general_ci', blank=True, null=True )
    kilometraje=models.IntegerField( db_column='KILOMETRAJE', blank=True, null=True )
    fh_alta=models.DateTimeField( db_column='FH_ALTA', blank=True, null=True )
    fh_inicio=models.DateTimeField( db_column='FH_INICIO', blank=True, null=True )
    fh_salida=models.DateTimeField( db_column='FH_SALIDA', blank=True, null=True )
    nombre_entrega=models.CharField( db_column='NOMBRE_ENTREGA', max_length=128, db_collation='utf8_general_ci', blank=True, null=True )
    status=models.IntegerField( db_column='STATUS', blank=True, null=True )
    fh_cancela=models.DateTimeField( db_column='FH_CANCELA', blank=True, null=True )
    km_anterior=models.IntegerField( db_column='KM_ANTERIOR', blank=True, null=True )
    fh_ultimo_servicio=models.DateTimeField( db_column='FH_ULTIMO_SERVICIO', blank=True, null=True )
    folio_ultima_orden=models.IntegerField( db_column='FOLIO_ULTIMA_ORDEN', blank=True, null=True )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'wc_unidad'

class WCuentaAbierta(models.Model):
    folio = models.IntegerField(db_column='Folio', primary_key=True)  
    info=models.CharField( db_column='INFO', max_length=64, blank=True, null=True )  

    cliente = models.CharField(db_column='Cliente', max_length=64, blank=True, null=True)  
    cuenta = models.DecimalField(db_column='Cuenta', max_digits=18, decimal_places=2)  
    fh_registro = models.CharField(db_column='FH_REGISTRO', max_length=19, blank=True, null=True)  
    fh_inicio = models.CharField(db_column='FH_INICIO', max_length=19, blank=True, null=True)
    fh_salida = models.CharField(db_column='FH_SALIDA', max_length=19, blank=True, null=True)
    fh_cancela = models.CharField(db_column='FH_CANCELA', max_length=19, blank=True, null=True)
    fh_registro_unidad=models.CharField( db_column='FH_REGISTRO_UNIDAD', max_length=19, blank=True, null=True )
    fh_ultimo_servicio=models.CharField( db_column='FH_ULTIMO_SERVICIO', max_length=19, blank=True, null=True )
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)
    desc_status=models.CharField( db_column='DESC_STATUS', max_length=31, blank=True);


    usu_alta = models.CharField(db_column='USU_ALTA', max_length=16, blank=True, null=True)  
    descuento_cuenta = models.DecimalField(db_column='DESCUENTO_CUENTA', max_digits=18, decimal_places=4)  
    id_cliente = models.IntegerField(db_column='ID_CLIENTE', blank=True, null=True)  
    placa = models.CharField(db_column='PLACA', max_length=16, blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    km_anterior = models.IntegerField(db_column='KM_ANTERIOR', blank=True, null=True)
    folio_ultima_orden = models.IntegerField(db_column='FOLIO_ULTIMA_ORDEN', blank=True, null=True)
    nombre_entrega = models.CharField(db_column='NOMBRE_ENTREGA', max_length=128, blank=True, null=True)
    marca=models.CharField( db_column='MARCA', max_length=64, blank=True, null=True )
    modelo=models.CharField( db_column='MODELO', max_length=64, blank=True, null=True )
    motor=models.CharField( db_column='MOTOR', max_length=64, blank=True, null=True )
    chasis=models.CharField( db_column='CHASIS', max_length=64, blank=True, null=True )
    cuenta_formato=models.CharField( db_column='CUENTA_FORMATO', max_length=64, blank=True, null=True )

    no_conceptos=models.IntegerField( db_column='NO_CONCEPTOS', blank=True, null=True )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'w_cuenta_abierta'


class WConceptosMain(models.Model):
    id_concepto=models.IntegerField( db_column='ID_CONCEPTO',primary_key=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32, db_collation='utf8_general_ci')  
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', max_length=128, db_collation='utf8_general_ci')  
    id_tipo_servicio = models.IntegerField(db_column='ID_TIPO_SERVICIO')  
    desc_tipo_servicio = models.CharField(db_column='DESC_TIPO_SERVICIO', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO')  
    id_categoria = models.IntegerField(db_column='ID_CATEGORIA', blank=True, null=True)  
    desc_tipo_concepto = models.CharField(db_column='DESC_TIPO_CONCEPTO', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  
    desc_categoria = models.CharField(db_column='DESC_CATEGORIA', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  
    id_unidad_medida = models.IntegerField(db_column='ID_UNIDAD_MEDIDA', blank=True, null=True)  
    abreb_unidad_medida = models.CharField(db_column='ABREB_UNIDAD_MEDIDA', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    desc_periodo_km = models.CharField(db_column='DESC_PERIODO_KM', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  
    id_marca = models.IntegerField(db_column='ID_MARCA', blank=True, null=True)  
    desc_marca = models.CharField(db_column='DESC_MARCA', max_length=64, db_collation='utf8_general_ci', blank=True, null=True)  
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2)  
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)  
    vida_util_hr = models.IntegerField(db_column='VIDA_UTIL_HR', blank=True, null=True)  
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=18, decimal_places=2, blank=True, null=True)  
    hora_hombre = models.DecimalField(db_column='HORA_HOMBRE', max_digits=9, decimal_places=2, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)
    no_serie = models.CharField(db_column='NO_SERIE', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  
    clave_sel = models.CharField(db_column='CLAVE_SEL', max_length=32, db_collation='utf8_general_ci')  
    bs_numero_serie = models.CharField(db_column='BS_NUMERO_SERIE', max_length=32, db_collation='utf8_general_ci')
    b_numero_serie = models.IntegerField(db_column='B_NUMERO_SERIE')
    b_nserie_obligatorio = models.IntegerField(db_column='B_NSERIE_OBLIGATORIO')
    bs_nserie_obligatorio=models.CharField( db_column='BS_NSERIE_OBLIGATORIO', max_length=32, db_collation='utf8_general_ci' )
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2)
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=227, db_collation='utf8_general_ci', blank=True, null=True)
    af_inventario = models.CharField(db_column='AF_INVENTARIO', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)
    b_personal = models.IntegerField(db_column='B_PERSONAL')
    b_agrega_conceptos = models.CharField(db_column='B_AGREGA_CONCEPTOS', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'w_conceptos_main'


class WbUnidad(models.Model):
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', primary_key=True)  # Field name made lowercase.
    id_cliente = models.IntegerField(db_column='ID_CLIENTE')  # Field name made lowercase.
    placa = models.CharField(db_column='PLACA', max_length=16, db_collation='utf8_general_ci')  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='MODELO', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    motor = models.CharField(db_column='MOTOR', max_length=64, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    chasis = models.CharField(db_column='CHASIS', max_length=64, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'wb_unidad'


class WOrdenDetalle(models.Model):
    id_orden_detalle = models.IntegerField(db_column='ID_ORDEN_DETALLE', primary_key=True)  # Field name made lowercase.
    folio_od = models.IntegerField(db_column='FOLIO_OD')  # Field name made lowercase.
    consecutivo = models.IntegerField(db_column='CONSECUTIVO')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    id_personal = models.IntegerField(db_column='ID_PERSONAL', blank=True, null=True)  # Field name made lowercase.
    no_serie_od = models.CharField(db_column='NO_SERIE_OD', max_length=512, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)  # Field name made lowercase.
    precio_compra_od = models.DecimalField(db_column='PRECIO_COMPRA_OD', max_digits=10, decimal_places=2)  # Field name made lowercase.
    precio_venta_od = models.DecimalField(db_column='PRECIO_VENTA_OD', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=1024, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)  # Field name made lowercase.
    cve_usu_alta_od = models.CharField(db_column='CVE_USU_ALTA_OD', max_length=45, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)  # Field name made lowercase.
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')  # Field name made lowercase.
    sit_code = models.CharField(db_column='SIT_CODE', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  # Field name made lowercase.
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', blank=True, null=True)  # Field name made lowercase.
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  # Field name made lowercase.
    fh_alta = models.DateTimeField(db_column='FH_ALTA', blank=True, null=True)  # Field name made lowercase.
    fh_inicio = models.DateTimeField(db_column='FH_INICIO', blank=True, null=True)  # Field name made lowercase.
    fh_salida = models.DateTimeField(db_column='FH_SALIDA', blank=True, null=True)  # Field name made lowercase.
    nombre_entrega = models.CharField(db_column='NOMBRE_ENTREGA', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', blank=True, null=True)  # Field name made lowercase.
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO', blank=True, null=True)  # Field name made lowercase.
    id_categoria = models.IntegerField(db_column='ID_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_unidad_medida = models.IntegerField(db_column='ID_UNIDAD_MEDIDA', blank=True, null=True)  # Field name made lowercase.
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', blank=True, null=True)  # Field name made lowercase.
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)  # Field name made lowercase.
    vida_util_hr = models.IntegerField(db_column='VIDA_UTIL_HR', blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_marca = models.IntegerField(db_column='ID_MARCA', blank=True, null=True)  # Field name made lowercase.
    hora_hombre = models.DecimalField(db_column='HORA_HOMBRE', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    no_serie = models.CharField(db_column='NO_SERIE', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    b_numero_serie = models.IntegerField(db_column='B_NUMERO_SERIE', blank=True, null=True)  # Field name made lowercase.
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_tipo_servicio = models.IntegerField(db_column='ID_TIPO_SERVICIO', blank=True, null=True)  # Field name made lowercase.
    b_agrega_conceptos = models.CharField(db_column='B_AGREGA_CONCEPTOS', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  # Field name made lowercase.
    desc_tipo_concepto = models.CharField(db_column='DESC_TIPO_CONCEPTO', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    b_personal = models.CharField(db_column='B_PERSONAL', max_length=1, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    desc_categoria = models.CharField(db_column='DESC_CATEGORIA', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=40, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=40, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    nombre_persona = models.CharField(db_column='NOMBRE_PERSONA', max_length=81, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    abreb_unidad_medida = models.CharField(db_column='ABREB_UNIDAD_MEDIDA', max_length=81, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'w_orden_detalle'

class Parametros(models.Model):
    cve_parametro = models.CharField(primary_key=True, max_length=128)
    valor = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'



class WsTipoSalida(models.Model):
    id=models.IntegerField( db_column='id', primary_key=True )
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=8, db_collation='utf8_general_ci')
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=139, db_collation='utf8_general_ci', blank=True, null=True)
    desc_operacion = models.CharField(db_column='DESC_OPERACION', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'ws_tipo_salida'


    def toJSON(self):
        item=model_to_dict( self )
        return item


class WListaMantenimiento(models.Model):
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', primary_key=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32, db_collation='utf8_general_ci')  # Field name made lowercase.
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', max_length=128, db_collation='utf8_general_ci')  # Field name made lowercase.
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  # Field name made lowercase.
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2)
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2)
    m25000 = models.BigIntegerField(db_column='M25000')  # Field name made lowercase.
    m50000 = models.BigIntegerField(db_column='M50000')  # Field name made lowercase.
    m75000 = models.BigIntegerField(db_column='M75000')  # Field name made lowercase.
    m100000 = models.BigIntegerField(db_column='M100000')  # Field name made lowercase.
    m125000 = models.BigIntegerField(db_column='M125000')  # Field name made lowercase.
    m150000 = models.BigIntegerField(db_column='M150000')  # Field name made lowercase.
    m175000 = models.BigIntegerField(db_column='M175000')  # Field name made lowercase.
    m200000 = models.BigIntegerField(db_column='M200000')  # Field name made lowercase.
    m225000 = models.BigIntegerField(db_column='M225000')  # Field name made lowercase.
    m275000 = models.BigIntegerField(db_column='M275000')  # Field name made lowercase.
    m300000 = models.BigIntegerField(db_column='M300000')  # Field name made lowercase.
    m325000 = models.BigIntegerField(db_column='M325000')  # Field name made lowercase.
    m350000 = models.BigIntegerField(db_column='M350000')  # Field name made lowercase.
    m375000 = models.BigIntegerField(db_column='M375000')  # Field name made lowercase.
    m400000 = models.BigIntegerField(db_column='M400000')  # Field name made lowercase.
    m425000 = models.BigIntegerField(db_column='M425000')  # Field name made lowercase.
    m450000 = models.BigIntegerField(db_column='M450000')  # Field name made lowercase.
    m475000 = models.BigIntegerField(db_column='M475000')  # Field name made lowercase.
    m500000 = models.BigIntegerField(db_column='M500000')  # Field name made lowercase.
    m525000 = models.BigIntegerField(db_column='M525000')  # Field name made lowercase.
    m550000 = models.BigIntegerField(db_column='M550000')  # Field name made lowercase.
    m575000 = models.BigIntegerField(db_column='M575000')  # Field name made lowercase.
    m600000 = models.BigIntegerField(db_column='M600000')  # Field name made lowercase.
    m625000 = models.BigIntegerField(db_column='M625000')  # Field name made lowercase.
    m650000 = models.BigIntegerField(db_column='M650000')  # Field name made lowercase.
    m675000 = models.BigIntegerField(db_column='M675000')  # Field name made lowercase.
    m700000 = models.BigIntegerField(db_column='M700000')  # Field name made lowercase.
    m725000 = models.BigIntegerField(db_column='M725000')  # Field name made lowercase.
    m750000 = models.BigIntegerField(db_column='M750000')  # Field name made lowercase.
    m775000 = models.BigIntegerField(db_column='M775000')  # Field name made lowercase.
    m800000 = models.BigIntegerField(db_column='M800000')  # Field name made lowercase.
    m825000 = models.BigIntegerField(db_column='M825000')  # Field name made lowercase.
    m850000 = models.BigIntegerField(db_column='M850000')  # Field name made lowercase.
    m875000 = models.BigIntegerField(db_column='M875000')  # Field name made lowercase.
    m900000 = models.BigIntegerField(db_column='M900000')  # Field name made lowercase.
    m925000 = models.BigIntegerField(db_column='M925000')  # Field name made lowercase.
    m950000 = models.BigIntegerField(db_column='M950000')  # Field name made lowercase.
    m975000 = models.BigIntegerField(db_column='M975000')  # Field name made lowercase.
    m1000000 = models.BigIntegerField(db_column='M1000000')  # Field name made lowercase.
    m1025000 = models.BigIntegerField(db_column='M1025000')  # Field name made lowercase.
    m1050000 = models.BigIntegerField(db_column='M1050000')  # Field name made lowercase.
    m1075000 = models.BigIntegerField(db_column='M1075000')  # Field name made lowercase.
    m1100000 = models.BigIntegerField(db_column='M1100000')  # Field name made lowercase.
    m1125000 = models.BigIntegerField(db_column='M1125000')  # Field name made lowercase.
    m1150000 = models.BigIntegerField(db_column='M1150000')  # Field name made lowercase.
    m1175000 = models.BigIntegerField(db_column='M1175000')  # Field name made lowercase.
    m1200000 = models.BigIntegerField(db_column='M1200000')  # Field name made lowercase.
    m1225000 = models.BigIntegerField(db_column='M1225000')  # Field name made lowercase.
    m1250000 = models.BigIntegerField(db_column='M1250000')  # Field name made lowercase.


    def toJSON(self):
        item=model_to_dict( self )
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'w_lista_mantenimiento'


class WbUnidadNeu(models.Model):
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', primary_key=True)  # Field name made lowercase.
    id_cliente = models.IntegerField(db_column='ID_CLIENTE')  # Field name made lowercase.
    placa = models.CharField(db_column='PLACA', max_length=16, db_collation='utf8_general_ci')  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='MODELO', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    motor = models.CharField(db_column='MOTOR', max_length=64, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    chasis = models.CharField(db_column='CHASIS', max_length=64, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', blank=True, null=True)  # Field name made lowercase.

    def toJSON(self):
        item=model_to_dict( self )
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'wb_unidad_neu'


class WcUnidadNeu(models.Model):
    id_unidad = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField()
    placa = models.CharField(max_length=16, db_collation='utf8_general_ci')
    marca = models.CharField(max_length=32, db_collation='utf8_general_ci', blank=True, null=True)
    modelo = models.CharField(max_length=32, db_collation='utf8_general_ci', blank=True, null=True)
    motor = models.CharField(max_length=64, db_collation='utf8_general_ci', blank=True, null=True)
    chasis = models.CharField(max_length=64, db_collation='utf8_general_ci', blank=True, null=True)
    fh_registro = models.DateTimeField(blank=True, null=True)
    rup = models.CharField(max_length=11, db_collation='utf8_general_ci', blank=True, null=True)
    nombre_empresa = models.CharField(max_length=64, db_collation='utf8_general_ci', blank=True, null=True)
    telefono_contacto = models.CharField(max_length=32, db_collation='utf8_general_ci', blank=True, null=True)
    celular_contacto = models.CharField(max_length=32, db_collation='utf8_general_ci', blank=True, null=True)
    correo_electronico = models.CharField(max_length=32, db_collation='utf8_general_ci', blank=True, null=True)
    direccion = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    nombre = models.CharField(max_length=40, db_collation='utf8_general_ci', blank=True, null=True)
    apellido = models.CharField(max_length=40, db_collation='utf8_general_ci', blank=True, null=True)
    cve_usu_alta_cliente = models.CharField(max_length=16, db_collation='utf8_general_ci', blank=True, null=True)
    fh_registro_cliente = models.DateTimeField(blank=True, null=True)
    folio_current = models.IntegerField(blank=True, null=True)
    fh_alta_current = models.DateTimeField(blank=True, null=True)
    kilometraje_current = models.IntegerField(blank=True, null=True)
    nombre_entrega_current = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    folio_ult = models.IntegerField(blank=True, null=True)
    id_unidad_ult = models.IntegerField(blank=True, null=True)
    kilometraje_ult = models.IntegerField(blank=True, null=True)
    cve_usu_alta_ult = models.CharField(max_length=16, db_collation='utf8_general_ci', blank=True, null=True)
    fh_alta_ult = models.DateTimeField(blank=True, null=True)
    fh_inicio_ult = models.DateTimeField(blank=True, null=True)
    fh_salida_ult = models.DateTimeField(blank=True, null=True)
    nombre_entrega_ult = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    status_ult = models.IntegerField(blank=True, null=True)
    fh_cancela_ult = models.DateTimeField(blank=True, null=True)
    km_anterior_ult = models.IntegerField(blank=True, null=True)
    fh_ultimo_servicio_ult = models.DateTimeField(blank=True, null=True)
    folio_ultima_orden_ult = models.IntegerField(blank=True, null=True)
    folio_oa = models.IntegerField(blank=True, null=True)
    fh_salida_oa = models.DateTimeField(blank=True, null=True)
    nombre_entrega_oa = models.CharField(max_length=128, db_collation='utf8_general_ci', blank=True, null=True)
    kilometraje_oa = models.IntegerField(blank=True, null=True)

    def toJSON(self):
        item=model_to_dict( self )
        return item

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'wc_unidad_neu'


class VwNeumaticosPosicion(models.Model):
    cons = models.BigIntegerField(db_column='CONS', primary_key=True)  # Field name made lowercase.
    id_posicion = models.IntegerField(db_column='ID_POSICION')  # Field name made lowercase.
    id_tipo_eje = models.BigIntegerField(db_column='ID_TIPO_EJE')  # Field name made lowercase.
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', blank=True, null=True)  # Field name made lowercase.
    posicion = models.IntegerField(db_column='POSICION', blank=True, null=True)  # Field name made lowercase.
    fh_alta = models.DateTimeField(db_column='FH_ALTA', blank=True, null=True)  # Field name made lowercase.
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=32, db_collation='utf8mb4_0900_ai_ci',
                                    blank=True, null=True)  # Field name made lowercase.
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  # Field name made lowercase.
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  # Field name made lowercase.
    tx_referencia = models.TextField(db_column='TX_REFERENCIA', db_collation='utf8mb4_0900_ai_ci', blank=True,
                                     null=True)  # Field name made lowercase.
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', blank=True, null=True)  # Field name made lowercase.
    no_serie = models.CharField(db_column='NO_SERIE', max_length=64, db_collation='utf8mb4_0900_ai_ci', blank=True,
                                null=True)  # Field name made lowercase.
    sit_code = models.IntegerField(db_column='SIT_CODE', blank=True, null=True)  # Field name made lowercase.
    placa = models.CharField(db_column='PLACA', unique=True, max_length=16)
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', unique=True, max_length=128)
    desc_marca = models.CharField(db_column='DESC_MARCA', max_length=64, db_collation='utf8_general_ci', blank=True,
                                      null=True)
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)
    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_neumaticos_posicion'


class UnidadNeumatico(models.Model):
    id_posicion = models.IntegerField(db_column='ID_POSICION', primary_key=True)  # Field name made lowercase.
    id_unidad = models.IntegerField(db_column='ID_UNIDAD')  # Field name made lowercase.
    posicion = models.IntegerField(db_column='POSICION')  # Field name made lowercase.
    fh_alta = models.DateTimeField(db_column='FH_ALTA')  # Field name made lowercase.
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=32)  # Field name made lowercase.
    kilometraje = models.IntegerField(db_column='KILOMETRAJE')  # Field name made lowercase.
    folio = models.IntegerField(db_column='FOLIO')  # Field name made lowercase.
    tx_referencia = models.TextField(db_column='TX_REFERENCIA')  # Field name made lowercase.
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO')  # Field name made lowercase.
    no_serie = models.CharField(db_column='NO_SERIE', max_length=64)  # Field name made lowercase.
    sit_code = models.IntegerField(db_column='SIT_CODE')  # Field name made lowercase.

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'unidad_neumatico'
