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
CREATE DATABASE IF NOT EXISTS `park` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `park`;

-- Volcando estructura para tabla park.usuarios
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
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla park.usuarios: 4 rows
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `telefono`, `correo`, `password`, `rol`, `imagen`) VALUES
	(9, 'Pepito', 'Mijares', 4652, 'correo@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', 1, NULL),
	(15, 'Oscar', 'Escamilla', 77563456, 'ozkar@gmail.com', '4297f44b13955235245b2497399d7a93', 1, NULL),
	(16, 'Oscar', 'Escamilla Luqueño', 7756235, 'escamilla@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 1, NULL),
	(17, 'Oscar', 'Lopez Perez', 89789431, 'manuelito@gmail.com', '25f9e794323b453885f5181f1b624d0b', 1, NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
