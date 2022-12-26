from locust import HttpUser, between, task

class HelloTest(HttpUser):
    @task
    def home(self):
        self.client.get('/')
