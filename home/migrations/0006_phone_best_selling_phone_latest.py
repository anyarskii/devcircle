# Generated by Django 4.0.6 on 2022-07-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_phone_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='best_selling',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='latest',
            field=models.BooleanField(default=True),
        ),
    ]