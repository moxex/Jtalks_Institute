from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


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
        about_us = request.POST['about_us']
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
                                 location=location, phone_number=phone_number, about_us=about_us,
                                 referral=referral, photo=photo, gender=gender)
        user = User.objects.get(username=username)
        context = {
            'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name,
            'location': location, 'phone_number': phone_number, 'referral': referral, 'photo': user.photo,
            'gender': gender, 'about_us': about_us
        }
        return render(request, 'users/signup_success.html', context)
    return render(request, 'users/signup.html')


# login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'This Username, ' + username + ', Does Not Exist...')
            return render(request, 'users/login.html')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
    return render(request, 'users/login.html')


# logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# user Profile
def user_profile(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'users/user_profile.html', {'user': user})
