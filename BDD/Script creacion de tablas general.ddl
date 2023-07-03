-- Generado por Oracle SQL Developer Data Modeler 22.2.0.165.1149
--   en:        2023-07-02 19:14:55 CLT
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE cargo_emp CASCADE CONSTRAINTS;

DROP TABLE comuna CASCADE CONSTRAINTS;

DROP TABLE empleado CASCADE CONSTRAINTS;

DROP TABLE estado_r CASCADE CONSTRAINTS;

DROP TABLE estado_s CASCADE CONSTRAINTS;

DROP TABLE estado_u CASCADE CONSTRAINTS;

DROP TABLE historial CASCADE CONSTRAINTS;

DROP TABLE insumos CASCADE CONSTRAINTS;

DROP TABLE piso CASCADE CONSTRAINTS;

DROP TABLE prioridad CASCADE CONSTRAINTS;

DROP TABLE region CASCADE CONSTRAINTS;

DROP TABLE reporte CASCADE CONSTRAINTS;

DROP TABLE sector CASCADE CONSTRAINTS;

DROP TABLE solicitud CASCADE CONSTRAINTS;

DROP TABLE sucursal CASCADE CONSTRAINTS;

DROP TABLE usuario CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE cargo_emp (
    id_cargo_emp NUMBER NOT NULL,
    cargo        VARCHAR2(50) NOT NULL
);

ALTER TABLE cargo_emp ADD CONSTRAINT cargo_emp_pk PRIMARY KEY ( id_cargo_emp );

CREATE TABLE comuna (
    id_comuna        NUMBER NOT NULL,
    comuna           VARCHAR2(50) NOT NULL,
    region_id_region NUMBER NOT NULL
);

ALTER TABLE comuna ADD CONSTRAINT comuna_pk PRIMARY KEY ( id_comuna );

CREATE TABLE empleado (
    rut                    NUMBER NOT NULL,
    dv_rut                 VARCHAR2(1) NOT NULL,
    p_nombre               VARCHAR2(50) NOT NULL,
    s_nombre               VARCHAR2(50) NOT NULL,
    p_apellido             VARCHAR2(50) NOT NULL,
    s_apellido             VARCHAR2(50) NOT NULL,
    email                  VARCHAR2(50) NOT NULL,
    cargo_emp_id_cargo_emp NUMBER NOT NULL,
    sucursal_id_sucursal   NUMBER NOT NULL,
    imagen                 BLOB
);

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( rut );

CREATE TABLE estado_r (
    id_estado NUMBER NOT NULL,
    estado    VARCHAR2(50) NOT NULL
);

ALTER TABLE estado_r ADD CONSTRAINT estado_r_pk PRIMARY KEY ( id_estado );

CREATE TABLE estado_s (
    id_estado_solicitud NUMBER NOT NULL,
    estado_solicitud    VARCHAR2(50) NOT NULL
);

ALTER TABLE estado_s ADD CONSTRAINT estado_s_pk PRIMARY KEY ( id_estado_solicitud );

CREATE TABLE estado_u (
    id_estado_u NUMBER NOT NULL,
    estado_u    VARCHAR2(50) NOT NULL
);

ALTER TABLE estado_u ADD CONSTRAINT estado_u_pk PRIMARY KEY ( id_estado_u );

CREATE TABLE historial (
    id          NUMBER NOT NULL,
    fecha       VARCHAR2(20),
    ingresado   VARCHAR2(30),
    descripcion VARCHAR2(150),
    origen      VARCHAR2(20)
);

CREATE TABLE insumos (
    id_insumo            NUMBER NOT NULL,
    insumo               VARCHAR2(50) NOT NULL,
    stock                NUMBER NOT NULL,
    color                VARCHAR2(50),
    sucursal_id_sucursal NUMBER NOT NULL
);

ALTER TABLE insumos ADD CONSTRAINT insumos_pk PRIMARY KEY ( id_insumo );

CREATE TABLE piso (
    id_piso NUMBER NOT NULL,
    piso    NUMBER NOT NULL
);

ALTER TABLE piso ADD CONSTRAINT piso_pk PRIMARY KEY ( id_piso );

CREATE TABLE prioridad (
    id_prioridad NUMBER NOT NULL,
    prioridad    VARCHAR2(50) NOT NULL
);

ALTER TABLE prioridad ADD CONSTRAINT prioridad_pk PRIMARY KEY ( id_prioridad );

CREATE TABLE region (
    id_region NUMBER NOT NULL,
    region    VARCHAR2(50) NOT NULL
);

ALTER TABLE region ADD CONSTRAINT region_pk PRIMARY KEY ( id_region );

