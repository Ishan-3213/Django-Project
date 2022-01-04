from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.http.response import Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db.models import *
from . import models
from .models import Products, OrderItem, Customer, Order, Address
from time import sleep



# @shared_task
# def send_mail_task():
    # send_mail('CELERY WORKED',"CELERY IS COOL",
    #             'ishan.pansuirya@gmail.com'
    #             ['ishanpansuriya.18.it@iite.indusuni.ac.in'],
    #             fail_silently = False)
    # return None

def checkout_1(user_id):
    print('inside the task')
    print(user_id, "user_id")
    customer = models.Customer.objects.get(pk=user_id)
    # customer = Customer.objects.get_or_create(pk=user_id)
    print('customer',customer)
    order, created = Order.objects.get_or_create(customer=user_id)
    # print('order',order)

    carts = order.orderitem_set.all()
    
    print(carts,'carts')
    purchased = '0'
    data = list()
    subtotal = 0
    for cart in carts:
        cart_dict = dict()
        cart_dict['name'] = cart.item.prod_name
        cart_dict['quan'] = cart.quan
        if cart.quan > cart.item.quantity:
            cart_dict['Price'] = "Sorry this product is out of stock..!! <(＿　＿)>"
        else:
            cart_dict['Price'] = cart.item.prod_price * cart.quan
            subtotal = subtotal + cart.item.prod_price * cart.quan
            cart.purchased = '1'
            cart.save()
            cart.item.quantity = cart.item.quantity - cart.quan
            cart.item.save()
        data.append(cart_dict)
    tax = subtotal * 0.18
    tax = "%.2f" % tax
    total = float(tax) + subtotal
    print('total',total)
    subject = "Order Confirmation Status"
    template_str = 'ecommerce/mail.html'
    print(data,'data')
    html_message = render_to_string(template_str, {"data": data, "subtotal": subtotal, "tax": tax, "total": total})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    print(from_email,'from_mail')
    # print("To mail", customer.customer_id.email)
    send_mail(subject, plain_message, from_email, ["ishan18112000@gmail.com"], html_message=html_message)

   