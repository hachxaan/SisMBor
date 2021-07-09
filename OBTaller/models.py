# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.contrib.auth.models import User
from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import now


class BitInventario(models.Model):
    id_trans_inventario = models.AutoField(db_column='ID_TRANS_INVENTARIO', primary_key=True)
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', blank=True, null=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32, default='')
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=8)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)
    cve_usuario = models.CharField(db_column='CVE_USUARIO', max_length=32, blank=True, null=True)
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True, default=0)
    existencia = models.IntegerField(db_column='EXISTENCIA', blank=True, null=True, default=0)
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2, default=0.00)
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=1024, blank=True, null=True)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True, default=0)
    id_orden_detalle = models.IntegerField(db_column='ID_ORDEN_DETALLE', blank=True, null=True, default=0)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        
        db_table = 'bit_inventario'


class BitVenta(models.Model):
    id_trans_venta = models.AutoField(db_column='ID_TRANS_VENTA', primary_key=True)
    id_orden_detalle = models.IntegerField(db_column='ID_ORDEN_DETALLE', blank=True, null=True)
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', blank=True, null=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32, default='')
    imp_trans = models.DecimalField(db_column='IMP_TRANS', max_digits=18, decimal_places=2, default=0)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)
    cve_usuario = models.CharField(db_column='CVE_USUARIO', max_length=32, blank=True, null=True)
    id_personal = models.IntegerField(db_column='ID_PERSONAL', blank=True, null=True)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=128, blank=True, null=True)  
    id_trans_inventario = models.IntegerField(db_column='ID_TRANS_INVENTARIO', blank=True, null=True)  
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=8, blank=True, null=True)  
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  
    fuerzasalida = models.CharField(db_column='FUERZASALIDA', max_length=1, blank=True, null=True)  
    status = models.IntegerField(db_column='STATUS', default=1)
    tipo_venta = models.CharField(db_column='TIPO_VENTA', max_length=16, blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        
        db_table = 'bit_venta'


class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='ID_CLIENTE', primary_key=True)  
    ruc = models.CharField( verbose_name='R.U.C.', db_column='RUC', max_length=11, blank=True, null=True)
    nombre_empresa = models.CharField(db_column='NOMBRE_EMPRESA', max_length=64, blank=True, null=True)  
    telefono_contacto = models.CharField(db_column='TELEFONO_CONTACTO', max_length=32, blank=True, null=True)  
    celular_contacto = models.CharField(db_column='CELULAR_CONTACTO', max_length=32, blank=True, null=True)  
    correo_electronico = models.CharField(db_column='CORREO_ELECTRONICO', max_length=32, blank=True, null=True)  
    direccion = models.CharField(db_column='DIRECCION', max_length=128, blank=True, null=True)  
    nombre = models.CharField(db_column='NOMBRE', max_length=40, blank=True, null=True)
    apellido = models.CharField(db_column='APELLIDO', max_length=40, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)


    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
        db_table = 'cliente'




class ConceptoCategoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO')  
    desc_categoria = models.CharField(db_column='DESC_CATEGORIA', max_length=32)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_categoria
    class Meta:
        
        db_table = 'concepto_categoria'




