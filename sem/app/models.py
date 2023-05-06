# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CargoEmp(models.Model):
    id_cargo_e = models.CharField(primary_key=True, max_length=25)
    nombre_cargo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cargo_emp'


class CargoEmpleado(models.Model):
    id_cargo_e = models.CharField(primary_key=True, max_length=25)
    nombre_cargo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cargo_empleado'


class Categoria(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=25)
    categoria = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'categoria'


class Comuna(models.Model):
    id_comuna = models.CharField(primary_key=True, max_length=25)  # The composite primary key (id_comuna, region_id_region) found, that is not supported. The first column is selected.
    comuna = models.CharField(max_length=30)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'comuna'
        unique_together = (('id_comuna', 'region_id_region'),)


class Credencial(models.Model):
    id_credencial = models.CharField(primary_key=True, max_length=25)
    user = models.CharField(max_length=25)
    pass_field = models.CharField(db_column='pass', max_length=25)  # Field renamed because it was a Python reserved word.
    tipo = models.CharField(max_length=25)
    emp_id_empleado = models.ForeignKey('Emp', models.DO_NOTHING, db_column='emp_id_empleado')
    emp_cargo_emp_id_cargo_e = models.ForeignKey('Emp', models.DO_NOTHING, db_column='emp_cargo_emp_id_cargo_e', to_field='cargo_emp_id_cargo_e', related_name='credencial_emp_cargo_emp_id_cargo_e_set')
    emp_id_empresa = models.ForeignKey('Emp', models.DO_NOTHING, db_column='emp_id_empresa', to_field='empresa_id_empresa', related_name='credencial_emp_id_empresa_set')
    emp_id_direccion = models.ForeignKey('Emp', models.DO_NOTHING, db_column='emp_id_direccion', to_field='empresa_direccion_id_direccion', related_name='credencial_emp_id_direccion_set')
    emp_id_comuna = models.ForeignKey('Emp', models.DO_NOTHING, db_column='emp_id_comuna', to_field='empresa_direccion_id_comuna', related_name='credencial_emp_id_comuna_set')
    emp_id_region = models.ForeignKey('Emp', models.DO_NOTHING, db_column='emp_id_region', to_field='empresa_direccion_id_region', related_name='credencial_emp_id_region_set')

    class Meta:
        managed = False
        db_table = 'credencial'
        unique_together = (('emp_id_empleado', 'emp_cargo_emp_id_cargo_e', 'emp_id_empresa', 'emp_id_direccion', 'emp_id_comuna', 'emp_id_region'),)


