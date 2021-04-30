from django.db import models

# Create your models here.
class Sensor(models.Model):
    payload = models.IntegerField('payload', default=0)
    datetime = models.DateTimeField(auto_now_add=True)

