-- Generado por Oracle SQL Developer Data Modeler 18.4.0.339.1532
--   en:        2021-01-09 13:21:00 CLST
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g

/* drop table detalle_boleta;
drop table detalle_cotizacion;
drop table abono;
drop table cotizacion;
drop table producto;
drop table tipo_producto;
drop table servicio;
drop table boleta;
drop table cliente;
drop table vendedor; */

CREATE TABLE boleta (
    id_boleta              INTEGER NOT NULL,
    fecha                  DATE NOT NULL,
    cliente_id_cliente     INTEGER NOT NULL,
    vendedor_id_vendedor   INTEGER NOT NULL,
    abono FLOAT
);

ALTER TABLE boleta ADD CONSTRAINT boleta_pk PRIMARY KEY ( id_boleta ) ;
ALTER TABLE `boleta` CHANGE `id_boleta` `id_boleta` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE cotizacion (
    id_cotizacion          INTEGER NOT NULL,
    fecha                  DATE,
    cliente_id_cliente     INTEGER NOT NULL,
    vendedor_id_vendedor   INTEGER NOT NULL
);

ALTER TABLE cotizacion ADD CONSTRAINT boletav1_pk PRIMARY KEY ( id_cotizacion );
ALTER TABLE `cotizacion` CHANGE `id_cotizacion` `id_cotizacion` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE cliente (
    id_cliente   INTEGER NOT NULL,
    nombre       VARCHAR(50),
    apellido     VARCHAR(50),
    rut          VARCHAR(10),
    telefono     VARCHAR(50),
    correo       VARCHAR(50),
    direccion    VARCHAR(50),
    comuna       VARCHAR(50),
    region       VARCHAR(50)
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente ) ;
ALTER TABLE `cliente` ADD UNIQUE( `rut`);
ALTER TABLE `cliente` CHANGE `id_cliente` `id_cliente` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE detalle_cotizacion (
    id_detallecotizacion       INTEGER NOT NULL,
    detalle                    VARCHAR(100),
    total                      FLOAT,
    cotizacion_id_cotizacion   INTEGER NOT NULL,
    servicio_id_servicio       INTEGER,
    producto_id_producto       INTEGER
);

ALTER TABLE detalle_cotizacion ADD CONSTRAINT detalle_boletav1_pk PRIMARY KEY ( id_detallecotizacion );
ALTER TABLE `detalle_cotizacion` CHANGE `id_detallecotizacion` `id_detallecotizacion` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE detalle_boleta (
    id_detalleboleta       INTEGER NOT NULL,
    detalle                VARCHAR(100),
    total                  FLOAT,
    boleta_id_boleta       INTEGER NOT NULL,
    producto_id_producto   INTEGER,
    servicio_id_servicio   INTEGER
);

ALTER TABLE detalle_boleta ADD CONSTRAINT detalle_boleta_pk PRIMARY KEY ( id_detalleboleta ) ;
ALTER TABLE `detalle_boleta` CHANGE `id_detalleboleta` `id_detalleboleta` INT(11) NOT NULL AUTO_INCREMENT; 


CREATE TABLE abono (
    id_abono INTEGER NOT NULL,
    monto FLOAT,
    fecha                  DATE,
    db_id_detalleboleta      INTEGER NOT NULL
);

ALTER TABLE abono ADD CONSTRAINT abono_pk PRIMARY KEY ( id_abono ) ;
ALTER TABLE `abono` CHANGE `id_abono` `id_abono` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE producto (
    id_producto                      INTEGER NOT NULL,
    nombre                           VARCHAR(50),
    descripcion                      VARCHAR(100),
    color                            VARCHAR(20),
    material                         VARCHAR(50),
    cantidad                         INTEGER,
    ancho                            FLOAT,
    alto                             FLOAT,
    espesor                          FLOAT,
    peso                             FLOAT,
    precio                           FLOAT,
    divisiones                       INTEGER,
    accesorios                       VARCHAR(50),
    tipo_producto_id_tipo_producto   INTEGER NOT NULL
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto ) ;
ALTER TABLE `producto` CHANGE `id_producto` `id_producto` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE servicio (
    id_servicio     INTEGER NOT NULL,
    nombre          VARCHAR(50),
    descripcion     VARCHAR(100),
    fecha_inicio    DATE,
    fecha_termino   DATE,
    estado          VARCHAR(50)
);

ALTER TABLE servicio ADD CONSTRAINT servicio_pk PRIMARY KEY ( id_servicio ) ;
ALTER TABLE `servicio` CHANGE `id_servicio` `id_servicio` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE tipo_producto (
    id_tipo_producto   INTEGER NOT NULL,
    nombre             VARCHAR(50),
    descripcion        VARCHAR(100)
);

ALTER TABLE tipo_producto ADD CONSTRAINT tipo_producto_pk PRIMARY KEY ( id_tipo_producto ) ;
ALTER TABLE `tipo_producto` CHANGE `id_tipo_producto` `id_tipo_producto` INT(11) NOT NULL AUTO_INCREMENT; 

CREATE TABLE vendedor (
    id_vendedor   INTEGER NOT NULL,
    rut           VARCHAR(10),
    nombre        VARCHAR(50),
    apellido      VARCHAR(50),
    telefono      VARCHAR(20),
    correo        VARCHAR(50),
    direccion     VARCHAR(50),
    comuna        VARCHAR(50)
);

ALTER TABLE vendedor ADD CONSTRAINT vendedor_pk PRIMARY KEY ( id_vendedor ) ;
ALTER TABLE vendedor ADD UNIQUE( `rut`);
ALTER TABLE `vendedor` CHANGE `id_vendedor` `id_vendedor` INT(11) NOT NULL AUTO_INCREMENT; 

ALTER TABLE boleta
    ADD CONSTRAINT boleta_cliente_fk FOREIGN KEY ( cliente_id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE boleta
    ADD CONSTRAINT boleta_vendedor_fk FOREIGN KEY ( vendedor_id_vendedor )
        REFERENCES vendedor ( id_vendedor );

ALTER TABLE detalle_boleta
    ADD CONSTRAINT detalle_boleta_boleta_fk FOREIGN KEY ( boleta_id_boleta )
        REFERENCES boleta ( id_boleta );

ALTER TABLE detalle_boleta
    ADD CONSTRAINT detalle_boleta_producto_fk FOREIGN KEY ( producto_id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE detalle_boleta
    ADD CONSTRAINT detalle_boleta_servicio_fk FOREIGN KEY ( servicio_id_servicio )
        REFERENCES servicio ( id_servicio );

ALTER TABLE producto
    ADD CONSTRAINT producto_tipo_producto_fk FOREIGN KEY ( tipo_producto_id_tipo_producto )
        REFERENCES tipo_producto ( id_tipo_producto );




-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             13
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           7
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
-- CREATE SEQUENCE                          7
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
