-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: testx2
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `plate` varchar(8) NOT NULL,
  `brand` varchar(20) NOT NULL,
  `model` varchar(20) NOT NULL,
  `color` varchar(20) NOT NULL,
  `km` float DEFAULT NULL,
  `statusc` char(1) NOT NULL,
  PRIMARY KEY (`plate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES ('P-01','Ford','K','Blue',0,'A'),('P-02','Ford','X','Black',0,'A'),('P-03','Hyundai','Accent','White',300,'A'),('P-04','Chevrolet','Aveo','White',520,'A'),('P-05','Toyota','Corola','Green',58,'A');
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `idx` varchar(8) NOT NULL,
  `namex` varchar(20) NOT NULL,
  `lastnamex` varchar(20) NOT NULL,
  `licensePlate` varchar(15) NOT NULL,
  `statusx` char(1) NOT NULL,
  PRIMARY KEY (`idx`),
  KEY `licensePlate` (`licensePlate`),
  CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`licensePlate`) REFERENCES `cars` (`plate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES ('C01','Carlos','Martínez','P-01','A'),('C02','María','Álvarez','P-02','A'),('C03','Patrica','Colmenarez','P-03','A');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientsv`
--

DROP TABLE IF EXISTS `clientsv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientsv` (
  `idc` varchar(8) NOT NULL,
  `namec` varchar(20) NOT NULL,
  `lastnamec` varchar(20) NOT NULL,
  `cityc` varchar(20) NOT NULL,
  `categoryc` int NOT NULL,
  `statusc` char(1) NOT NULL,
  PRIMARY KEY (`idc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientsv`
--

LOCK TABLES `clientsv` WRITE;
/*!40000 ALTER TABLE `clientsv` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientsv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `ido` varchar(8) NOT NULL,
  `dateo` date NOT NULL,
  `total` float NOT NULL,
  `vendoro` varchar(8) NOT NULL,
  `cliento` varchar(8) NOT NULL,
  PRIMARY KEY (`ido`),
  KEY `vendoro` (`vendoro`),
  KEY `cliento` (`cliento`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`vendoro`) REFERENCES `vendors` (`idv`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`cliento`) REFERENCES `clientsv` (`idc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger` (
  `P_CODE` varchar(8) NOT NULL,
  `P_FIRST_NAME` varchar(30) NOT NULL,
  `P_LAST_NAME` varchar(30) NOT NULL,
  `P_PROFILE` varchar(30) NOT NULL,
  `P_DATE_BORN` date NOT NULL,
  `P_PHONE_NUMBER` varchar(15) NOT NULL,
  `statusPassenger` char(1) DEFAULT NULL,
  PRIMARY KEY (`P_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
INSERT INTO `passenger` VALUES ('p-001','Ana','García','Turista','1990-05-15','+123456789','A'),('p-002','Juan','López','Aventurero','1985-10-22','+987654321','A'),('p-003','María','Martínez','Relajación','1978-12-07','+111222333','A');
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `place`
--

DROP TABLE IF EXISTS `place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `place` (
  `L_CODE` varchar(8) NOT NULL,
  `L_NAME` varchar(30) NOT NULL,
  `L_TYPE` varchar(30) NOT NULL,
  `L_CLIMATE` varchar(30) NOT NULL,
  `L_TOTAL_INHABITANTS` int DEFAULT NULL,
  `L_DESCRIPTION` varchar(30) DEFAULT NULL,
  `statusPlace` char(1) DEFAULT NULL,
  PRIMARY KEY (`L_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `place`
--

LOCK TABLES `place` WRITE;
/*!40000 ALTER TABLE `place` DISABLE KEYS */;
INSERT INTO `place` VALUES ('1','París','Ciudad','Templado',2200000,'París es la capital...','A'),('2','Playa del Carmen','Playa','Cálido',150000,'Playa del Carmen...','A'),('3','Montañas Rocosas','Montaña','Frío',100000,'Las Montañas Rocosas...','A');
/*!40000 ALTER TABLE `place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip`
--

DROP TABLE IF EXISTS `trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip` (
  `V_CODE` varchar(8) NOT NULL,
  `V_PASSENGER` varchar(8) DEFAULT NULL,
  `V_PLACE` varchar(8) DEFAULT NULL,
  `V_DATE` date NOT NULL,
  `statusTrip` char(1) NOT NULL,
  PRIMARY KEY (`V_CODE`),
  KEY `V_PASSENGER` (`V_PASSENGER`),
  KEY `V_PLACE` (`V_PLACE`),
  CONSTRAINT `trip_ibfk_1` FOREIGN KEY (`V_PASSENGER`) REFERENCES `passenger` (`P_CODE`),
  CONSTRAINT `trip_ibfk_2` FOREIGN KEY (`V_PLACE`) REFERENCES `place` (`L_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip`
--

LOCK TABLES `trip` WRITE;
/*!40000 ALTER TABLE `trip` DISABLE KEYS */;
INSERT INTO `trip` VALUES ('1','p-001','2','2023-06-20','A'),('2','p-002','3','2023-08-10','A'),('3','p-002','1','2023-05-05','A');
/*!40000 ALTER TABLE `trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendors`
--

DROP TABLE IF EXISTS `vendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendors` (
  `idv` varchar(8) NOT NULL,
  `namev` varchar(20) NOT NULL,
  `lastnamev` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `comision` float NOT NULL,
  `statusv` char(1) NOT NULL,
  PRIMARY KEY (`idv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendors`
--

LOCK TABLES `vendors` WRITE;
/*!40000 ALTER TABLE `vendors` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'testx2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-21  8:55:16
