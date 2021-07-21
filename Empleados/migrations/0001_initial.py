# Generated by Django 3.2.4 on 2021-07-12 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(max_length=30)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('numero_de_identidad', models.CharField(max_length=20, unique=True)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('salario', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.rol')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.sexo')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
            },
        ),
    ]
