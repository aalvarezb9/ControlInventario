# Generated by Django 3.2.4 on 2021-07-12 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 12, 16, 2, 57, 393499)),
        ),
    ]