# Generated by Django 3.2.6 on 2021-08-23 00:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0011_auto_20210823_0011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='Profile',
        ),
    ]
