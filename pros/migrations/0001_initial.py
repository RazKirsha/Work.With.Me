# Generated by Django 3.2.4 on 2021-06-15 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offers', '0003_rename_expired_offers_completed'),
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField(auto_now_add=True)),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offers.offers')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]
