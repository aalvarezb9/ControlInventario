# Generated by Django 3.2.4 on 2021-07-12 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_alter_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='registrado_por',
        ),
    ]