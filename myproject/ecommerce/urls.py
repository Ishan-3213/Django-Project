# Login
from django.urls import path
from django.conf.urls import url
from ecommerce import views
from .views import *                  

#Templates

app_name = 'ecommerce'

urlpatterns = [
    # path('', views.index,name = 'celery'),
    path('single_product/<int:id1>/', SingleProductView.as_view(), name="single_product"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('checkout/', CheckoutView.as_view(),name ='checkout'),
    path('category/',SingleProductView.category,name='category'),
    path('email/',CheckoutView.email_send, name='email_1'),
    path('', HomeView.as_view(),name = 'index'),
    path('item/', ProductListView.as_view(),name = 'item'),
    path('contact.html',SearchView.contact,name='contact'),
    path('login/',LoginView.as_view(),name='login_1'),
    path('registration/',Register.as_view(),name='registration'),
    path('search.html', SearchView.as_view(), name="search"),
    path('cart.html', CartItemView.cart, name='cart'),
    path('update_cart/',SingleProductView.updateitem,name='update_cart'),

]