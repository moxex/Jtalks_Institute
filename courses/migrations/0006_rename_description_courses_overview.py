# Generated by Django 3.2.9 on 2021-11-16 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211115_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='description',
            new_name='overview',
        ),
    ]