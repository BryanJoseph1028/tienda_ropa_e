from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre las solicitudes (en segundos)

    @task
    def load_home_page(self):
        self.client.get("/homepage/templates/homepage/home.html")

    @task
    def load_product_page(self):
        self.client.get("/homepage/templates/homepage/catalogo.html")

if __name__ == "__main__":
    import os
    os.system("locust -f locust.py")