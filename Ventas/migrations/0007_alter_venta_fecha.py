# Generated by Django 3.2.4 on 2021-07-14 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0006_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 13, 2, 3, 356936)),
        ),
    ]
