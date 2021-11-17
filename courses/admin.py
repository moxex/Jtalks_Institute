from django.contrib import admin
from .models import Category, Courses

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}


# @admin.register(Courses)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price', 'created', 'updated']
#     list_filter = ['created', 'updated']
#     list_editable = ['price']
#     prepopulated_fields = {'slug': ('name',)}


