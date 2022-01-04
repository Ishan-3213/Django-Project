from django.contrib import admin
from ecommerce.models import Customer,User
from ecommerce.models import *

# Register your models here.
# admin.site.register(stock)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(OrderItem)
admin.site.register(Address)