# Generated by Django 3.2.4 on 2021-06-17 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_profile_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 12, 38, 51, 16411)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]