# Generated by Django 3.2.6 on 2021-08-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20210821_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]