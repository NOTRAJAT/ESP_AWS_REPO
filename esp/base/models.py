from turtle import update
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class esp(models.Model):
    state = models.BooleanField()
    analog = models.IntegerField(default=0)

    def __str__(self):
        return str(self.analog)
