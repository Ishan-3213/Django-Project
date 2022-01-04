from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django_countries.fields import CountryField
# from datetime import datetime
from django.utils import timezone
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.

# Shipping add...


class Address(models.Model):

    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField(default="380015")
    address_type = models.CharField(max_length=1)
    default = models.BooleanField(default=False)

    def __str__(self):
        return str(self.address_1) + " " + str(self.address_2)

    class Meta:
        verbose_name_plural = "Addresses"



class Customer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_user')

    # Additional
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(upload_to="profile_pic", blank=True)
    mobile_no = PhoneNumberField(blank=True,)
    alternate_mobile_no = PhoneNumberField(blank=True,)
    address = models.ManyToManyField(Address, related_name='customer_Addresses')
    # related_name = "profile_address"

    def __str__(self):
        return self.user.username


# class User1(models.Model):
#     username = models.OneToOneField(Customer,on_delete=models.CASCADE,
#                                      null=True, blank=True)
#     email = models.CharField(max_length=200, null=True)



# Products
class Products(models.Model):
    prod_name = models.CharField(max_length=200)
    prod_details = models.TextField()
    prod_price = models.FloatField(null=False)
    prod_discount_price = models.FloatField(blank=True, null=True)
    prod_img = models.ImageField(upload_to="ecommerce/", 
                                    default="ecommerce/p1.jpg", null=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)


    def __str__(self):
        return self.prod_name

    @property
    def imageURL(self):
        try:
            url = self.prod_img.url
        except:
            url = ''
        return url



class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)

    ordered = models.BooleanField(default=False)
    shipping_address = models.ManyToManyField(Address,
                                             related_name="shipping_address")

    # start_date = models.DateTimeField(default = timezone.now,blank=True, null=True)
    # ordered_date = models.DateTimeField(default = timezone.now,blank=True, null=True)

    def __str__(self):
        return self.customer

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total_1 = sum([items.get_total for items in orderitems]) 
        total = total_1 + int(0.18 * total_1)
        return total


CHOICE = (('0', 'No'),
          ('1', 'Yes'),
          )


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)

    purchased = models.CharField(max_length=5, choices=CHOICE, default='0')
    quan = models.IntegerField(default=0,null=True,blank=True)


    def __str__(self):
        return f"{self.quan} of {self.item.prod_name}"

    @property
    def get_total(self):
        total = self.item.prod_price * self.quan
        return total


@receiver(post_save, sender=Customer)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance.user)
