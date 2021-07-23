from django.urls import path
from OBTaller.operador.views import IndexOperadorView, UnidadCombustibleCreateView, UnidadCombustibleUpdateView, \
    UnidadCombustibleDeleteView, UnidadPeajeCreateView, UnidadPeajeDeleteView

app_name='operador'


urlpatterns = [
    path('', IndexOperadorView.as_view(), name='index_operador'),
    # path('', IndexOperadorView.as_view(), name='indexl'),
    path('addc/', UnidadCombustibleCreateView.as_view(), name='create_combustible'),
    path('addc/del/<int:id_unidad_combustible>/', UnidadCombustibleDeleteView.as_view(), name='delete_combustible'),
    path('addp/', UnidadPeajeCreateView.as_view(), name='create_peaje'),
    path('addp/del/<int:id_unidad_peaje>/', UnidadPeajeDeleteView.as_view(), name='delete_peaje'),
]