from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Courses

# # Create your views here.
# class CourseListView(generic.ListView):
#     template_name = "jtalks/categories.html",
#     template_name = "jtalks/course.html"
#     queryset = Courses.objects.all()

# class CourseDetailView(generic.ListView):
#     template_name = "jtalks/course-inner.html",
#     queryset = Courses.objects.all()


def course_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Courses.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = courses.filter(category=category)
    return render(request,'courses/content/list.html', {'category': category, 'categories': categories, 'courses': courses})

def course_detail(request, id, slug):
    course = get_object_or_404(Courses, id=id, slug=slug, available=True)
    return render(request, 'courses/content/detail.html', {'course': course})