# Generated by Django 4.0.6 on 2022-08-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.CharField(max_length=50),
        ),
    ]
