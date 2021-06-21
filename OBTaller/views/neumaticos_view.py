from django.http import JsonResponse
from django.shortcuts import render


def NeumaticosAdmin(request):
    return render( request, 'neumaticos/neumaticos-admin.html' )