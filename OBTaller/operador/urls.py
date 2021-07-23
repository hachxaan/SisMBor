from django.urls import path
from OBTaller.operador.views import IndexOperadorView, UnidadCombustibleCreateView

urlpatterns = [

    path('', IndexOperadorView.as_view(), name='index_operador'),
    # path('', IndexOperadorView.as_view(), name='indexl'),
    path('addc/', UnidadCombustibleCreateView.as_view(), name='create_combustible'),
]