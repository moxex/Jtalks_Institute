# Generated by Django 3.2.9 on 2021-12-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_about_title_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('support', models.CharField(max_length=100)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.TextField(help_text='Write Your Message, not more than 1000 characters', max_length=1000)),
            ],
        ),
    ]