CREATE TABLE reporte (
    id_reporte             NUMBER NOT NULL,
    titulo                 VARCHAR2(50) NOT NULL,
    descripcion            VARCHAR2(300) NOT NULL,
    fecha_ingreso          TIMESTAMP NOT NULL,
    usuario_usuario        VARCHAR2(50) NOT NULL,
    prioridad_id_prioridad NUMBER NOT NULL,
    piso_id_piso           NUMBER NOT NULL,
    sector_id_sector       NUMBER NOT NULL,
    estado_r_id_estado     NUMBER NOT NULL,
    sucursal_id_sucursal   NUMBER NOT NULL,
    imagen                 BLOB,
    asignado               VARCHAR2(50),
    desc_solucion          VARCHAR2(300)
);

ALTER TABLE reporte ADD CONSTRAINT reporte_pk PRIMARY KEY ( id_reporte );

CREATE TABLE sector (
    id_sector NUMBER NOT NULL,
    sector    VARCHAR2(50) NOT NULL
);

ALTER TABLE sector ADD CONSTRAINT sector_pk PRIMARY KEY ( id_sector );

CREATE TABLE solicitud (
    id_solicitud                 NUMBER NOT NULL,
    solicitud                    VARCHAR2(50) NOT NULL,
    fecha                        TIMESTAMP NOT NULL,
    estado_s_id_estado_solicitud NUMBER NOT NULL,
    sucursal_id_sucursal         NUMBER NOT NULL,
    usuario_usuario              VARCHAR2(50) NOT NULL
);

ALTER TABLE solicitud ADD CONSTRAINT solicitud_pk PRIMARY KEY ( id_solicitud );

CREATE TABLE sucursal (
    id_sucursal      NUMBER NOT NULL,
    sucursal         VARCHAR2(50) NOT NULL,
    direccion        VARCHAR2(50) NOT NULL,
    n_direccion      NUMBER NOT NULL,
    comuna_id_comuna NUMBER NOT NULL
);

ALTER TABLE sucursal ADD CONSTRAINT sucursal_pk PRIMARY KEY ( id_sucursal );

