# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Buses(models.Model):
    id_tipo_buses = models.ForeignKey('TipoBuses', models.DO_NOTHING, db_column='id_tipo_buses')
    id_empresas = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresas')
    id_trayectos = models.ForeignKey('Trayectos', models.DO_NOTHING, db_column='id_trayectos')
    id_operadores = models.ForeignKey('Operadores', models.DO_NOTHING, db_column='id_operadores')
    id_lectores = models.ForeignKey('Lectores', models.DO_NOTHING, db_column='id_lectores')
    id_lineas = models.ForeignKey('Lineas', models.DO_NOTHING, db_column='id_lineas')
    chapa = models.CharField(unique=True, max_length=12)
    coche_numero = models.IntegerField()
    observaciones = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buses'
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
    #def __str__(self):
        #return self.coche_numero
    def __str__(self):
        return str(self.coche_numero) if self.coche_numero else ''


class Comprobantes(models.Model):
    id_timbrados = models.ForeignKey('Timbrados', models.DO_NOTHING, db_column='id_timbrados')
    num_doc = models.CharField(unique=True, max_length=20)
    id_lectores = models.ForeignKey('Lectores', models.DO_NOTHING, db_column='id_lectores')
    id_mov = models.ForeignKey('Movimientos', models.DO_NOTHING, db_column='id_mov')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'comprobantes'
        verbose_name = 'Comprobante'
        verbose_name_plural = 'Comprobantes'
    def __str__(self):
        return self.num_doc


class DetallesComprobantes(models.Model):
    id_comp = models.ForeignKey(Comprobantes, models.DO_NOTHING, db_column='id_comp')
    id_tarjetas = models.ForeignKey('Tarjetas', models.DO_NOTHING, db_column='id_tarjetas')
    id_tipopago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tipopago', blank=True, null=True)
    cantidad = models.IntegerField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'detalles_comprobantes'
        


class Empresas(models.Model):
    nombre_razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=150)
    actividad_economica = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'empresas'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_razon_social

class Lectores(models.Model):
    serie = models.CharField(max_length=20)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lectores'
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
     
    def __str__(self):
        return str(self.serie)
    

class Lineas(models.Model):
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lineas'
        verbose_name = 'Linea'
        verbose_name_plural = 'Lineas'
    
    def __str__(self):
        return str(self.numero)

class Movimientos(models.Model):
    tipo_movimiento = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'movimientos'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
    def __str__(self):
        return self.tipo_movimiento

class Operadores(models.Model):
    id_personas = models.ForeignKey('Personas', models.DO_NOTHING, db_column='id_personas')
    id_empresas = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresas')

    class Meta:
        managed = False
        db_table = 'operadores'
        verbose_name = 'Operador'
        verbose_name_plural = 'Operadores'
        permissions = {
            ('view_oper', 'View Operadores')
        }

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

class Sucursales(models.Model):
    id_empresas = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresas')
    id_lectores = models.ForeignKey(Lectores, models.DO_NOTHING, db_column='id_lectores')
    nombre = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    contacto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursales'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
    def __str__(self):
        return str(self.id_empresas) if self.id_empresas else ''

class Tarjetas(models.Model):
    uid = models.CharField(max_length=16)
    fecha_expedicion = models.DateField()
    fecha_vencimiento = models.DateField()
    estado = models.IntegerField()
    saldo_actual = models.DecimalField(max_digits=12, decimal_places=0)
    id_tipo_tarjetas = models.ForeignKey('TipoTarjeta', models.DO_NOTHING, db_column='id_tipo_tarjetas')

    class Meta:
        managed = False
        db_table = 'tarjetas'
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
    def __str__(self):
        return self.uid

class Timbrados(models.Model):
    numero = models.IntegerField()
    valido_desde = models.DateField()
    valido_hasta = models.DateField()
    num_doc_ini = models.CharField(max_length=20)
    num_doc_fin = models.CharField(max_length=20)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'timbrados'
        verbose_name = 'Timbrado'
        verbose_name_plural = 'Timbrados'
    def __str__(self):
        return str(self.numero)

class TipoBuses(models.Model):
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_buses'
        verbose_name = 'Tipo Bus'
        verbose_name_plural = 'Tipo Buses'

    def __str__(self):
        return self.descripcion

class TipoPago(models.Model):
    nro_boleta = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_pago'
        verbose_name = 'Tipo Pago'
        verbose_name_plural = 'Tipo Pagos'
    def __str__(self):
        return self.nro_boleta

class TipoTarjeta(models.Model):
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'
        verbose_name = 'Tipo Tarjeta'
        verbose_name_plural = 'Tipo Tarjetas'
    def __str__(self):
        return self.descripcion

class Trayectos(models.Model):
    ramal = models.CharField(max_length=30)
    itinerario_ida = models.CharField(max_length=500)
    itinerario_vuelta = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'trayectos'
        verbose_name = 'Trayecto'
        verbose_name_plural = 'Trayectos'
    def __str__(self):
        return self.ramal

