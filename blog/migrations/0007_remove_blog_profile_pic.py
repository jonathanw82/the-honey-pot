# Generated by Django 3.0.6 on 2020-05-14 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='profile_pic',
        ),
    ]