# Generated by Django 2.0.3 on 2018-04-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180422_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]
