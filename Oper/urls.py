from django.urls import path
from Oper.views import login

app_name = 'Oper'
urlpatterns = [
    path('operador', login, name='login'),
]
