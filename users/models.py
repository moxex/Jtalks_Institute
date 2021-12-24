from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
# from courses.models import Courses

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='admin_pics/%Y/%m/%d/', null=True)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)
    location = models.CharField(max_length=50, blank=True)
    
    Here_about_us = [
        ('W', 'WhatsApp'), 
        ('F', 'Facebook'), 
        ('T', 'Twitter'), 
        ('I', 'Instagram'), 
        ('Y', 'YouTube'), 
        ('B', 'Blog')
    ]
    about_us = models.CharField(choices=Here_about_us, max_length=20, blank=True)
    referral = models.CharField(max_length=50, default="Referral Name", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD = "email"

    # REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} {self.email}'

# @receiver(post_save, sender=User)
# def created_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
    

# # Users Library
# class UserLibrary(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='library')
#     courses = models.ManyToManyField(Courses, blank=True)

#     class Meta:
#         verbose_name_plural = "UserLibraries"

#     def __str__(self):
#         return self.user.email

