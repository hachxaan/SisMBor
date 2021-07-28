
# from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from OBTaller.operador.views import UnidadCombustibleCreateView
from OBTaller.views.StoreProcedures import StpInsOrden, StpInsBitInventario
from OBTaller.views.cliente.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from OBTaller.views.dash_combustible_consumo_view import DashboardCombustibleConsumoView, \
    DashboardCombustibleConsumoGraficaView
from OBTaller.views.dash_combustible_gasto_view import DashboardCombustibleGastoGraficaView, \
    DashboardCombustibleGastoView
from OBTaller.views.dash_peaje_gasto_view import DashboardPeajeView, DashboardPeajeGraficaView
from OBTaller.views.inventario_neomaticos_view import InventarioNeumaticosView, InventarioNeumaticosUpdateView, \
    InventarioNeumaticosCreateView
from OBTaller.views.inventario_view import InventarioView, InventarioCreateView, InventarioUpdateView
from OBTaller.views.manobra.views import ManobraListView, ManobraCreateView, ManobraUpdateView, ManobraDeleteView
from OBTaller.views.mantenimiento.views import MantenimientoListView, MantenimientoCreateView, MantenimientoUpdateView, \
    MantenimientoDeleteView
from OBTaller.views.personal.views import PersonalListView, PersonalCreateView, PersonalUpdateView, PersonalDeleteView
from OBTaller.views.reportes_view import ReportesView

from OBTaller.views.unidad_view import UnidadListView, UnidadCreateView, UnidadUpdateView, UnidadDeleteView
from OBTaller.views.unidad_asignacion_view import UnidadAsignacionView, UnidadCombustibleTicketView, \
    UnidadCombustibleAdminCreateView, UnidadPeajeTicketView, UnidadPeajeAdminCreateView
from OBTaller.views.views import addConceptoCategoria, addTipoServicio, \
    getInfoUnidad, SetParametros, addConceptoMarca, addUnidadMedida

from OBTaller.views.orden_view import WCuentaAbiertaListView, OrdenNuevaView, UpdSitOrden, OrdenListaEditar, \
    OrdenListaDetalle

from OBTaller.views.neumaticos_view import NeumaticosAdmin

app_name='OBTaller'


