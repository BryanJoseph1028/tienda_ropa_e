from django.contrib import admin
from .models import registros_usuarios
from .models import roles
from .models import Login
from .models import Categoria
from .models import Productos 
from .models import Carrito
from .models import ItemCarrito
from .models import PedidoRealizado
from .models import Venta
# Register your models here.

admin.site.register(registros_usuarios),

admin.site.register(roles),

admin.site.register(Login),

admin.site.register(Categoria),

admin.site.register(Productos),

admin.site.register(Carrito),

admin.site.register(ItemCarrito),

admin.site.register(PedidoRealizado),

admin.site.register(Venta),









