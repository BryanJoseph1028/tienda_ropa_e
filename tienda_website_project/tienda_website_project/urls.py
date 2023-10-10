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

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include('homepage.urls')),
    
    path('acccounts/', include('django.contrib.auth.urls')),
    
    path('login/', views.login, name='login'),#son las rutas
    
    path('RegistrosUsuarios/', views.RegistrosUsuarios, name='RegistrosUsuarios'),
    
    path('Carrito/', views.CarritoCompras, name='Carrito'),
    
    path('catalogo/', views.catalogo, name='catalogo'),
    
    path('productoDetalle/', views.ProductoDetalle, name='productoDetalle'),
    
    path('Dashboard/', views.Dashboard, name='Dashboard'),    
    
    path('GenerarPedido/', views.GenerarPedido, name='GenerarPedido'),
    
    path('PedidoRealizado/', views.PedidoRealizado, name='PedidoRealizado'),
    
    path('Proveedores/', views.Proveedores, name='proveedores'),
    
    path('RecuperacionContrasena/', views.RecuperacionContrasena, name='RecuperacionContrasena'),
    
    path('Roles/', views.Roles, name='Roles'),

    path('contacto/', views.contacto, name='contacto'),
    
    path('ofertas/', views.ofertas, name='ofertas'),
    
    path('VentasRealizadas/', views.VentasRealizadas, name='VentasRealizadas'),
    
    path ('logout/', views.logout, name='logout'),
    
    
    
    
]
