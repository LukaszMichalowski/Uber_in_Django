from django.contrib import admin
from .models import Client, Destination


@admin.register(Client)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','surname','created', 'updated']


@admin.register(Destination)
class ClientAdmin(admin.ModelAdmin):
    list_display=['destination','order_date','client']

