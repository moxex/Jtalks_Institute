from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jtalks-home'),
    path('about/', views.about, name='jtalks-about'),
]