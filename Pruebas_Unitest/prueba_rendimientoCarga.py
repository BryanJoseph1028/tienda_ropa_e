import unittest
from locust import HttpUser, task, between
from selenium import webdriver
import time

class TestPageLoadTime(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Puedes usar otro navegador si lo prefieres

    def tearDown(self):
        self.driver.quit()

    def measure_page_load_time(self, url):
        start_time = time.time()
        self.driver.get(url)
        end_time = time.time()
        page_load_time = end_time - start_time
        return page_load_time

    def test_home_page_load_time(self):
        home_url = "C:\Users\bryan\Desktop\tienda_ropa\tienda_website_project\homepage\templates\homepage\home.html"  # Reemplaza con la URL de tu página principal
        home_page_load_time = self.measure_page_load_time(home_url)
        print(f"Tiempo de carga de la página principal: {home_page_load_time} segundos")

    def test_product_page_load_time(self):
        product_url = "C:\Users\bryan\Desktop\tienda_ropa\tienda_website_project\homepage\templates\homepage\catalogo.html"  # Reemplaza con la URL de un producto en tu tienda
        product_page_load_time = self.measure_page_load_time(product_url)
        print(f"Tiempo de carga de la página de producto: {product_page_load_time} segundos")

if _name_ == "_main_":
 unittest.main()