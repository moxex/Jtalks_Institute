# Generated by Django 3.2.9 on 2022-03-06 19:50

import courses.models
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=160)),
                ('review_rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=150)),
                ('rated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='courses_cover/')),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('course_pdf', models.FileField(blank=True, null=True, upload_to=courses.models.pdf_directory)),
                ('course_video', models.FileField(blank=True, null=True, upload_to=courses.models.video_directory)),
                ('content_url', models.URLField(blank=True, null=True)),
                ('tutor', models.CharField(blank=True, max_length=100, null=True)),
                ('tutor_image', models.ImageField(blank=True, null=True, upload_to='course_tutor')),
                ('tutor_title', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='UserLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('reference_id', models.CharField(blank=True, max_length=200, null=True)),
                ('order_id', models.CharField(blank=True, default=products.models.random_code, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('courses', models.ManyToManyField(to='courses.Courses')),
            ],
            options={
                'verbose_name_plural': 'UserLibraries',
                'ordering': ('id',),
            },
        ),
    ]
