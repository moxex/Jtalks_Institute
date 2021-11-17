"""jtalks_institute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from courses.views import CourseListView
from users.views import user_signup
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jtalks.urls')),
    # path("categories/", CourseListView.as_view(), name='category'),
    # path("course/", CourseListView.as_view(), name='courses'),
    # path("c/", include("courses.urls", namespace="courses")),
    path('signup/', user_signup, name='signup'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('course/', include('courses.urls', namespace='courses')),
    # path('signup/', include('signup.urls'), name='signup'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
