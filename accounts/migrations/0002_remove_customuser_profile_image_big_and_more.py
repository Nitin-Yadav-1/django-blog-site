# Generated by Django 5.0.6 on 2024-07-02 12:02

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image_big',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image_small',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='profile_image/default.jpeg', force_format=None, keep_meta=False, quality=-1, scale=None, size=(300, 300), upload_to='profile_image/'),
        ),
    ]