class TipoServicio(models.Model):
    id_tipo_servicio = models.AutoField(db_column='ID_TIPO_SERVICIO', primary_key=True)  
    desc_tipo_servicio = models.CharField(db_column='DESC_TIPO_SERVICIO', max_length=45, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.desc_tipo_servicio

    class Meta:
        
        db_table = 'tipo_servicio'

class ConceptoTipoMarca(models.Model):
    id_marca = models.AutoField(db_column='ID_MARCA', primary_key=True)
    desc_marca = models.CharField(db_column='DESC_MARCA', unique=True, max_length=64)
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO', blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def __str__(self):
        return self.desc_marca

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
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
        
        db_table = 'periodo_km'



class UnidadMedida(models.Model):
    id_unidad_medida = models.AutoField(db_column='ID_UNIDAD_MEDIDA', primary_key=True)
    desc_unidad_medida = models.CharField(db_column='DESC_UNIDAD_MEDIDA', max_length=45, blank=True, null=True)
    abreb_unidad_medida = models.CharField(db_column='ABREB_UNIDAD_MEDIDA', max_length=45, blank=True, null=True)
    # fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_unidad_medida + ' (' + self.abreb_unidad_medida +')'
    class Meta:
        
        db_table = 'unidad_medida'



class Concepto(models.Model):
    id_concepto=models.AutoField( db_column='ID_CONCEPTO', primary_key=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', unique=True,max_length=32)
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', unique=True, max_length=128)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO')  
    id_categoria = models.ForeignKey( ConceptoCategoria, models.DO_NOTHING, db_column='ID_CATEGORIA')
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2, default=0)
    id_unidad_medida = models.ForeignKey(UnidadMedida, models.DO_NOTHING,db_column='ID_UNIDAD_MEDIDA', blank=True, null=True)
    id_periodo_km = models.ForeignKey( PeriodoKm, models.DO_NOTHING, db_column='ID_PERIODO_KM', blank=True, null=True)  
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)  
    vida_util_hr = models.IntegerField(db_column='VIDA_UTIL_HR', blank=True, null=True)  
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=18, decimal_places=2, blank=True, null=True, default=0)
    id_marca = models.ForeignKey(ConceptoTipoMarca, models.DO_NOTHING, db_column='ID_MARCA', blank=True, null=True)
    hora_hombre = models.DecimalField(db_column='HORA_HOMBRE', max_digits=9, decimal_places=2, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    no_serie = models.CharField(db_column='NO_SERIE', max_length=128, blank=True, null=True)  
    b_numero_serie = models.BooleanField(db_column='B_NUMERO_SERIE')
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2, default=0)
    id_tipo_servicio = models.ForeignKey( TipoServicio, models.DO_NOTHING, default=1, db_column='ID_TIPO_SERVICIO', blank=True, null=True)
    b_agrega_conceptos = models.BooleanField(db_column='B_AGREGA_CONCEPTOS', default=0)
    stock=models.IntegerField( db_column='STOCK' )
    b_nserie_obligatorio=models.BooleanField( db_column='B_NSERIE_OBLIGATORIO' )
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self):
        return self.desc_concepto
    class Meta:
        
        db_table = 'concepto'



class ConceptoKilometraje(models.Model):
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', primary_key=True, max_length=32)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE')  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        
        db_table = 'concepto_kilometraje'


class ConceptoTipo(models.Model):
    id_tipo_concepto = models.AutoField(db_column='ID_TIPO_CONCEPTO', primary_key=True)  
    desc_tipo_concepto = models.CharField(db_column='DESC_TIPO_CONCEPTO', max_length=32)  
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=16)  
    b_aplica_comision = models.CharField(db_column='B_APLICA_COMISION', max_length=1)  
    categoria = models.IntegerField(db_column='CATEGORIA', blank=True, null=True)  
    activo = models.IntegerField(db_column='ACTIVO')  
    b_personal = models.CharField(db_column='B_PERSONAL', max_length=1)  
    posicion = models.IntegerField(db_column='POSICION')
    # fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.desc_tipo_concepto

    class Meta:
        db_table = 'concepto_tipo'


class Cuenta(models.Model):
    id_cuenta = models.AutoField(db_column='ID_CUENTA', primary_key=True)  
    folio = models.ForeignKey('Orden', models.DO_NOTHING, db_column='FOLIO')  
    descuento_cuenta = models.DecimalField(db_column='DESCUENTO_CUENTA', max_digits=18, decimal_places=4, default=0)
    imp_total = models.DecimalField(db_column='IMP_TOTAL', max_digits=18, decimal_places=2, default=0)
    tipo_pago = models.CharField(db_column='TIPO_PAGO', max_length=16, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
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
        
        db_table = 'operacion'


class Orden(models.Model):
    folio = models.AutoField(db_column='FOLIO', primary_key=True)  
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    kilometraje_pq = models.IntegerField(db_column='KILOMETRAJE_PQ', blank=True, null=True)
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_alta = models.DateTimeField(db_column='FH_ALTA', default=now)
    fh_inicio = models.DateTimeField(db_column='FH_INICIO', blank=True, null=True)  
    fh_salida = models.DateTimeField(db_column='FH_SALIDA', blank=True, null=True)
    fh_cancela = models.DateTimeField(db_column='FH_CANCELA', blank=True, null=True)
    nombre_entrega = models.CharField(db_column='NOMBRE_ENTREGA', max_length=128, blank=True, null=True)  
    status = models.IntegerField(db_column='STATUS', default=0)
    km_anterior = models.IntegerField(db_column='KM_ANTERIOR', blank=True, null=True, default=0)
    fh_ultimo_servicio = models.DateTimeField(db_column='FH_ULTIMO_SERVICIO', blank=True, null=True)
    folio_ultima_orden = models.IntegerField(db_column='FOLIO_ULTIMA_ORDEN', blank=True, null=True, default=0)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        
        db_table = 'orden'

class OrdenDetalle(models.Model):
    id_orden_detalle=models.AutoField( db_column='ID_ORDEN_DETALLE', primary_key=True )
    folio = models.IntegerField(db_column='FOLIO')  
    consecutivo = models.IntegerField(db_column='CONSECUTIVO')  
    cantidad = models.IntegerField(db_column='CANTIDAD', default=1)
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO')  
    id_personal=models.IntegerField( db_column='ID_PERSONAL', default=0 )
    no_serie = models.CharField(db_column='NO_SERIE', max_length=512, blank=True, null=True)  
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=10, decimal_places=2, default=0)
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=1024, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=45, blank=True, null=True)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)
    sit_code = models.CharField(db_column='SIT_CODE', max_length=45, default='PE')


    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        
        db_table = 'orden_detalle'
        unique_together = (('folio', 'consecutivo'),)

