
# from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from OBTaller.views.StoreProcedures import StpInsOrden
from OBTaller.views.cliente.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from OBTaller.views.manobra.views import ManobraListView, ManobraCreateView, ManobraUpdateView, ManobraDeleteView
from OBTaller.views.personal.views import PersonalListView, PersonalCreateView, PersonalUpdateView, PersonalDeleteView
from OBTaller.views.unidad.views import UnidadListView, UnidadCreateView, UnidadUpdateView, UnidadDeleteView
from OBTaller.views.views import WCuentaAbiertaListView, login, addConceptoCategoria, addTipoServicio, \
    getInfoUnidad, OrdenNuevaView

app_name='OBTaller'


urlpatterns=[



    path( '', WCuentaAbiertaListView.as_view(), name='panel-operacion' ),
    path( '', login, name='login' ),
    # path( 'panel/', panel, name='panel' ),
    path( 'operacion/', WCuentaAbiertaListView.as_view(), name='panel-operacion' ),
    path( 'ordennueva/', OrdenNuevaView, name='orden-nueva' ),
    path( 'ordennueva/getInfoUnidad/', getInfoUnidad, name='get_info_unidad' ),

    # path('unidad/', UnidadView.as_view(), name='unidad-list'),
    # path('unidad/<int:id_unidad>/', UnidadDetailView.as_view(), name='unidad-detail'),
    # path('unidad/edit/<int:id_unidad>/', Unidadedit, name='unidad-edit'),
    # path('unidad/create/', Unidadcreate, name='unidad-create'),
    # path('unidad/delete/<int:id_unidad>/', Unidaddelete, name='unidad-delete'),
    # *******************************************************************************************************************
    # STORE PROCEDURES
    # *******************************************************************************************************************
        path( 'stp/insorden/', StpInsOrden, name='ins_orden' ),
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

                # Personal
                path( 'personal/list/', PersonalListView.as_view(), name='personal_list' ),
                path( 'personal/add/', PersonalCreateView.as_view(), name='personal_create' ),
                path( 'personal/update/<int:id_personal>/', PersonalUpdateView.as_view(), name='personal_update' ),
                path( 'personal/delete/<int:id_personal>/', PersonalDeleteView.as_view(), name='personal_delete' ),


                # Catálogos generales
                path( 'catalogo/conceptocategoria/add/', addConceptoCategoria, name='conceptocategoria_create' ),
                path( 'catalogo/tiposervicio/add/', addTipoServicio, name='tiposervicio_create' ),

                # path( 'cliente/add/', ClienteCreateView.as_view(), name='cliente_create' ),
                # path( 'cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update' ),
                # path( 'cliente/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete' ),


]  + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )