from django.contrib.auth import forms
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import Group, User
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
# from .decorators import unauthorised_user

User = get_user_model()

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        location = request.POST['location']
        phone_number = request.POST['phone_number']
        referral = request.POST['referral']
        photo = request.FILES['photo']
        password = request.POST['password']
        password2 = request.POST['password2']

        # username validation
        check_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root', 'email',
                       'user', 'join', 'sql', 'static', 'python', 'delete', 'sex', 'sexy']

        if username in check_users:
            messages.error(request, 'Your Username, ' + username + ', Is Not Acceptable. Please Use Another Username')
            return render(request, 'users/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Your Username, ' + username + ', Already Exists. Please Try Another Username')
            return render(request, 'users/signup.html')

        # email validation
        email = email.strip().lower()
        if ("@" not in email) or (email[-4:] not in ".com.org.edu.gov.net"):
            messages.error(request, 'Your Email, ' + email + ', Is Invalid!!!')
            return render(request, 'users/signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Your Email, ' + email + ', Already Exists. Please Try Another Email')
            return render(request, 'users/signup.html')

        # password validation
        if password != password2:
            messages.error(request, "Your Passwords Don't match")
            return render(request, 'users/signup.html')

        User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,
                                 location=location, phone_number=phone_number,
                                 referral=referral, photo=photo,
                                gender=gender)
        user = User.objects.get(username=username)
        context = {
            'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name,
            'location': location, 'phone_number': phone_number, 'referral': referral, 'photo': user.photo,
            'gender': gender
        }
        return render(request, 'users/signup_success.html', context)
    return render(request, 'users/signup.html')



