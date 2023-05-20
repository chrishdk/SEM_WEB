
create or replace procedure sp_listar_usuarios(usuarios out SYS_REFCURSOR)
is

begin
    open usuarios for select * from Usuario;
end;
/


create or replace procedure sp_agregar_reporte(
    v_id_reporte number,
    v_titulo varchar2,
    v_descripcion varchar2,
    v_fecha_ingreso DATE,
    v_usuario  varchar2,
    v_prioridad  number,
    v_piso  number,
    v_sector  number,
    v_estado  number,
    v_imagen  blob,
    v_salida out number
)
is
begin
    insert into reporte(
    id_reporte,
    titulo,
    descripcion,
    fecha_ingreso,usuario_usuario,
    prioridad_id_prioridad,
    piso_id_piso,
    sector_id_sector,
    estado_r_id_estado,
    imagen)
    values (
    v_id_reporte,
    v_titulo,
    v_descripcion,
    v_fecha_ingreso,
    v_usuario,
    v_prioridad,
    v_piso,
    v_sector,
    v_estado,
    v_imagen
    );
    commit;
    v_salida:=1;
    exception
    when others then
        v_salida:=0;
end;
/


create or replace procedure sp_listar_empleados(usuarios out SYS_REFCURSOR)
is

begin
    open usuarios for select * from empleado;
end;
/