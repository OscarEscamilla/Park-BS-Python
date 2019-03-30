create database park;


use park;

create table usuarios(
	id int not null auto_increment,
	nombre varchar(20) not null,
	apellidos varchar(50) not null,
	telefono int(10) not null,
	correo varchar(50) not null,
	password varchar(100) not null,
	rol int not null,
	imagen varchar(20) null,
	primary key(id)
);

create table estacionamientos(
	id int not null auto_increment,
	nombre varchar(20) not null,
	titular varchar(90) not null,
	colonia varchar(30) not null,
	calle varchar(30) not null,
	numero int(5) not null,
	cp int(5) not null, 
	latitud varchar(30) not null,
	longitud varchar(30) not null,
	tarifa float not null,
	telefono char(10) not null,
	correo varchar(50) not null,
	hora_apertura time not null,
	hora_cierre time not null,
	dia_inicio varchar(20) not null,
	dia_final varchar(20) not null,
	password varchar(100) not null,
	disponibilidad int null, 
	estado int null, 
	imagen varchar(20) null, 
	puntuacion float null, 
	rol int not null,
	primary key(id)
);

create table login(
	id int,
	correo varchar(50),
	password varchar(50),
	rol int
);

CREATE TRIGGER nuevo_usuario AFTER INSERT ON usuarios
    FOR EACH ROW
    INSERT INTO  login (id,correo, password, rol) VALUES
    (new.id, new.correo ,new.password, new.rol);

CREATE TRIGGER nuevo_estacionamiento AFTER INSERT ON estacionamientos
    FOR EACH ROW
    INSERT INTO  login (id,correo, password, rol) VALUES
    (new.id, new.correo ,new.password, new.rol);