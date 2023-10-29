"""
URL configuration for tienda_website_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from homepage import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    
    path('catalogo/', views.catalogo, name='catalogo'),
    
    path('Carrito/', views.CarritoCompras, name='Carrito'),
    
    path('contacto/', views.contacto, name='contacto'),
    
    path('Dashboard/', views.Dashboard, name='Dashboard'),  
    
    path('GenerarPedido/', views.GenerarPedido, name='GenerarPedido'),
    
    path('login/', views.login, name='login'),#son las rutas
    
    path('logout/', views.logout, name='logout'),
    
    path('ofertas/', views.ofertas, name='ofertas'),
    
    path('PedidoRealizado/', views.PedidoRealizado, name='PedidoRealizado'),
    
    path('Proveedores/', views.Proveedores, name='proveedores'),
    
    path('productoDetalle/', views.ProductoDetalle, name='productoDetalle'),
    
    path('RegistrosUsuarios/', views.RegistrosUsuarios, name='RegistrosUsuarios'),
    
    path('RecuperacionContrasena/', views.RecuperacionContrasena, name='RecuperacionContrasena'),
    
    path('Roles/', views.Roles, name='Roles'),
    
    path('VentasRealizadas/', views.VentasRealizadas, name='VentasRealizadas'),
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