CREATE TABLE usuario (
    usuario              VARCHAR2(50) NOT NULL,
    contrasena           VARCHAR2(50) NOT NULL,
    empleado_rut         NUMBER NOT NULL,
    estado_u_id_estado_u NUMBER NOT NULL
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( usuario );

ALTER TABLE comuna
    ADD CONSTRAINT comuna_region_fk FOREIGN KEY ( region_id_region )
        REFERENCES region ( id_region );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_cargo_emp_fk FOREIGN KEY ( cargo_emp_id_cargo_emp )
        REFERENCES cargo_emp ( id_cargo_emp );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_sucursal_fk FOREIGN KEY ( sucursal_id_sucursal )
        REFERENCES sucursal ( id_sucursal );

ALTER TABLE insumos
    ADD CONSTRAINT insumos_sucursal_fk FOREIGN KEY ( sucursal_id_sucursal )
        REFERENCES sucursal ( id_sucursal );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_estado_r_fk FOREIGN KEY ( estado_r_id_estado )
        REFERENCES estado_r ( id_estado );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_piso_fk FOREIGN KEY ( piso_id_piso )
        REFERENCES piso ( id_piso );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_prioridad_fk FOREIGN KEY ( prioridad_id_prioridad )
        REFERENCES prioridad ( id_prioridad );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_sector_fk FOREIGN KEY ( sector_id_sector )
        REFERENCES sector ( id_sector );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_sucursal_fk FOREIGN KEY ( sucursal_id_sucursal )
        REFERENCES sucursal ( id_sucursal );

ALTER TABLE reporte
    ADD CONSTRAINT reporte_usuario_fk FOREIGN KEY ( usuario_usuario )
        REFERENCES usuario ( usuario );

ALTER TABLE solicitud
    ADD CONSTRAINT solicitud_estado_s_fk FOREIGN KEY ( estado_s_id_estado_solicitud )
        REFERENCES estado_s ( id_estado_solicitud );

ALTER TABLE solicitud
    ADD CONSTRAINT solicitud_sucursal_fk FOREIGN KEY ( sucursal_id_sucursal )
        REFERENCES sucursal ( id_sucursal );

ALTER TABLE solicitud
    ADD CONSTRAINT solicitud_usuario_fk FOREIGN KEY ( usuario_usuario )
        REFERENCES usuario ( usuario );

ALTER TABLE sucursal
    ADD CONSTRAINT sucursal_comuna_fk FOREIGN KEY ( comuna_id_comuna )
        REFERENCES comuna ( id_comuna );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_empleado_fk FOREIGN KEY ( empleado_rut )
        REFERENCES empleado ( rut );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_estado_u_fk FOREIGN KEY ( estado_u_id_estado_u )
        REFERENCES estado_u ( id_estado_u );

CREATE SEQUENCE cargo_emp_id_cargo_emp_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER cargo_emp_id_cargo_emp_trg BEFORE
    INSERT ON cargo_emp
    FOR EACH ROW
    WHEN ( new.id_cargo_emp IS NULL )
BEGIN
    :new.id_cargo_emp := cargo_emp_id_cargo_emp_seq.nextval;
END;
/

CREATE SEQUENCE comuna_id_comuna_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER comuna_id_comuna_trg BEFORE
    INSERT ON comuna
    FOR EACH ROW
    WHEN ( new.id_comuna IS NULL )
BEGIN
    :new.id_comuna := comuna_id_comuna_seq.nextval;
END;
/

CREATE SEQUENCE empleado_rut_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER empleado_rut_trg BEFORE
    INSERT ON empleado
    FOR EACH ROW
    WHEN ( new.rut IS NULL )
BEGIN
    :new.rut := empleado_rut_seq.nextval;
END;
/

CREATE SEQUENCE estado_r_id_estado_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER estado_r_id_estado_trg BEFORE
    INSERT ON estado_r
    FOR EACH ROW
    WHEN ( new.id_estado IS NULL )
BEGIN
    :new.id_estado := estado_r_id_estado_seq.nextval;
END;
/

CREATE SEQUENCE estado_s_id_estado_solicitud START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER estado_s_id_estado_solicitud BEFORE
    INSERT ON estado_s
    FOR EACH ROW
    WHEN ( new.id_estado_solicitud IS NULL )
BEGIN
    :new.id_estado_solicitud := estado_s_id_estado_solicitud.nextval;
END;
/

CREATE SEQUENCE estado_u_id_estado_u_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER estado_u_id_estado_u_trg BEFORE
    INSERT ON estado_u
    FOR EACH ROW
    WHEN ( new.id_estado_u IS NULL )
BEGIN
    :new.id_estado_u := estado_u_id_estado_u_seq.nextval;
END;
/

CREATE SEQUENCE historial_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER historial_id_trg BEFORE
    INSERT ON historial
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := historial_id_seq.nextval;
END;
/

CREATE SEQUENCE insumos_id_insumo_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER insumos_id_insumo_trg BEFORE
    INSERT ON insumos
    FOR EACH ROW
    WHEN ( new.id_insumo IS NULL )
BEGIN
    :new.id_insumo := insumos_id_insumo_seq.nextval;
END;
/

CREATE SEQUENCE piso_id_piso_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER piso_id_piso_trg BEFORE
    INSERT ON piso
    FOR EACH ROW
    WHEN ( new.id_piso IS NULL )
BEGIN
    :new.id_piso := piso_id_piso_seq.nextval;
END;
/

CREATE SEQUENCE prioridad_id_prioridad_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER prioridad_id_prioridad_trg BEFORE
    INSERT ON prioridad
    FOR EACH ROW
    WHEN ( new.id_prioridad IS NULL )
BEGIN
    :new.id_prioridad := prioridad_id_prioridad_seq.nextval;
END;
/

CREATE SEQUENCE reporte_id_reporte_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER reporte_id_reporte_trg BEFORE
    INSERT ON reporte
    FOR EACH ROW
    WHEN ( new.id_reporte IS NULL )
BEGIN
    :new.id_reporte := reporte_id_reporte_seq.nextval;
END;
/

CREATE SEQUENCE sector_id_sector_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER sector_id_sector_trg BEFORE
    INSERT ON sector
    FOR EACH ROW
    WHEN ( new.id_sector IS NULL )
BEGIN
    :new.id_sector := sector_id_sector_seq.nextval;
END;
/

CREATE SEQUENCE solicitud_id_solicitud_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER solicitud_id_solicitud_trg BEFORE
    INSERT ON solicitud
    FOR EACH ROW
    WHEN ( new.id_solicitud IS NULL )
BEGIN
    :new.id_solicitud := solicitud_id_solicitud_seq.nextval;
END;
/

CREATE SEQUENCE sucursal_id_sucursal_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER sucursal_id_sucursal_trg BEFORE
    INSERT ON sucursal
    FOR EACH ROW
    WHEN ( new.id_sucursal IS NULL )
BEGIN
    :new.id_sucursal := sucursal_id_sucursal_seq.nextval;
END;
/

CREATE SEQUENCE usuario_usuario_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER usuario_usuario_trg BEFORE
    INSERT ON usuario
    FOR EACH ROW
    WHEN ( new.usuario IS NULL )
BEGIN
    :new.usuario := usuario_usuario_seq.nextval;
END;
/



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            16
-- CREATE INDEX                             0
-- ALTER TABLE                             31
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                          15
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                         15
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
