from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_profile/<int:id>/', views.user_profile, name='user_profile'),
]