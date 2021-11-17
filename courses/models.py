from django.db import models
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('courses:course_list_by_category', args=[self.slug])
    
    def __str__(self):
        return self.name


class Courses(models.Model):
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    overview = models.TextField()
    cover = models.ImageField(blank=True, null=True, upload_to="courses_cover/")
    slug = models.SlugField()

    # Courses content
    content_url = models.URLField(blank=True, null=True)
    content_file = models.FileField(blank=True, null=True)
    tutor = models.CharField(max_length=100, blank=True, null=True)
    tutor_image = models.ImageField(blank=True, null=True, upload_to="course_tutor")
    tutor_title = models.CharField(max_length=100, blank=True, null=True)

    # What you will learn


    price = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[self.id, self.slug])

    def price_display(self):
        return "{0:.2f}".format (self.price / 100)

