-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.24 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para park
DROP DATABASE IF EXISTS `park`;
CREATE DATABASE IF NOT EXISTS `park` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `park`;

-- Volcando estructura para tabla park.estacionamientos
DROP TABLE IF EXISTS `estacionamientos`;
CREATE TABLE IF NOT EXISTS `estacionamientos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `titular` varchar(90) NOT NULL,
  `colonia` varchar(50) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `numero` int(5) NOT NULL,
  `cp` int(5) NOT NULL,
  `latitud` varchar(30) NOT NULL,
  `longitud` varchar(30) NOT NULL,
  `tarifa` float NOT NULL,
  `telefono` char(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `hora_apertura` time NOT NULL,
  `hora_cierre` time NOT NULL,
  `dia_inicio` varchar(20) NOT NULL,
  `dia_final` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rol` int(11) NOT NULL DEFAULT '2',
  `disponibilidad` int(11) DEFAULT NULL,
  `estado` int(11) DEFAULT NULL,
  `imagen` varchar(20) DEFAULT NULL,
  `puntuacion` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.estacionamientos: 1 rows
/*!40000 ALTER TABLE `estacionamientos` DISABLE KEYS */;
INSERT INTO `estacionamientos` (`id`, `nombre`, `titular`, `colonia`, `calle`, `numero`, `cp`, `latitud`, `longitud`, `tarifa`, `telefono`, `correo`, `hora_apertura`, `hora_cierre`, `dia_inicio`, `dia_final`, `password`, `rol`, `disponibilidad`, `estado`, `imagen`, `puntuacion`) VALUES
	(1, 'estacionamiento', 'estacionamiento', 'estacionamiento', 'estacionamiento', 123, 12345, '4343', '-15165165', 20, '7758965456', 'estacionamiento@estacionamiento', '00:00:00', '00:00:00', 'Lunes', 'Lunes', '1cf22be5c5d6e219528ca3ba66b8fdab', 2, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `estacionamientos` ENABLE KEYS */;

-- Volcando estructura para tabla park.login
DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `id` int(11) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `rol` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.login: 2 rows
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`id`, `correo`, `password`, `rol`) VALUES
	(1, 'usuario@usuario.com', 'f8032d5cae3de20fcec887f395ec9a6a', 1),
	(1, 'estacionamiento@estacionamiento', '1cf22be5c5d6e219528ca3ba66b8fdab', 2);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;

-- Volcando estructura para tabla park.usuarios
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `telefono` int(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rol` int(11) NOT NULL DEFAULT '1',
  `imagen` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.usuarios: 1 rows
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `telefono`, `correo`, `password`, `rol`, `imagen`) VALUES
	(1, 'usuario', 'usuario', 5555555, 'usuario@usuario.com', 'f8032d5cae3de20fcec887f395ec9a6a', 1, NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

-- Volcando estructura para disparador park.nuevo_estacionamiento
DROP TRIGGER IF EXISTS `nuevo_estacionamiento`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER';
DELIMITER //
CREATE TRIGGER `nuevo_estacionamiento` AFTER INSERT ON `estacionamientos` FOR EACH ROW INSERT INTO  login (id,correo, password, rol) VALUES
    (new.id, new.correo ,new.password, new.rol)//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Volcando estructura para disparador park.nuevo_usuario
DROP TRIGGER IF EXISTS `nuevo_usuario`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER';
DELIMITER //
CREATE TRIGGER `nuevo_usuario` AFTER INSERT ON `usuarios` FOR EACH ROW INSERT INTO  login (id,correo, password, rol) VALUES
    (new.id, new.correo ,new.password, new.rol)//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
