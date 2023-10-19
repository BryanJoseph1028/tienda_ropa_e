from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import login
from .models import login
from .models import Product, Cart, CartItem
# Create your tests here.

class LoginTestCase(TestCase):
    def setUp(self):
        # Crear un usuario para probar el inicio de sesión
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_view(self):
        # Simular una solicitud POST de inicio de sesión exitosa
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # 302 indica redirección exitosa después del inicio de sesión
        self.assertRedirects(response, reverse('inicio'))

        # Verificar que el usuario está autenticado después del inicio de sesión
        self.assertTrue(response.wsgi_request.user.is_authenticated)

        # Simular una solicitud POST de inicio de sesión fallida
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # 200 indica una respuesta exitosa pero sin redirección

        # Verificar que el usuario no está autenticado después de un intento de inicio de sesión fallido
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        
        
        
class ShoppingCartTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Producto de prueba', price='10.00')

    def test_add_to_cart(self):
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # 302 indica redirección exitosa

        cart = Cart.objects.get()
        self.assertEqual(cart.items.count(), 1)

        cart_item = CartItem.objects.get(product=self.product, cart=cart)
        self.assertEqual(cart_item.quantity, 1)

    def test_add_to_cart_existing_item(self):
        # Agregar un producto al carrito
        self.client.get(reverse('add_to_cart', args=[self.product.id]))

        # Agregar el mismo producto nuevamente al carrito
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # 302 indica redirección exitosa

        cart = Cart.objects.get()
        self.assertEqual(cart.items.count(), 1)

        cart_item = CartItem.objects.get(product=self.product, cart=cart)
        self.assertEqual(cart_item.quantity, 2)