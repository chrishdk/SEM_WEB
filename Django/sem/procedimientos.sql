
create or replace procedure sp_listar_usuarios(usuarios out SYS_REFCURSOR)
is

begin
    open usuarios for select * from Usuario;
end;
/


create or replace procedure sp_agregar_usuario(
    v_id number,
    v_nombre varchar2,
    v_edad number,
    v_direccion varchar2,
    v_salida out number
)
is
begin
    insert into usuario(nombre, edad, direccion)
    values (v_nombre, v_edad, v_direccion);
    commit;
    v_salida:=1;
    exception
    when others then
        v_salida:=0;
end;
/


