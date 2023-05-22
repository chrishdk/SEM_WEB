-- Generado por Oracle SQL Developer Data Modeler 22.2.0.165.1149
--   en:        2023-05-22 13:00:36 CLT
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE cargo_emp CASCADE CONSTRAINTS;

DROP TABLE comuna CASCADE CONSTRAINTS;

DROP TABLE empleado CASCADE CONSTRAINTS;

DROP TABLE estado_r CASCADE CONSTRAINTS;

DROP TABLE estado_s CASCADE CONSTRAINTS;

DROP TABLE estado_u CASCADE CONSTRAINTS;

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
    s_apellido             VARCHAR2(50) NOT NULL,
    s_apellido_1           VARCHAR2(50) NOT NULL,
    email                  VARCHAR2(50) NOT NULL,
    cargo_emp_id_cargo_emp NUMBER NOT NULL,
    sucursal_id_sucursal   NUMBER NOT NULL
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
    id_repote              NUMBER NOT NULL,
    titulo                 VARCHAR2(50) NOT NULL,
    descripcion            VARCHAR2(300) NOT NULL,
    fecha_ingreso          DATE NOT NULL,
    usuario_usuario        VARCHAR2(50) NOT NULL,
    prioridad_id_prioridad NUMBER NOT NULL,
    piso_id_piso           NUMBER NOT NULL,
    sector_id_sector       NUMBER NOT NULL,
    estado_r_id_estado     NUMBER NOT NULL,
    sucursal_id_sucursal   NUMBER NOT NULL,
    imagen                 BLOB,
    asignado               VARCHAR2(50)
);

ALTER TABLE reporte ADD CONSTRAINT reporte_pk PRIMARY KEY ( id_repote );

CREATE TABLE sector (
    id_sector NUMBER NOT NULL,
    sector    VARCHAR2(50) NOT NULL
);

ALTER TABLE sector ADD CONSTRAINT sector_pk PRIMARY KEY ( id_sector );

CREATE TABLE solicitud (
    id_solicitud                 NUMBER NOT NULL,
    solicitud                    VARCHAR2(50) NOT NULL,
    fecha                        DATE NOT NULL,
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



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            15
-- CREATE INDEX                             0
-- ALTER TABLE                             31
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
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
-- CREATE SEQUENCE                          0
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


INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	1	,		'XV Arica y Parinacota'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	2	,		'I Tarapacá'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	3	,		'II Antofagasta'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	4	,		'III Atacama'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	5	,		'IV Coquimbo'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	6	,		'V Valparaíso'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	7	,		'XIII Región Metropolitana'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	8	,		'VI O Higgins'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	9	,		'VII Maule'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	10	,		'XVI Ñuble'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	11	,		'VIII Biobío'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	12	,		'IX La Araucanía'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	13	,		'XIV Los Ríos'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	14	,		'X Los Lagos'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	15	,		'XI Aysén'	);
INSERT INTO REGION (	ID_REGION	,	REGION	)	VALUES(	16	,		'XII Magallanes y la Antártica'	);

INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	(1, 'Santiago', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	(2, 'Cerrillos', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (3, 'Cerro Navia', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (4, 'Conchalí', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (5, 'El Bosque', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (6, 'Estación Central', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (7, 'Huechuraba', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (8, 'Independencia', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (9, 'La Cisterna', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (10, 'La Florida', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (11, 'La Granja', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (12, 'La Pintana', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (13, 'La Reina', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (14, 'Las Condes', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (15, 'Lo Barnechea', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (16, 'Lo Espejo', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (17, 'Lo Prado', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (18, 'Macul', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (19, 'Maipú', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (20, 'Ñuñoa', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (21, 'Pedro Aguirre Cerda', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (22, 'Peñalolén', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (23, 'Providencia', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (24, 'Pudahuel', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (25, 'Quilicura', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (26, 'Quinta Normal', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (27, 'Recoleta', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (28, 'Renca', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (29, 'San Joaquín', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (30, 'San Miguel', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (31, 'San Ramón', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (32, 'Vitacura', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (33, 'Puente Alto', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (34, 'Pirque', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (35, 'San José de Maipo', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (36, 'Colina', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (37, 'Lampa', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (38, 'Tiltil', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (39, 'San Bernardo', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (40, 'Buin', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (41, 'Calera de Tango', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (42, 'Paine', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (43, 'Melipilla', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (44, 'Alhué', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (45, 'Curacaví', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (46, 'María Pinto', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (47, 'San Pedro', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (48, 'Talagante', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (49, 'El Monte', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (50, 'Isla de Maipo', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (51, 'Padre Hurtado', 7)	;
INSERT INTO comuna (id_comuna, comuna, region_id_region)			VALUES 	       (52, 'Peñaflor', 7);	


insert into sucursal values(1,'SEM', 'Av. Manuel Montt','170',23);

insert into cargo_emp values ( 1,'carpintero');

insert into empleado values ( 19170582,3,'Daniel','Christian','Stari','Zúñiga','da.stari@duocuc.cl',1,1);

insert into estado_u values ( '1','habilitado');

insert into usuario values ( 'da.stari','19Da123*',19170582,1);

