# Generated by Django 2.1.1 on 2018-09-29 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20180928_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operadores',
            options={'managed': False, 'permissions': (('view_operador', 'View Operador'),), 'verbose_name': 'Operador', 'verbose_name_plural': 'Operadores'},
        ),
    ]
