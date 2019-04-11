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

-- Volcando estructura para tabla park.login
DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `id` int(11) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `rol` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.login: 8 rows
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`id`, `correo`, `password`, `rol`) VALUES
	(1, 'usuario@usuario.com', 'f8032d5cae3de20fcec887f395ec9a6a', 1),
	(2, 'empresa@empresa', '04299e213f5391ede16784de41dd847d', 2),
	(3, 'empresa@empresa', '04299e213f5391ede16784de41dd847d', 2),
	(4, 'empresa@empresa', '04299e213f5391ede16784de41dd847d', 2),
	(5, 'empresa@empresa', '04299e213f5391ede16784de41dd847d', 2),
	(6, 'empresa@empresa', '81dc9bdb52d04dc20036dbd8313ed055', 2),
	(2, '', 'd41d8cd98f00b204e9800998ecf8427e', 1),
	(3, '', 'd41d8cd98f00b204e9800998ecf8427e', 1);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;

-- Volcando estructura para tabla park.parks
DROP TABLE IF EXISTS `parks`;
CREATE TABLE IF NOT EXISTS `parks` (
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
  `telefono` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `hora_apertura` varchar(50) NOT NULL,
  `hora_cierre` varchar(50) NOT NULL,
  `dia_inicio` varchar(20) NOT NULL,
  `dia_final` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rol` int(11) NOT NULL DEFAULT '2',
  `disponibilidad` int(11) DEFAULT NULL,
  `imagen` varchar(20) DEFAULT NULL,
  `puntuacion` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.parks: 5 rows
/*!40000 ALTER TABLE `parks` DISABLE KEYS */;
INSERT INTO `parks` (`id`, `nombre`, `titular`, `colonia`, `calle`, `numero`, `cp`, `latitud`, `longitud`, `tarifa`, `telefono`, `correo`, `hora_apertura`, `hora_cierre`, `dia_inicio`, `dia_final`, `password`, `rol`, `disponibilidad`, `imagen`, `puntuacion`) VALUES
	(2, 'Oscar', 'sdsadasd', 'Jaltepec', 'jjhbj', 516, 156165, '45612', '-98652', 52, '34324324', 'empresa@empresa', '00:00', '00:00', 'Lunes', 'Lunes', '04299e213f5391ede16784de41dd847d', 2, NULL, NULL, NULL),
	(3, 'Oscar', 'sdsadasd', 'Jaltepec', 'jjhbj', 516, 156165, '45612', '-98652', 52, '34324324', 'empresa@empresa', '00:00', '00:00', 'Lunes', 'Lunes', '04299e213f5391ede16784de41dd847d', 2, NULL, NULL, NULL),
	(4, 'Oscar', 'sdsadasd', 'Jaltepec', 'jjhbj', 516, 156165, '45612', '-98652', 52, '34324324', 'empresa@empresa', '00:00', '00:00', 'Lunes', 'Lunes', '04299e213f5391ede16784de41dd847d', 2, NULL, NULL, NULL),
	(5, 'Oscar', 'sdsadasd', 'Jaltepec', 'jjhbj', 516, 156165, '45612', '-98652', 52, '34324324', 'empresa@empresa', '00:00', '00:00', 'Lunes', 'Lunes', '04299e213f5391ede16784de41dd847d', 2, NULL, NULL, NULL),
	(6, 'usuario', 'estacionamiento', 'paraiso ', 'zpata', 302, 456987, '45612', '-98652', 52, '34324324', 'empresa@empresa', '00:00', '00:00', 'Lunes', 'Lunes', '81dc9bdb52d04dc20036dbd8313ed055', 2, NULL, NULL, NULL);
/*!40000 ALTER TABLE `parks` ENABLE KEYS */;

-- Volcando estructura para tabla park.reservas
DROP TABLE IF EXISTS `reservas`;
CREATE TABLE IF NOT EXISTS `reservas` (
  `id_user` int(11) NOT NULL,
  `id_park` int(11) NOT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `hora_limite` varchar(50) NOT NULL,
  `folio` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.reservas: 0 rows
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;

-- Volcando estructura para tabla park.sessions
DROP TABLE IF EXISTS `sessions`;
CREATE TABLE IF NOT EXISTS `sessions` (
  `id` int(11) NOT NULL,
  `rol` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.sessions: 1 rows
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` (`id`, `rol`) VALUES
	(9, 1);
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;

-- Volcando estructura para tabla park.users
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'identidficador del usuario ',
  `nombre` varchar(20) NOT NULL COMMENT 'nombre del usuario',
  `apellidos` varchar(50) NOT NULL COMMENT 'apellidos del usuario',
  `telefono` varchar(50) NOT NULL COMMENT 'telefono del usuario',
  `correo` varchar(50) NOT NULL COMMENT 'correo del usuario',
  `password` varchar(100) NOT NULL COMMENT 'password del usuario',
  `rol` int(11) NOT NULL DEFAULT '1' COMMENT 'rol del usuario',
  `imagen` varchar(20) DEFAULT NULL COMMENT 'imagen del usuario ',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.users: 1 rows
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `nombre`, `apellidos`, `telefono`, `correo`, `password`, `rol`, `imagen`) VALUES
	(1, 'Oscar', 'Escamilla ', '7751306549', 'usuario@usuario.com', 'f8032d5cae3de20fcec887f395ec9a6a', 1, NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Volcando estructura para disparador park.nuevo_estacionamiento
DROP TRIGGER IF EXISTS `nuevo_estacionamiento`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER';
DELIMITER //
CREATE TRIGGER `nuevo_estacionamiento` AFTER INSERT ON `parks` FOR EACH ROW INSERT INTO  login (id,correo, password, rol) VALUES
    (new.id, new.correo ,new.password, new.rol)//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Volcando estructura para disparador park.nuevo_usuario
DROP TRIGGER IF EXISTS `nuevo_usuario`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER';
DELIMITER //
CREATE TRIGGER `nuevo_usuario` AFTER INSERT ON `users` FOR EACH ROW INSERT INTO  login (id,correo, password, rol) VALUES
    (new.id, new.correo ,new.password, new.rol)//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
