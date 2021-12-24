# Generated by Django 3.2.9 on 2021-12-22 12:52

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_pdf',
            field=models.FileField(blank=True, null=True, upload_to=courses.models.pdf_directory),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_video',
            field=models.FileField(blank=True, null=True, upload_to=courses.models.video_directory),
        ),
    ]
