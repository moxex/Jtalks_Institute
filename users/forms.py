from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import fields, widgets

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
        # widgets = {
        #     'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}),
        #     'email': forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
        #     'referral': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Who Referred You'}),
        #     'gender': forms.MultipleChoiceField(widget=forms.SelectMultiple(GENDER)),
        #     'about_us': forms.MultipleChoiceField(widget=forms.SelectMultiple(Here_about_us)),
        #     'about_me': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell Us Something About Yourself (not more than 300 words)...'}),

        # }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username', 'first_name', 'last_name', 'email', 'gender',
#             'referral', 'location', 'phone_number', 'photo',
#             'about_me'
#         ]
#         widgets = {
#             'username': forms.TextInput(attrs={'readonly': 'readonly'}),
#             'code_number': forms.TextInput(attrs={'readonly': 'readonly'})
#         }