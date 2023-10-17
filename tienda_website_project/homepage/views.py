from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import registros_usuarios

# Create your views here.
def home(request): #aqui empiezan las rutas como el index
    return render(request, 'homepage\home.html') 

def CarritoCompras(request): 
    return render(request, 'homepage\carritoCompras.html')    

def catalogo(request): 
    return render(request, 'homepage\catalogo.html')  

@login_required
def Compra(request): 
    return render(request, 'homepage\compra.html')

def contacto(request): 
    return render(request, 'homepage\contacto.html')

@login_required
def Dashboard(request): 
    return render(request, 'homepage\dashboard.html')

@login_required
def GenerarPedido(request): 
    return render(request, 'homepage\generarPedido.html')   

def login(request): 
    return render(request, 'homepage\login.html')

def logout(request):
    return render(request, 'homepage\logout.html')

def ofertas(request): 
    return render(request, 'homepage\ofertas.html')

def ProductoDetalle(request): 
    return render(request, 'homepage\productoDetalle.html')  

@login_required
def Proveedores(request): 
    return render(request, 'homepage\Proveedores.html')

@login_required
def PedidoRealizado(request): 
    return render(request, 'homepage\pedidoRealizado.html')

def RecuperacionContrasena(request): 
    return render(request, 'homepage\RecuperacionContrasena.html')    

def RegistrosUsuarios(request): 
    return render(request, 'homepage\RegistrosUsuarios.html')

@login_required
def Roles(request): 
    return render(request, 'homepage\Roles.html')

@login_required
def VentasRealizadas(request): 
    return render(request, 'homepage\VentasRealizadas.html')     