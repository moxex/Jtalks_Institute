from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import fields, widgets
from .models import ContactUs

User = get_user_model

GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

Here_about_us = [
        ('W', 'WhatsApp'), 
        ('F', 'Facebook'), 
        ('T', 'Twitter'), 
        ('I', 'Instagram'), 
        ('Y', 'YouTube'), 
        ('B', 'Blog')
    ]

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'phone_number', 
            'about_us', 'photo', 'referral', 'gender', 'password1', 'password2'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"