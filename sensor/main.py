import time
from locust import task
from locust.contrib.fasthttp import FastHttpUser

class Sensor(FastHttpUser):
    host = "http://192.168.64.175:8000/"

    @task
    def send_data(self):
        self.client.post("sensors/", data={"payload": 2})