class OrdenReferencias(models.Model):
    id_orden_referencia = models.AutoField(db_column='ID_ORDEN_REFERENCIA', primary_key=True)  
    folio = models.IntegerField(db_column='FOLIO')  
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=512, blank=True, null=True)  
    cve_usuario_alta = models.CharField(db_column='CVE_USUARIO_ALTA', max_length=32, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'orden_referencias'



class Personal(models.Model):
    id_personal = models.AutoField(db_column='ID_PERSONAL', primary_key=True)  
    nombre = models.CharField(db_column='NOMBRE', unique=True, max_length=40, blank=True, null=True)  
    apellido = models.CharField(db_column='APELLIDO', max_length=40, blank=True, null=True)  
    # cve_usu_alta = models.ForeignKey(User, null=True, blank=True)
    cve_usu_alta = models.CharField(User, db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now, blank=True, null=True)
    # , auto_now_add=True

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        
        db_table = 'personal'

class Unidad(models.Model):
    id_unidad = models.AutoField(db_column='ID_UNIDAD', primary_key=True)  
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ID_CLIENTE')  
    placa = models.CharField(db_column='PLACA', unique=True, max_length=16)  
    marca = models.CharField(db_column='MARCA', max_length=32, blank=True, null=True)  
    modelo = models.CharField(db_column='MODELO', max_length=32, blank=True, null=True)  
    motor = models.CharField(db_column='MOTOR', max_length=64, blank=True, null=True)  
    chasis = models.CharField(db_column='CHASIS', max_length=64, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)

    def toJSON(self):
        item = model_to_dict(self)
        return item



    class Meta:
        
        db_table = 'unidad'




class Usuario(models.Model):
    cve_usuario = models.CharField(db_column='CVE_USUARIO', primary_key=True, max_length=32)
    nombre = models.CharField(db_column='NOMBRE', max_length=64, blank=True, null=True)  
    passw = models.CharField(db_column='PASSW', max_length=64, blank=True, null=True)  
    mail = models.CharField(db_column='MAIL', max_length=64, blank=True, null=True)  
    sit_usuario = models.CharField(db_column='SIT_USUARIO', max_length=5)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', default=now)
    b_system = models.CharField(db_column='B_SYSTEM', max_length=5)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'usuario'


# **********************************************************************************************************************
#         vistas
# **********************************************************************************************************************
class WcUnidad(models.Model):
    id_unidad=models.IntegerField( db_column='ID_UNIDAD', primary_key=True )
    id_cliente = models.IntegerField(db_column='ID_CLIENTE')  
    placa = models.CharField(db_column='PLACA', max_length=16)
    marca = models.CharField(db_column='MARCA', max_length=32, blank=True, null=True)
    modelo = models.CharField(db_column='MODELO', max_length=32, blank=True, null=True)
    motor = models.CharField(db_column='MOTOR', max_length=64, blank=True, null=True)
    chasis = models.CharField(db_column='CHASIS', max_length=64, blank=True, null=True)
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', blank=True, null=True)
    ruc = models.CharField(db_column='RUC', max_length=11, blank=True, null=True)
    nombre_empresa = models.CharField(db_column='NOMBRE_EMPRESA', max_length=64, blank=True, null=True)
    telefono_contacto = models.CharField(db_column='TELEFONO_CONTACTO', max_length=32, blank=True, null=True)
    celular_contacto = models.CharField(db_column='CELULAR_CONTACTO', max_length=32, blank=True, null=True)
    correo_electronico = models.CharField(db_column='CORREO_ELECTRONICO', max_length=32, blank=True, null=True)
    direccion = models.CharField(db_column='DIRECCION', max_length=128, blank=True, null=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=40, blank=True, null=True)
    apellido = models.CharField(db_column='APELLIDO', max_length=40, blank=True, null=True)
    cve_usu_alta_cliente = models.CharField(db_column='CVE_USU_ALTA_CLIENTE', max_length=16, blank=True, null=True)
    fh_registro_cliente = models.DateTimeField(db_column='FH_REGISTRO_CLIENTE', blank=True, null=True)
    folio_current = models.IntegerField(db_column='FOLIO_CURRENT', blank=True, null=True)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    fh_alta = models.DateTimeField(db_column='FH_ALTA', blank=True, null=True)  
    fh_inicio = models.DateTimeField(db_column='FH_INICIO', blank=True, null=True)  
    fh_salida = models.DateTimeField(db_column='FH_SALIDA', blank=True, null=True)  
    nombre_entrega = models.CharField(db_column='NOMBRE_ENTREGA', max_length=128, blank=True, null=True)
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  
    fh_cancela = models.DateTimeField(db_column='FH_CANCELA', blank=True, null=True)  
    km_anterior = models.IntegerField(db_column='KM_ANTERIOR', blank=True, null=True)  
    fh_ultimo_servicio = models.DateTimeField(db_column='FH_ULTIMO_SERVICIO', blank=True, null=True)
    folio_ultima_orden = models.IntegerField(db_column='FOLIO_ULTIMA_ORDEN', blank=True, null=True)


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
    desc_status=models.CharField(db_column='DESC_STATUS', max_length=31, blank=True)
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
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32)  
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', max_length=128)  
    id_tipo_servicio = models.IntegerField(db_column='ID_TIPO_SERVICIO')  
    desc_tipo_servicio = models.CharField(db_column='DESC_TIPO_SERVICIO', max_length=45, blank=True, null=True)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO')  
    id_categoria = models.IntegerField(db_column='ID_CATEGORIA', blank=True, null=True)  
    desc_tipo_concepto = models.CharField(db_column='DESC_TIPO_CONCEPTO', max_length=32, blank=True, null=True)  
    desc_categoria = models.CharField(db_column='DESC_CATEGORIA', max_length=32, blank=True, null=True)  
    id_unidad_medida = models.IntegerField(db_column='ID_UNIDAD_MEDIDA', blank=True, null=True)  
    abreb_unidad_medida = models.CharField(db_column='ABREB_UNIDAD_MEDIDA', max_length=45, blank=True, null=True)  
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    desc_periodo_km = models.CharField(db_column='DESC_PERIODO_KM', max_length=16, blank=True, null=True)  
    id_marca = models.IntegerField(db_column='ID_MARCA', blank=True, null=True)  
    desc_marca = models.CharField(db_column='DESC_MARCA', max_length=64, blank=True, null=True)  
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2)  
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)  
    vida_util_hr = models.IntegerField(db_column='VIDA_UTIL_HR', blank=True, null=True)  
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=18, decimal_places=2, blank=True, null=True)  
    hora_hombre = models.DecimalField(db_column='HORA_HOMBRE', max_digits=9, decimal_places=2, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)
    no_serie = models.CharField(db_column='NO_SERIE', max_length=128, blank=True, null=True)  
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  
    clave_sel = models.CharField(db_column='CLAVE_SEL', max_length=32)  
    bs_numero_serie = models.CharField(db_column='BS_NUMERO_SERIE', max_length=32)
    b_numero_serie = models.IntegerField(db_column='B_NUMERO_SERIE')
    b_nserie_obligatorio = models.IntegerField(db_column='B_NSERIE_OBLIGATORIO')
    bs_nserie_obligatorio=models.CharField( db_column='BS_NSERIE_OBLIGATORIO', max_length=32 )
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2)
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=227, blank=True, null=True)
    af_inventario = models.CharField(db_column='AF_INVENTARIO', max_length=1, blank=True, null=True)
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=16, blank=True, null=True)
    b_personal = models.IntegerField(db_column='B_PERSONAL')
    b_agrega_conceptos = models.CharField(db_column='B_AGREGA_CONCEPTOS', max_length=1, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'w_conceptos_main'


class WbUnidad(models.Model):
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', primary_key=True)  
    id_cliente = models.IntegerField(db_column='ID_CLIENTE')  
    placa = models.CharField(db_column='PLACA', max_length=16)  
    marca = models.CharField(db_column='MARCA', max_length=32, blank=True, null=True)  
    modelo = models.CharField(db_column='MODELO', max_length=32, blank=True, null=True)  
    motor = models.CharField(db_column='MOTOR', max_length=64, blank=True, null=True)  
    chasis = models.CharField(db_column='CHASIS', max_length=64, blank=True, null=True)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'wb_unidad'


class WOrdenDetalle(models.Model):
    id_orden_detalle = models.IntegerField(db_column='ID_ORDEN_DETALLE', primary_key=True)  
    folio_od = models.IntegerField(db_column='FOLIO_OD')  
    consecutivo = models.IntegerField(db_column='CONSECUTIVO')  
    cantidad = models.IntegerField(db_column='CANTIDAD')  
    id_personal = models.IntegerField(db_column='ID_PERSONAL', blank=True, null=True)  
    no_serie_od = models.CharField(db_column='NO_SERIE_OD', max_length=512, blank=True, null=True)  
    precio_compra_od = models.DecimalField(db_column='PRECIO_COMPRA_OD', max_digits=10, decimal_places=2)  
    precio_venta_od = models.DecimalField(db_column='PRECIO_VENTA_OD', max_digits=10, decimal_places=2)  
    tx_referencia = models.CharField(db_column='TX_REFERENCIA', max_length=1024, blank=True, null=True)  
    cve_usu_alta_od = models.CharField(db_column='CVE_USU_ALTA_OD', max_length=45, blank=True, null=True)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO')  
    sit_code = models.CharField(db_column='SIT_CODE', max_length=45)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    fh_alta = models.DateTimeField(db_column='FH_ALTA', blank=True, null=True)  
    fh_inicio = models.DateTimeField(db_column='FH_INICIO', blank=True, null=True)  
    fh_salida = models.DateTimeField(db_column='FH_SALIDA', blank=True, null=True)  
    nombre_entrega = models.CharField(db_column='NOMBRE_ENTREGA', max_length=128, blank=True, null=True)  
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', blank=True, null=True)  
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32, blank=True, null=True)  
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', max_length=128, blank=True, null=True)  
    id_tipo_concepto = models.IntegerField(db_column='ID_TIPO_CONCEPTO', blank=True, null=True)  
    id_categoria = models.IntegerField(db_column='ID_CATEGORIA', blank=True, null=True)  
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2, blank=True, null=True)  
    id_unidad_medida = models.IntegerField(db_column='ID_UNIDAD_MEDIDA', blank=True, null=True)  
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', blank=True, null=True)  
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)  
    vida_util_hr = models.IntegerField(db_column='VIDA_UTIL_HR', blank=True, null=True)  
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=18, decimal_places=2, blank=True, null=True)  
    id_marca = models.IntegerField(db_column='ID_MARCA', blank=True, null=True)  
    hora_hombre = models.DecimalField(db_column='HORA_HOMBRE', max_digits=9, decimal_places=2, blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=16, blank=True, null=True)  
    no_serie = models.CharField(db_column='NO_SERIE', max_length=128, blank=True, null=True)  
    b_numero_serie = models.IntegerField(db_column='B_NUMERO_SERIE', blank=True, null=True)  
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2, blank=True, null=True)  
    id_tipo_servicio = models.IntegerField(db_column='ID_TIPO_SERVICIO', blank=True, null=True)  
    b_agrega_conceptos = models.CharField(db_column='B_AGREGA_CONCEPTOS', max_length=1, blank=True, null=True)  
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  
    desc_tipo_concepto = models.CharField(db_column='DESC_TIPO_CONCEPTO', max_length=32, blank=True, null=True)  
    b_personal = models.CharField(db_column='B_PERSONAL', max_length=1, blank=True, null=True)  
    desc_categoria = models.CharField(db_column='DESC_CATEGORIA', max_length=32, blank=True, null=True)  
    nombre = models.CharField(db_column='NOMBRE', max_length=40, blank=True, null=True)  
    apellido = models.CharField(db_column='APELLIDO', max_length=40, blank=True, null=True)  
    nombre_persona = models.CharField(db_column='NOMBRE_PERSONA', max_length=81, blank=True, null=True)  
    abreb_unidad_medida = models.CharField(db_column='ABREB_UNIDAD_MEDIDA', max_length=81, blank=True, null=True)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'w_orden_detalle'

