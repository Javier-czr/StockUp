-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2024 at 07:38 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stockup`
--

-- --------------------------------------------------------

--
-- Table structure for table `categoria`
--

CREATE TABLE `categoria` (
  `IdCategoria` int(4) NOT NULL,
  `Nombre` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categoria`
--

INSERT INTO `categoria` (`IdCategoria`, `Nombre`) VALUES
(0, '[liquido]'),
(1, 'Salsas');

-- --------------------------------------------------------

--
-- Table structure for table `causadano`
--

CREATE TABLE `causadano` (
  `IdCausaDano` int(4) NOT NULL,
  `CausaDano` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `causadano`
--

INSERT INTO `causadano` (`IdCausaDano`, `CausaDano`) VALUES
(0, 'Externa');

-- --------------------------------------------------------

--
-- Table structure for table `historailcambio`
--

CREATE TABLE `historailcambio` (
  `IdCambio` int(5) NOT NULL,
  `fechaCambio` date NOT NULL,
  `DescripcionCambio` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `historialpedido`
--

CREATE TABLE `historialpedido` (
  `IdPedido` int(6) NOT NULL,
  `nombreProducto` int(4) NOT NULL,
  `cantidadEmpaque` int(4) NOT NULL,
  `UnidadPorEmpaque` int(5) NOT NULL,
  `FechaPedido` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `producto`
--

CREATE TABLE `producto` (
  `IdProducto` int(13) NOT NULL,
  `Nombre` varchar(40) NOT NULL,
  `Marca` varchar(40) NOT NULL,
  `IdCategoria` varchar(20) NOT NULL,
  `Cantidad` int(4) NOT NULL,
  `FechaVencimiento` date NOT NULL,
  `Precio` int(7) NOT NULL,
  `IdUbicacion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `producto`
--

INSERT INTO `producto` (`IdProducto`, `Nombre`, `Marca`, `IdCategoria`, `Cantidad`, `FechaVencimiento`, `Precio`, `IdUbicacion`) VALUES
(12, 'Javier', 'Nestle', 'Cuerda', 450, '2024-04-29', 4000, '2a');

-- --------------------------------------------------------

--
-- Table structure for table `productodanado`
--

CREATE TABLE `productodanado` (
  `IdDanado` int(6) NOT NULL,
  `IdProducto` int(13) NOT NULL,
  `Nombre` varchar(40) NOT NULL,
  `Cantidad` int(4) NOT NULL,
  `Costo` int(7) NOT NULL,
  `CausaDano` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `proveedor`
--

CREATE TABLE `proveedor` (
  `RutProveedor` varchar(9) NOT NULL,
  `Empresa` varchar(40) NOT NULL,
  `Nombre` varchar(40) NOT NULL,
  `Apellido` varchar(40) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Correo` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proveedor`
--

INSERT INTO `proveedor` (`RutProveedor`, `Empresa`, `Nombre`, `Apellido`, `Telefono`, `Correo`) VALUES
('201113324', 'Carozzi', 'Martha', 'Wayne', 2147483647, 'javi.sanchez@duocuc.com'),
('213548832', 'Nestle', 'Roberto', 'Gomez', 234567876, 'javi.sanchez@duocuc.cls'),
('213548833', 'Vederal', 'Javier', 'Sanchez', 2147483647, 'javi.sanchez@duocuc.cl'),
('23232', 'Carozzi', 'Martha', 'Wayne', 2147483647, 'javi.sanchez@duocuc.css');

-- --------------------------------------------------------

--
-- Table structure for table `ubicacion`
--

CREATE TABLE `ubicacion` (
  `IdUbicacion` int(11) NOT NULL,
  `Nombre` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ubicacion`
--

INSERT INTO `ubicacion` (`IdUbicacion`, `Nombre`) VALUES
(0, '[a1]'),
(1, 'a2');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(3) NOT NULL,
  `Usuario` varchar(40) NOT NULL,
  `Contrasena` varchar(40) NOT NULL,
  `Correo` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`IdCategoria`);

--
-- Indexes for table `causadano`
--
ALTER TABLE `causadano`
  ADD PRIMARY KEY (`IdCausaDano`);

--
-- Indexes for table `historailcambio`
--
ALTER TABLE `historailcambio`
  ADD PRIMARY KEY (`IdCambio`);

--
-- Indexes for table `historialpedido`
--
ALTER TABLE `historialpedido`
  ADD PRIMARY KEY (`IdPedido`),
  ADD KEY `NombrePedido` (`nombreProducto`);

--
-- Indexes for table `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`IdProducto`),
  ADD KEY `RutProveedor` (`Marca`),
  ADD KEY `IdUbicacion` (`IdUbicacion`),
  ADD KEY `IdCategoria` (`IdCategoria`);

--
-- Indexes for table `productodanado`
--
ALTER TABLE `productodanado`
  ADD PRIMARY KEY (`IdDanado`),
  ADD KEY `IdProducto` (`IdProducto`),
  ADD KEY `CausaDano` (`CausaDano`);

--
-- Indexes for table `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`RutProveedor`);

--
-- Indexes for table `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD PRIMARY KEY (`IdUbicacion`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `historailcambio`
--
ALTER TABLE `historailcambio`
  MODIFY `IdCambio` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `historialpedido`
--
ALTER TABLE `historialpedido`
  MODIFY `IdPedido` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(3) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `historialpedido`
--
ALTER TABLE `historialpedido`
  ADD CONSTRAINT `NombrePedido` FOREIGN KEY (`nombreProducto`) REFERENCES `producto` (`IdProducto`);

--
-- Constraints for table `productodanado`
--
ALTER TABLE `productodanado`
  ADD CONSTRAINT `CausaDano` FOREIGN KEY (`CausaDano`) REFERENCES `causadano` (`IdCausaDano`),
  ADD CONSTRAINT `IdProducto` FOREIGN KEY (`IdProducto`) REFERENCES `producto` (`IdProducto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
