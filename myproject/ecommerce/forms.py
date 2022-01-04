from django import forms
from django.contrib.auth.models import User
from .models import Customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields= ('email','profile_pic','mobile_no','alternate_mobile_no')