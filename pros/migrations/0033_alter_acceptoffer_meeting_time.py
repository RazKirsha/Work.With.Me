# Generated by Django 3.2.4 on 2021-06-22 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pros', '0032_alter_acceptoffer_meeting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptoffer',
            name='meeting_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 13, 35, 7, 965498)),
        ),
    ]
