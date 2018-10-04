# Generated by Django 2.1.1 on 2018-10-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20180930_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallesComprobantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('monto_pagado', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'detalles_comprobantes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('contacto', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sucursales',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='buses',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='comprobantes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='empresas',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lectores',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lineas',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='movimientos',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='operadores',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='personas',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tarjetas',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='timbrados',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tipobuses',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tipopago',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tipotarjeta',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='trayectos',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='comprobantes',
            table='comprobantes',
        ),
    ]