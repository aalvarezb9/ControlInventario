# Generated by Django 3.2.4 on 2021-07-14 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0016_auto_20210714_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 34, 2, 773934)),
        ),
    ]
