# Generated by Django 3.2.4 on 2021-06-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default='Hello Worldie', max_length=1000),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
