# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Buses(models.Model):
    id_tipobuses = models.ForeignKey('TipoBuses', models.DO_NOTHING, db_column='id_tipobuses')
    id_empresas = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresas')
    id_trayectos = models.ForeignKey('Trayectos', models.DO_NOTHING, db_column='id_trayectos')
    id_operador = models.ForeignKey('Operadores', models.DO_NOTHING, db_column='id_operador')
    id_lectores = models.ForeignKey('Lectores', models.DO_NOTHING, db_column='id_lectores')
    id_lineas = models.ForeignKey('Lineas', models.DO_NOTHING, db_column='id_lineas')
    chapa = models.CharField(unique=True, max_length=12)
    coche_numero = models.IntegerField()
    observaciones = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buses'


class Caja(models.Model):
    id = models.IntegerField(primary_key=True)
    numero = models.CharField(max_length=45)
    id_empresas = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresas')
    id_lectores = models.ForeignKey('Lectores', models.DO_NOTHING, db_column='id_lectores')

    class Meta:
        managed = False
        db_table = 'caja'


class Comprobantes(models.Model):
    numero = models.IntegerField()
    id_timbrados = models.ForeignKey('Timbrados', models.DO_NOTHING, db_column='id_timbrados')
    id_buses = models.ForeignKey(Buses, models.DO_NOTHING, db_column='id_buses')
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja')
    num_doc = models.CharField(max_length=20)
    monto_a_pagar = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'comprobantes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class GuardianGroupobjectpermission(models.Model):
    object_pk = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'guardian_groupobjectpermission'
        unique_together = (('group', 'permission', 'object_pk'),)


class GuardianUserobjectpermission(models.Model):
    object_pk = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'guardian_userobjectpermission'
        unique_together = (('user', 'permission', 'object_pk'),)


class Lectores(models.Model):
    serie = models.CharField(max_length=20)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lectores'


class Lineas(models.Model):
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lineas'


class Movimientos(models.Model):
    tipo_movimiento = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Operadores(models.Model):
    id_personas = models.ForeignKey('Personas', models.DO_NOTHING, db_column='id_personas')
    id_empresas = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresas')

    class Meta:
        managed = False
        db_table = 'operadores'


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


class TarjetasHasComprobantes(models.Model):
    id_comp = models.ForeignKey(Comprobantes, models.DO_NOTHING, db_column='id_comp')
    id_tarjetas = models.ForeignKey(Tarjetas, models.DO_NOTHING, db_column='id_tarjetas')
    id_movimientos = models.ForeignKey(Movimientos, models.DO_NOTHING, db_column='id_movimientos')
    id_tipo_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tipo_pago')
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'tarjetas_has_comprobantes'


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


class TipoBuses(models.Model):
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_buses'


class TipoPago(models.Model):
    nro_boleta = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class TipoTarjeta(models.Model):
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'


class Trayectos(models.Model):
    ramal = models.CharField(max_length=30)
    itinerario_ida = models.CharField(max_length=500)
    itinerario_vuelta = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'trayectos'