class Direccion(models.Model):
    id_direccion = models.CharField(primary_key=True, max_length=25)  # The composite primary key (id_direccion, comuna_id_comuna, comuna_id_region) found, that is not supported. The first column is selected.
    direccion = models.CharField(max_length=25)
    n_direccion = models.CharField(max_length=25)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    comuna_id_region = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_region', to_field='region_id_region', related_name='direccion_comuna_id_region_set')

    class Meta:
        managed = False
        db_table = 'direccion'
        unique_together = (('id_direccion', 'comuna_id_comuna', 'comuna_id_region'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emp(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=50)  # The composite primary key (id_empleado, cargo_emp_id_cargo_e, empresa_id_empresa, empresa_direccion_id_direccion, empresa_direccion_id_comuna, empresa_direccion_id_region) found, that is not supported. The first column is selected.
    email = models.CharField(max_length=50)
    rut = models.CharField(max_length=8)
    dv_rut = models.CharField(max_length=1)
    p_nombre = models.CharField(max_length=15)
    s_nombre = models.CharField(max_length=15)
    p_apellido = models.CharField(max_length=15)
    s_apellido = models.CharField(max_length=15)
    cargo_emp_id_cargo_e = models.ForeignKey(CargoEmp, models.DO_NOTHING, db_column='cargo_emp_id_cargo_e')
    empresa_id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_id_empresa')
    empresa_direccion_id_direccion = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_direccion_id_direccion', to_field='direccion_id_direccion', related_name='emp_empresa_direccion_id_direccion_set')
    empresa_direccion_id_comuna = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_direccion_id_comuna', to_field='direccion_id_comuna', related_name='emp_empresa_direccion_id_comuna_set')
    empresa_direccion_id_region = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_direccion_id_region', to_field='direccion_id_region', related_name='emp_empresa_direccion_id_region_set')

    class Meta:
        managed = False
        db_table = 'emp'
        unique_together = (('id_empleado', 'cargo_emp_id_cargo_e', 'empresa_id_empresa', 'empresa_direccion_id_direccion', 'empresa_direccion_id_comuna', 'empresa_direccion_id_region'),)


class Empresa(models.Model):
    id_empresa = models.CharField(primary_key=True, max_length=25)  # The composite primary key (id_empresa, direccion_id_direccion, direccion_id_comuna, direccion_id_region) found, that is not supported. The first column is selected.
    empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    n_direccion = models.CharField(max_length=10)
    direccion_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_direccion')
    direccion_id_comuna = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_comuna', to_field='comuna_id_comuna', related_name='empresa_direccion_id_comuna_set')
    direccion_id_region = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_region', to_field='comuna_id_region', related_name='empresa_direccion_id_region_set')

    class Meta:
        managed = False
        db_table = 'empresa'
        unique_together = (('id_empresa', 'direccion_id_direccion', 'direccion_id_comuna', 'direccion_id_region'),)


class Estado(models.Model):
    id_estado = models.CharField(primary_key=True, max_length=25)
    estado = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoSoli(models.Model):
    id_estado_soli = models.CharField(primary_key=True, max_length=25)
    estado = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado_soli'


class Piso(models.Model):
    id_piso = models.CharField(primary_key=True, max_length=25)
    piso = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'piso'


class Prioridad(models.Model):
    id_prioridad = models.CharField(primary_key=True, max_length=20)
    prioridad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'prioridad'


class Region(models.Model):
    id_region = models.CharField(primary_key=True, max_length=25)
    region = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'region'


class Reporte(models.Model):
    id_reporte = models.CharField(primary_key=True, max_length=50)  # The composite primary key (id_reporte, prioridad_id_prioridad, emp_id_empleado, emp_cargo_emp_id_cargo_e, emp_id_empresa, emp_id_direccion, emp_id_comuna, emp_id_region, sector_id_sector, piso_id_piso, estado_id_estado, categoria_id_categoria) found, that is not supported. The first column is selected.
    imagen = models.BinaryField()
    titulo = models.CharField(max_length=25)
    ingreso = models.DateField()
    descripcion = models.CharField(max_length=250)
    emp_id_empleado = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_empleado')
    emp_cargo_emp_id_cargo_e = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_cargo_emp_id_cargo_e', to_field='cargo_emp_id_cargo_e', related_name='reporte_emp_cargo_emp_id_cargo_e_set')
    prioridad_id_prioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='prioridad_id_prioridad')
    sector_id_sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector_id_sector')
    piso_id_piso = models.ForeignKey(Piso, models.DO_NOTHING, db_column='piso_id_piso')
    estado_id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado_id_estado')
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_categoria')
    emp_id_empresa = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_empresa', to_field='empresa_id_empresa', related_name='reporte_emp_id_empresa_set')
    emp_id_direccion = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_direccion', to_field='empresa_direccion_id_direccion', related_name='reporte_emp_id_direccion_set')
    emp_id_comuna = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_comuna', to_field='empresa_direccion_id_comuna', related_name='reporte_emp_id_comuna_set')
    emp_id_region = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_region', to_field='empresa_direccion_id_region', related_name='reporte_emp_id_region_set')

    class Meta:
        managed = False
        db_table = 'reporte'
        unique_together = (('id_reporte', 'prioridad_id_prioridad', 'emp_id_empleado', 'emp_cargo_emp_id_cargo_e', 'emp_id_empresa', 'emp_id_direccion', 'emp_id_comuna', 'emp_id_region', 'sector_id_sector', 'piso_id_piso', 'estado_id_estado', 'categoria_id_categoria'),)


class Sector(models.Model):
    id_sector = models.CharField(primary_key=True, max_length=25)
    sector = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'sector'


class Solicitud(models.Model):
    id_solicitud = models.CharField(primary_key=True, max_length=25)  # The composite primary key (id_solicitud, emp_id_empleado, emp_cargo_emp_id_cargo_e, emp_id_empresa, emp_id_direccion, emp_id_comuna, emp_id_region, estado_soli_id_estado_soli) found, that is not supported. The first column is selected.
    solicitud = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    emp_id_empleado = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_empleado')
    emp_cargo_emp_id_cargo_e = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_cargo_emp_id_cargo_e', to_field='cargo_emp_id_cargo_e', related_name='solicitud_emp_cargo_emp_id_cargo_e_set')
    estado_soli_id_estado_soli = models.ForeignKey(EstadoSoli, models.DO_NOTHING, db_column='estado_soli_id_estado_soli')
    emp_id_empresa = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_empresa', to_field='empresa_id_empresa', related_name='solicitud_emp_id_empresa_set')
    emp_id_direccion = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_direccion', to_field='empresa_direccion_id_direccion', related_name='solicitud_emp_id_direccion_set')
    emp_id_comuna = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_comuna', to_field='empresa_direccion_id_comuna', related_name='solicitud_emp_id_comuna_set')
    emp_id_region = models.ForeignKey(Emp, models.DO_NOTHING, db_column='emp_id_region', to_field='empresa_direccion_id_region', related_name='solicitud_emp_id_region_set')

    class Meta:
        managed = False
        db_table = 'solicitud'
        unique_together = (('id_solicitud', 'emp_id_empleado', 'emp_cargo_emp_id_cargo_e', 'emp_id_empresa', 'emp_id_direccion', 'emp_id_comuna', 'emp_id_region', 'estado_soli_id_estado_soli'),)
