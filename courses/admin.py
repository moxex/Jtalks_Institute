from django.contrib import admin
from .models import Category, Courses, CourseReview, UserLibrary


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'available', 'created', 'updated', 'is_featured']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'review_text', 'get_review_rating')


admin.site.register(CourseReview, CourseReviewAdmin)


admin.site.register(Category)


class UserLibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid', 'reference_id', 'order_id', 'payment_date']


admin.site.register(UserLibrary, UserLibraryAdmin)

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