class Parametros(models.Model):
    cve_parametro = models.CharField(primary_key=True, max_length=128)
    valor = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        db_table = 'parametros'



class WsTipoSalida(models.Model):
    id=models.IntegerField( db_column='id', primary_key=True )
    cve_operacion = models.CharField(db_column='CVE_OPERACION', max_length=8)
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=139, blank=True, null=True)
    desc_operacion = models.CharField(db_column='DESC_OPERACION', max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_tipo_salida'

    def toJSON(self):
        item=model_to_dict( self )
        return item


class WListaMantenimiento(models.Model):
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', primary_key=True)
    cve_concepto = models.CharField(db_column='CVE_CONCEPTO', max_length=32)  
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', max_length=128)  
    id_periodo_km = models.IntegerField(db_column='ID_PERIODO_KM', blank=True, null=True)  
    stock = models.IntegerField(db_column='STOCK', blank=True, null=True)  
    precio_compra = models.DecimalField(db_column='PRECIO_COMPRA', max_digits=18, decimal_places=2)
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=18, decimal_places=2)
    m25000 = models.BigIntegerField(db_column='M25000')  
    m50000 = models.BigIntegerField(db_column='M50000')  
    m75000 = models.BigIntegerField(db_column='M75000')  
    m100000 = models.BigIntegerField(db_column='M100000')  
    m125000 = models.BigIntegerField(db_column='M125000')  
    m150000 = models.BigIntegerField(db_column='M150000')  
    m175000 = models.BigIntegerField(db_column='M175000')  
    m200000 = models.BigIntegerField(db_column='M200000')  
    m225000 = models.BigIntegerField(db_column='M225000')  
    m275000 = models.BigIntegerField(db_column='M275000')  
    m300000 = models.BigIntegerField(db_column='M300000')  
    m325000 = models.BigIntegerField(db_column='M325000')  
    m350000 = models.BigIntegerField(db_column='M350000')  
    m375000 = models.BigIntegerField(db_column='M375000')  
    m400000 = models.BigIntegerField(db_column='M400000')  
    m425000 = models.BigIntegerField(db_column='M425000')  
    m450000 = models.BigIntegerField(db_column='M450000')  
    m475000 = models.BigIntegerField(db_column='M475000')  
    m500000 = models.BigIntegerField(db_column='M500000')  
    m525000 = models.BigIntegerField(db_column='M525000')  
    m550000 = models.BigIntegerField(db_column='M550000')  
    m575000 = models.BigIntegerField(db_column='M575000')  
    m600000 = models.BigIntegerField(db_column='M600000')  
    m625000 = models.BigIntegerField(db_column='M625000')  
    m650000 = models.BigIntegerField(db_column='M650000')  
    m675000 = models.BigIntegerField(db_column='M675000')  
    m700000 = models.BigIntegerField(db_column='M700000')  
    m725000 = models.BigIntegerField(db_column='M725000')  
    m750000 = models.BigIntegerField(db_column='M750000')  
    m775000 = models.BigIntegerField(db_column='M775000')  
    m800000 = models.BigIntegerField(db_column='M800000')  
    m825000 = models.BigIntegerField(db_column='M825000')  
    m850000 = models.BigIntegerField(db_column='M850000')  
    m875000 = models.BigIntegerField(db_column='M875000')  
    m900000 = models.BigIntegerField(db_column='M900000')  
    m925000 = models.BigIntegerField(db_column='M925000')  
    m950000 = models.BigIntegerField(db_column='M950000')  
    m975000 = models.BigIntegerField(db_column='M975000')  
    m1000000 = models.BigIntegerField(db_column='M1000000')  
    m1025000 = models.BigIntegerField(db_column='M1025000')  
    m1050000 = models.BigIntegerField(db_column='M1050000')  
    m1075000 = models.BigIntegerField(db_column='M1075000')  
    m1100000 = models.BigIntegerField(db_column='M1100000')  
    m1125000 = models.BigIntegerField(db_column='M1125000')  
    m1150000 = models.BigIntegerField(db_column='M1150000')  
    m1175000 = models.BigIntegerField(db_column='M1175000')  
    m1200000 = models.BigIntegerField(db_column='M1200000')  
    m1225000 = models.BigIntegerField(db_column='M1225000')  
    m1250000 = models.BigIntegerField(db_column='M1250000')  


    def toJSON(self):
        item=model_to_dict( self )
        return item

    class Meta:
        managed = False
        db_table = 'w_lista_mantenimiento'


