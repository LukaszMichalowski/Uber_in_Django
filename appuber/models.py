from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    surname = models.CharField(max_length=255,db_index=True)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Client'
    def __str__(self):
        return self.name



class Destination(models.Model):
    destination = models.CharField(max_length=255,db_index=True)
    order_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client,related_name='destinations', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Destination'
    def __str__(self):
        return self.destination

