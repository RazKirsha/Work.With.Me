# Generated by Django 3.2.4 on 2021-06-18 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pros', '0024_auto_20210618_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptoffer',
            name='meeting_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 19, 0, 30, 26, 436526)),
        ),
    ]