class WbUnidadNeu(models.Model):
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', primary_key=True)  
    id_cliente = models.IntegerField(db_column='ID_CLIENTE')  
    placa = models.CharField(db_column='PLACA', max_length=16)  
    marca = models.CharField(db_column='MARCA', max_length=32, blank=True, null=True)  
    modelo = models.CharField(db_column='MODELO', max_length=32, blank=True, null=True)  
    motor = models.CharField(db_column='MOTOR', max_length=64, blank=True, null=True)  
    chasis = models.CharField(db_column='CHASIS', max_length=64, blank=True, null=True)  
    fh_registro = models.DateTimeField(db_column='FH_REGISTRO', blank=True, null=True)  

    def toJSON(self):
        item=model_to_dict( self )
        return item

    class Meta:
        managed = False
        db_table = 'wb_unidad_neu'


class WcUnidadNeu(models.Model):
    id_unidad = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField()
    placa = models.CharField(max_length=16)
    marca = models.CharField(max_length=32, blank=True, null=True)
    modelo = models.CharField(max_length=32, blank=True, null=True)
    motor = models.CharField(max_length=64, blank=True, null=True)
    chasis = models.CharField(max_length=64, blank=True, null=True)
    fh_registro = models.DateTimeField(blank=True, null=True)
    ruc = models.CharField(max_length=11, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=64, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=32, blank=True, null=True)
    celular_contacto = models.CharField(max_length=32, blank=True, null=True)
    correo_electronico = models.CharField(max_length=32, blank=True, null=True)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    apellido = models.CharField(max_length=40, blank=True, null=True)
    cve_usu_alta_cliente = models.CharField(max_length=16, blank=True, null=True)
    fh_registro_cliente = models.DateTimeField(blank=True, null=True)
    folio_current = models.IntegerField(blank=True, null=True)
    fh_alta_current = models.DateTimeField(blank=True, null=True)
    kilometraje_current = models.IntegerField(blank=True, null=True)
    nombre_entrega_current = models.CharField(max_length=128, blank=True, null=True)
    folio_ult = models.IntegerField(blank=True, null=True)
    id_unidad_ult = models.IntegerField(blank=True, null=True)
    kilometraje_ult = models.IntegerField(blank=True, null=True)
    cve_usu_alta_ult = models.CharField(max_length=16, blank=True, null=True)
    fh_alta_ult = models.DateTimeField(blank=True, null=True)
    fh_inicio_ult = models.DateTimeField(blank=True, null=True)
    fh_salida_ult = models.DateTimeField(blank=True, null=True)
    nombre_entrega_ult = models.CharField(max_length=128, blank=True, null=True)
    status_ult = models.IntegerField(blank=True, null=True)
    fh_cancela_ult = models.DateTimeField(blank=True, null=True)
    km_anterior_ult = models.IntegerField(blank=True, null=True)
    fh_ultimo_servicio_ult = models.DateTimeField(blank=True, null=True)
    folio_ultima_orden_ult = models.IntegerField(blank=True, null=True)
    folio_oa = models.IntegerField(blank=True, null=True)
    fh_salida_oa = models.DateTimeField(blank=True, null=True)
    nombre_entrega_oa = models.CharField(max_length=128, blank=True, null=True)
    kilometraje_oa = models.IntegerField(blank=True, null=True)

    def toJSON(self):
        item=model_to_dict( self )
        return item

    class Meta:
        managed = False
        db_table = 'wc_unidad_neu'


