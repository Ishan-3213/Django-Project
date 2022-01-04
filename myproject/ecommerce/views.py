# Home page Using Templates
# from django.shortcuts import render
from django import template
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView
from . import models, task
from .task import *
from django.contrib.auth.forms import UserChangeForm
from ecommerce.models import User
from .models import Products, OrderItem, Customer, Order, Address
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib import messages
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponse
from ecommerce.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
# import json
from django.db.models import Q

my_list = []
check = True


class ProductListView(ListView):

    context_object_name = 'item'
    model = models.Products
    template_name = 'ecommerce/category.html'

class UserEditView(TemplateView):

    form_class = UserChangeForm
    template_name = 'ecommerce/edit_profile.html'
    success_url = reverse_lazy('index')

    def ger_object(self):
        return self.request.user

class HomeView(ListView):

    context_object_name = 'items'
    model = models.Products
    template_name = 'ecommerce/index.html'


class SingleProductView(View):


    def get(self, request, id1, *args, **kwargs):

        object_1 = get_object_or_404(models.Products, pk=id1)
        # products = models.Products.objects.filter(is_deleted=False).exclude(pk=id1).filter()
        return render(request, 'ecommerce/single_product.html', context={
            'object_1': object_1,
        })

    def ItemIndex(request):


        return render(request, 'ecommerce/index.html', {'items': Products.objects.all()})


    @login_required(login_url='ecommerce/login.html')
    def category(request):
        return render(request, 'ecommerce/category.html', {'item': Products.objects.all()})


    def updateitem(request):


        print('Enter the update')

        customer = models.Customer.objects.filter(user=request.user).first()
        print('Under the user', customer)

        item_id = request.POST.get('item_id')
        print('item_id', item_id)
        action = request.POST.get('action')
        print('action', action)

        item, created = Products.objects.get_or_create(id=item_id)
        print('item', item)

        order, created = Order.objects.get_or_create(customer=customer)
        # print('order', order)
        orderitem, created = OrderItem.objects.get_or_create(order=order, item=item)
        print(orderitem)
        print('above if')
        if action == "add":
            orderitem.quan = (orderitem.quan + 1)
            # if ((item.quantity >= orderitem.quan)):
            #     my_list.append(True)
            #     print(check)
            # else:
            #     my_list.append(False)
            # print(my_list)


        elif action == "remove":
            my_list.clear()
            orderitem.quan = (orderitem.quan - 1)
            # if (item.quantity >= orderitem.quan):
            #     my_list.append(True)
            #     print(my_list)
            # else:
            #     my_list.append(False)
            #     print(my_list)


        orderitem.save()
        print('action: ', action)
        print('item_id: ', item_id)
        return JsonResponse("item was added", safe=False)


    # def elements(request):
    #     return render(request, 'elements.html', {})

@login_required(login_url='ecommerce/login.html')
class CartItemView(TemplateView):
    def cart(request):

        print('enter the cart')

        customer = models.Customer.objects.filter(user=request.user).first()
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer)

        items = order.orderitem_set.all()
        print(items)
        
        context = {'items': items, 'order': order}
        return render(request, 'ecommerce/cart.html' , context=context)


    


class CheckoutView(View):


    # print("inside checkout view")


    def get(self, request, *args, **kwargs):
        print("inside get func")
        customer = models.Customer.objects.filter(user_id=request.user).first()
        order = Order.objects.get(customer=customer)
        # print('order', order)

        items = order.orderitem_set.all()
        address = models.Address.objects.filter(
            customer_Addresses__user_id=request.user).first()
        context = {'checkout': True,
                'customer': customer,
                'items': items,
                'address': address,
                'order': order}
        return render(request, 'ecommerce/checkout.html', context)


    # print("outside get func")


    def email_send(request, *args, **kwargs):
        print("inside post view")

        customer = Customer.objects.get(user_id=request.user.id)
        print(customer, 'customer')
        order, created = Order.objects.get_or_create(customer=customer)
        # print(order, 'order')
        carts = order.orderitem_set.all()

        # carts = models.OrderItem.objects.get(user=request.user)
        print('cart', carts)
        task.checkout_1(user_id=customer.id)
        context = {'carts': carts,
                'order': order}
        return render(request, 'ecommerce/confirmation.html', context)
    # print("outside post func")


