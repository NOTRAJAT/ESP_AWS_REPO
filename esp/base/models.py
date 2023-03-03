import imp
from turtle import update
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.


class esp(models.Model):
    state = models.IntegerField(default=0)
    analog = models.IntegerField(default=0)

    def __str__(self):
        return str(self.analog)
