# Generated by Django 4.0.6 on 2022-08-07 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': True, 'verbose_name': 'Customer', 'verbose_name_plural': 'Customer'},
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
    ]
