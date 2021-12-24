from django.urls import path
from . import views

app_name = 'jtalks'

urlpatterns = [
    path('', views.home, name='jtalks-home'),
    path('about/', views.about, name='jtalks-about'),
    path('get_courses/', views.GetCourses.as_view(), name='get_courses'),
    path('load-more-data/', views.load_more_data, name='load_more_data'),
    path('load_more_products/', views.load_more_products, name='load_more_products'),
    path('search_more_products/', views.search_more_products, name='search_more_products'),
    path('search_products/', views.search_products, name='search_products')
]