class VwNeumaticosPosicion(models.Model):
    cons = models.BigIntegerField(db_column='CONS', primary_key=True)  
    id_posicion = models.IntegerField(db_column='ID_POSICION')  
    id_tipo_eje = models.BigIntegerField(db_column='ID_TIPO_EJE')  
    id_unidad = models.IntegerField(db_column='ID_UNIDAD', blank=True, null=True)  
    posicion = models.IntegerField(db_column='POSICION', blank=True, null=True)  
    fh_alta = models.DateTimeField(db_column='FH_ALTA', blank=True, null=True)  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=32,
                                    blank=True, null=True)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', blank=True, null=True)  
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  
    tx_referencia = models.TextField(db_column='TX_REFERENCIA', blank=True,
                                     null=True)  
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', blank=True, null=True)  
    no_serie = models.CharField(db_column='NO_SERIE', max_length=64, blank=True,
                                null=True)  
    sit_code = models.IntegerField(db_column='SIT_CODE', blank=True, null=True)  
    placa = models.CharField(db_column='PLACA', unique=True, max_length=16)
    desc_concepto = models.CharField(db_column='DESC_CONCEPTO', unique=True, max_length=128)
    desc_marca = models.CharField(db_column='DESC_MARCA', max_length=64, blank=True,
                                      null=True)
    vida_util_km = models.IntegerField(db_column='VIDA_UTIL_KM', blank=True, null=True)
    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        managed = False
        db_table = 'vw_neumaticos_posicion'


