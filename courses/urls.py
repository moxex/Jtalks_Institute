from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:id>/<slug:slug>/', views.course_detail, name='course_detail'),
    path('save_review/', views.SaveReview.as_view(), name='save_review'),
    path('load_more_review/', views.load_more_review, name='load_more_review'),
    path('create_user_library/', views.UserCourse.as_view(), name='user_library'),
    path('<str:username>/user_library/', views.user_library, name='user_library'),
    path('pay_for_courses/', views.AjaxCoursePayment.as_view(), name='pay_for_courses'),
    path('<int:id>/print_course_pdf', views.CoursePdf.as_view(), name='print_course_pdf'),
    path('search_more_courses/', views.search_more_courses, name='search_more_courses'),
    path('search_courses/', views.search_courses, name='search_courses')
]