class SearchView(ListView):

        # print("enter the search")
    model = Products
    template_name = 'ecommerce/search.html'
    context_object_name = 'products'
    # context_object_name = 'q'

    def get_queryset(self):
        print("enter the function")
        q = self.request.GET.get('q')
        print("getting q", q)
        products = Products.objects.filter(Q(prod_name__icontains=q))
        print('products', products)

        return products
        # return q


    # def send_mail_without_celery():
    #     send_mail('Sending Mail from Django-Celery','CELERY IS COOL',
    #                 'ishan.pansuirya@gmail.com',
    #                 ['ishanpansuriya.18.it@iite.indusuni.ac.in'],
    #                 fail_silently = False)
    #     return None

    # def index(request):
    #     send_mail_without_celery()
    #     return HttpResponse("<h1> Hello , From Celery</h1>")


    # LOGIN
    

    # Contact Page
    def contact(request):


        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            return render(request, 'ecommerce/contact.html', {'name': name})
        else:
            return render(request, 'ecommerce/contact.html', {})

   
    @login_required(login_url='ecommerce/login.html')
    def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'ecommerce/login.html', {})


    def post(self, request, *args, **kwargs):
        try:
            print("inside user_login func")
            print("Entering Username nd Password")
            username = request.POST.get('username')
            password = request.POST.get('password')

            print("Checking Username nd Password")

            user = authenticate(username=username, password=password)
            print("user", user)
            token, created = Token.objects.get_or_create(user=user)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))

                else:
                    return HttpResponse("Account not active")

        except Exception as e:
            messages.add_message(request, messages.INFO, "Please Enter Valid Username or Password")
            return render(request, 'ecommerce/login.html', {})
      



class Register(TemplateView):
    form_class_1 = UserForm
    form_class_2 = UserProfileInfoForm
    template_name = 'ecommerce/registration.html'

    def get(self, request, *args, **kwargs):
        form_U = self.form_class_1()
        form_P = self.form_class_2()

        return render(request, self.template_name, {'form_U': form_U, 'form_P': form_P})

    def post(self, request, *args, **kwargs):
        print("Entering post")

        form_U = self.form_class_1(request.POST)
        form_P = self.form_class_2(request.POST)
        print("Geting forms")
        print("cheking forms....")
        try: 
            if form_U.is_valid() and form_P.is_valid():
                print("form is valid")
                user = form_U.save()
                user.set_password(user.password)

                user.save()
                print("cheking profile pic")
                profile = form_P.save(commit=False)
                profile.user = user
                if 'profile_pic' in request.FILES:
                    print('Found It!')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                print("rofile pic is valid")
                registered = True
                # return HttpResponse('index')
                # return redirect(HomeView)
                return render(request, 'ecommerce/login.html', {})
                # return HttpResponseRedirect('index')
            else:
                print(form_U.errors, form_P.errors)

        except Exception as e:
            messages.add_message(request, form_U.errors and form_P.errors, "Please Enter Valid Username or Password")
            return render(request, 'ecommerce/registration.html', {})
      

        


    # def register(request):
    #     registered = False
    #     if request.method == "POST":
    #         user_form = UserForm(data=request.POST)
    #         profile_form = UserProfileInfoForm(data=request.POST)

    #         if user_form.is_valid() and profile_form.is_valid():   

    #         else:
    #             print(user_form.errors, profile_form.errors)

    #     else:
    #         user_form = UserForm()
    #         profile_form = UserProfileInfoForm()

    #     return render(request, 'ecommerce/registration.html',
    #                 {'user_form': user_form,
    #                 'profile_form': profile_form,
    #                 'registered': registered})


   