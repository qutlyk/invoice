# Generated by Django 2.1 on 2018-08-21 06:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0011_department_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]