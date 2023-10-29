from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import registros_usuarios
from .models import roles
from .models import Carrito, Venta
from .models import Productos
from .models import Login

# Create your views here.
def home(request): #aqui empiezan las rutas como el index
    return render(request, 'homepage\home.html') 

def CarritoCompras(request, product_id): 
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create()
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return render(request, 'homepage\carritoCompras.html')    

def catalogo(request): 
    productos = Productos.objects.all()
    return render(request, 'homepage\catalogo.html', {'productos': productos})  

@login_required
def Compra(request): 
    return render(request, 'homepage\compra.html')

def contacto(request): 
    return render(request, 'homepage\contacto.html')

def Dashboard(request): 
    return render(request, 'homepage\dashboard.html')

def GenerarPedido(request): 
    return render(request, 'homepage\generarPedido.html')   

def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
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
    if request.method == 'POST':
        carrito = Carrito.objects.get(usuario=request.user)
        venta = Venta(carrito=carrito)
        venta.save()
        carrito.productos.clear()
        return redirect('homepage\pedidoRealizado.html')
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