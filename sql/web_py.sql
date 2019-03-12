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
	primary key(id)

);