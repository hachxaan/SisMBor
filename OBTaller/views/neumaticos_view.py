from django.http import JsonResponse
from django.shortcuts import render


def NeumaticosAdmin(request):
    context={}
    context['neumaticos'] = 'active'
    return render( request, 'neumaticos/neumaticos-admin.html', context )