class UnidadNeumatico(models.Model):
    id_posicion = models.AutoField(db_column='ID_POSICION', primary_key=True)
    id_unidad = models.IntegerField(db_column='ID_UNIDAD')  
    posicion = models.IntegerField(db_column='POSICION')  
    fh_alta = models.DateTimeField(db_column='FH_ALTA')  
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=32)  
    kilometraje = models.IntegerField(db_column='KILOMETRAJE')  
    folio = models.IntegerField(db_column='FOLIO')  
    tx_referencia = models.TextField(db_column='TX_REFERENCIA')  
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO')  
    no_serie = models.CharField(db_column='NO_SERIE', max_length=64)  
    sit_code = models.IntegerField(db_column='SIT_CODE')  
    id_orden_detalle = models.IntegerField(db_column='ID_ORDEN_DETALLE', blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'unidad_neumatico'

class BitUnidadNeumatico(models.Model):
    id_bit_uni_neu = models.AutoField(db_column='ID_BIT_UNI_NEU', primary_key=True)  
    fh_alta_bit = models.DateTimeField(db_column='FH_ALTA_BIT', default=now)
    id_posicion = models.IntegerField(db_column='ID_POSICION')  
    id_unidad = models.IntegerField(db_column='ID_UNIDAD')  
    posicion = models.IntegerField(db_column='POSICION')  
    fh_alta = models.DateTimeField(db_column='FH_ALTA', default=now)
    cve_usu_alta = models.CharField(db_column='CVE_USU_ALTA', max_length=32, default='')
    kilometraje = models.IntegerField(db_column='KILOMETRAJE', default=0)
    folio = models.IntegerField(db_column='FOLIO', default=0)
    tx_referencia = models.TextField(db_column='TX_REFERENCIA')  
    id_concepto = models.IntegerField(db_column='ID_CONCEPTO', default=0)
    no_serie = models.CharField(db_column='NO_SERIE', max_length=64, default=0)
    sit_code = models.IntegerField(db_column='SIT_CODE', default=0)
    id_orden_detalle = models.IntegerField(db_column='ID_ORDEN_DETALLE', blank=True, null=True, default=0)
    bit_tipo = models.CharField(db_column='BIT_TIPO', max_length=45)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'bit_unidad_neumatico'

class Reportes(models.Model):
    id_reporte = models.AutoField(db_column='ID_REPORTE', primary_key=True)  
    titulo_reporte = models.CharField(db_column='TITULO_REPORTE', max_length=45)  
    desc_reporte = models.CharField(db_column='DESC_REPORTE', max_length=128)  
    vista = models.CharField(db_column='VISTA', max_length=45)  
    activo = models.CharField(db_column='ACTIVO', max_length=45)  
    nom_file = models.CharField(db_column='NOM_FILE', max_length=128)  

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'reportes'


class VwrServicioUnidad(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    placa = models.CharField(db_column='Placa', max_length=16, blank=True, null=True)
    servicios = models.BigIntegerField(db_column='Servicios')  
    fecha = models.CharField(db_column='Fecha', max_length=16, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        managed = False
        db_table = 'vwr_servicio_unidad'

#
# class User(AbstractUser):
#     is_admin_web = models.BooleanField(default=False)
#     is_user_web = models.BooleanField(default=False)
#     is_unidad = models.BooleanField(default=False)
#
#
# class UnidadUser(models.Model):
#     id_unidad = models.OneToOneField(Unidad, on_delete=models.CASCADE, primary_key=True)
#     id_personal = models.IntegerField(Personal)
#
