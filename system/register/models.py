# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Empresas(models.Model):
    nombre_razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'empresas'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_razon_social




class Operadores(models.Model):
    id_personas = models.ForeignKey('Personas', models.DO_NOTHING, db_column='id_personas')
    id_empresas = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresas')


    class Meta:
        managed = False
        db_table = 'operadores'
        verbose_name = 'Operador'
        verbose_name_plural = 'Operadores'

    def __str__(self):
        return str(self.id_personas) if self.id_personas else ''


class Personas(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=150)
    fecha_nac = models.DateField()

    class Meta:
        managed = False
        db_table = 'personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nombres