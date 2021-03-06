
# C O N C E P T O S ################
TCONCEPTO_MANTENIMIENTO = 1;
TCONCEPTO_MANOBRA = 2
TCONCEPTO_MATERIAL = 3
TCONCEPTO_COMPONENTE = 4
TCONCEPTO_NEUMATICOS = 5
TCONCEPTO_COMBUSTIBLE = 6
TCONCEPTO_REPUESTOS = 7
####################################

#### ID CATEGORIA MANTENIMIENTO ####
ID_CATEGORIA_MANTO = 44
####################################

####### T I P O   D E   P E R S O N A  #######
TPERSONAL_MECANICO = 1
TPERSONAL_OPERADOR_UNIDAD = 2
#############################################

####### T I P O   D E   U S U A R I O  #######
TUSUARIO_PERFIL = 1
TUSUARIO_SISTEMAS = 2
TUSUARIO_ADMINISTRADOR = 3
TUSUARIO_SOLOLECTURA = 4
#############################################


####### T I P O   D E   P E R F I L     #######
TPERFIL_TALLER = 1
TPERFIL_SISTEMAS = 2
TPERFIL_ADMINISTRADOR = 3
TPERFIL_SOLOLECTURA = 4
TPERFIL_DIRECCION = 5
TPERFIL_OPERADOR = 6
TPERFIL_CONTABILIDAD = 7
TPERFIL_ADMINISTRACION = 8
TPERFIL_CAJA = 9
#############################################

TCOMBUSTIBLE_DISEL = 1
TCOMBUSTIBLE_GNV = 2


UNIDAD_MEDIDA_COMBUSTIBLE = (
    (1, "DISEL"),
    (2, "GNV")
)

urlsOperador = ['/registro/', '/loginoper/']