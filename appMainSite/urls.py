"""appMainSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from OBTaller.loginus.views import LoginFromView, LoginOperador
urlpatterns = [

    path('', include('OBTaller.urls')),
    path('registro/', include('OBTaller.operador.urls')),
    path('accounts/login/', LoginFromView.as_view()),
    path('login/', LoginFromView.as_view(), name='login'),
    path('loginoper/', LoginOperador.as_view(), name='login_operador'),
    path('admin/', admin.site.urls),
    path('accounts/', include( 'django.contrib.auth.urls' ) ),
    # url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
urlpatterns += [

]