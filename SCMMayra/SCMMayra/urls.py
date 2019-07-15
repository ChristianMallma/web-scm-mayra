"""SCMMayra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('produccion/', include('produccion.urls')),
    path('admin/', admin.site.urls),
    #paths del Autenticador (Ath)
    path('accounts/',include('django.contrib.auth.urls')),
    #paths de la página web
    path("WebPage/",include('coreWebPage.urls')),
    #paths de registration
    path('accounts/', include('registration.urls')),
    #paths de catalog
    path('catalog/', include('catalog.urls')),
    #paths de comprobantes
    path('comprobante/', include('salidas.urls')),
    #paths de distribución
    path('distribucion/', include('distribucion.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#Personalizando el admin
admin.site.site_header="SCM Mayra"
admin.site.index_title="Panel de administrador"
admin.site.site_title="SCM Mayra"