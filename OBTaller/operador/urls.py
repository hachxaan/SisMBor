from django.urls import path
from OBTaller.operador.views import IndexOperadorView


urlpatterns = [

    path('', IndexOperadorView.as_view(), name='index_operador'),
]