# Generated by Django 3.2.4 on 2021-06-17 11:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_auto_20210617_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 14, 37, 40, 959680)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]