urlpatterns=[

    path( '', WCuentaAbiertaListView.as_view(), name='panel_web' ),
    path( 'operacion/', WCuentaAbiertaListView.as_view(), name='panel-operacion' ),
    path( 'parametros/', SetParametros, name='parametros' ),
    path( 'ordennueva/', OrdenNuevaView.as_view(), name='orden_nueva' ),
    path( 'getInfoUnidad/', getInfoUnidad, name='get_info_unidad' ),
    path( 'ordennueva/getInfoUnidad/', getInfoUnidad, name='get_info_unidad' ),


    path( 'operacion/ordendetalle/', OrdenListaDetalle.as_view(), name='detalle_order' ),
    path( 'ordendetalle/', OrdenListaDetalle.as_view(), name='detalle_order' ),

    path( 'neumaticosadmin/', NeumaticosAdmin.as_view(), name='neumaticos_admin' ),
    path( 'reportes/<int:id_reporte>/', ReportesView.as_view(), name='reportes_view' ),
    # path( 'reportes/', ReportesView.as_view(), name='reportes_view' ),

# <int:id_reporte>/

    path( 'inventario/', InventarioView.as_view(), name='inventario_list' ),
    path( 'inventario/add/', InventarioCreateView.as_view(), name='inventario_create' ),
    path( 'inventario/update/<int:id_concepto>/', InventarioUpdateView.as_view(), name='inventario_update' ),

    path('inventario_neumaticos/', InventarioNeumaticosView.as_view(), name='inventario_neumaticos_list'),
    path('inventario_neumaticos/add/', InventarioNeumaticosCreateView.as_view(), name='inventario_neumaticos_create'),
    path('inventario_neumaticos/update/<int:id_concepto>/', InventarioNeumaticosUpdateView.as_view(), name='inventario_neumaticos_update'),

    # *******************************************************************************************************************
    # STORED PROCEDURE
    # *******************************************************************************************************************
        path( 'stp/insorden/', StpInsOrden, name='ins_orden' ),
        path( 'stp/entradainventario/', StpInsBitInventario, name='entrada_inventario' ),
        path( 'stp/salidainventario/', StpInsBitInventario, name='salida_inventario' ),

    # *******************************************************************************************************************
    # UPDATE
    # *******************************************************************************************************************
        path( 'stp/updsitorden/', UpdSitOrden, name='upd_sit_orden' ),
    # *******************************************************************************************************************
    # PROCESOS
    # *******************************************************************************************************************
    #     ORDEN EDITAR
        path( 'operacion/ordeneditar/', OrdenListaEditar.as_view(), name='editar_order' ),
        path( 'ordeneditar/', OrdenListaEditar.as_view(), name='editar_order' ),
        # path( 'operacion/ordeneditar/lista/', OrdenListaEditar.as_view(), name='lista_editar_order' ),

    # *******************************************************************************************************************
    # C O M B U S T I B L E   Y   P E A J E S
    # *******************************************************************************************************************
        path( 'unidades/asignacion/', UnidadAsignacionView.as_view(), name='unidad_asignacion' ),
        path( 'unidades/combustible_ticket/', UnidadCombustibleTicketView.as_view(), name='unidad_combustible_ticket' ),
        path( 'unidades/combustible_ticket/add/<int:id_unidad_asigna>/', UnidadCombustibleAdminCreateView.as_view(), name='create_ticket_combustible' ),
        # path( 'unidades/combustible_ticket/add/', UnidadCombustibleCreateView.as_view(), name='create_unidad_asignacion' ),
        path('unidades/peaje_ticket/', UnidadPeajeTicketView.as_view(), name='unidad_peaje_ticket'),
        path( 'unidades/peaje_ticket/add/<int:id_unidad_asigna>/', UnidadPeajeAdminCreateView.as_view(), name='create_ticket_peaje' ),

        # DASHBOARD ########################################
        path('dashboard/peaje/', DashboardPeajeView.as_view(), name='dashboard_peaje'),
        path('dashboard/peaje/data/<str:tipo>/<int:id_unidad>/<str:filtro>/', DashboardPeajeGraficaView.as_view(), name='dashboard_peaje_grafica'),

        path('dashboard/combustible_gasto/', DashboardCombustibleGastoView.as_view(), name='dashboard_combustible_gasto'),
        path('dashboard/combustible_gasto/data/<str:tipo>/<int:id_unidad>/<str:filtro>/', DashboardCombustibleGastoGraficaView.as_view(), name='dashboard_combustible_gasto_grafica'),

        path('dashboard/combustible_consumo/', DashboardCombustibleConsumoView.as_view(), name='dashboard_combustible_consumo'),
        path('dashboard/combustible_consumo/data/<str:tipo>/<int:id_unidad>/<str:filtro>/', DashboardCombustibleConsumoGraficaView.as_view(), name='dashboard_combustible_consumo_grafica'),


    # *******************************************************************************************************************
    # C A T A L O G O S
    # *******************************************************************************************************************
                # Cliente
                path( 'cliente/list/', ClienteListView.as_view(), name='cliente_list' ),
                path( 'cliente/add/', ClienteCreateView.as_view(), name='cliente_create' ),
                path( 'cliente/update/<int:id_cliente>/', ClienteUpdateView.as_view(), name='cliente_update' ),
                path( 'cliente/delete/<int:id_cliente>/', ClienteDeleteView.as_view(), name='cliente_delete' ),


                # Unidad
                path( 'unidad/list/', UnidadListView.as_view(), name='unidad_list' ),
                path( 'unidad/add/', UnidadCreateView.as_view(), name='unidad_create' ),
                path( 'unidad/update/<int:id_unidad>/', UnidadUpdateView.as_view(), name='unidad_update' ),
                path( 'unidad/delete/<int:id_unidad>/', UnidadDeleteView.as_view(), name='unidad_delete' ),

                # Mano de Obra
                path( 'manobra/list/', ManobraListView.as_view(), name='manobra_list' ),
                path( 'manobra/add/', ManobraCreateView.as_view(), name='manobra_create' ),
                path( 'manobra/update/<int:id_concepto>/', ManobraUpdateView.as_view(), name='manobra_update' ),
                path( 'manobra/delete/<int:id_concepto>/', ManobraDeleteView.as_view(), name='manobra_delete' ),
                # Mantenimiento
                path( 'mantenimiento/list/', MantenimientoListView.as_view(), name='mantenimiento_list' ),
                path( 'mantenimiento/add/', MantenimientoCreateView.as_view(), name='mantenimiento_create' ),
                path( 'mantenimiento/update/<int:id_concepto>/', MantenimientoUpdateView.as_view(), name='mantenimiento_update' ),
                path( 'mantenimiento/delete/<int:id_concepto>/', MantenimientoDeleteView.as_view(), name='mantenimiento_delete' ),
                # Personal
                path( 'personal/list/', PersonalListView.as_view(), name='personal_list' ),
                path( 'personal/add/', PersonalCreateView.as_view(), name='personal_create' ),
                path( 'personal/update/<int:id_personal>/', PersonalUpdateView.as_view(), name='personal_update' ),
                path( 'personal/delete/<int:id_personal>/', PersonalDeleteView.as_view(), name='personal_delete' ),


                # Catálogos generales
                path( 'catalogo/conceptocategoria/add/', addConceptoCategoria, name='conceptocategoria_create' ),
                path( 'catalogo/tiposervicio/add/', addTipoServicio, name='tiposervicio_create' ),
                path( 'catalogo/marca/add/', addConceptoMarca, name='marca_create' ),
                path( 'catalogo/umedida/add/', addUnidadMedida, name='umedida_create' ),




]  + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )