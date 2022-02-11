-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hospital` (
  `Nameoftablets` varchar(45) DEFAULT NULL,
  `Reference_NO` varchar(45) NOT NULL,
  `dose` varchar(45) DEFAULT NULL,
  `Numberoftablets` varchar(45) DEFAULT NULL,
  `lot` varchar(45) DEFAULT NULL,
  `issuedate` varchar(45) DEFAULT NULL,
  `expdate` varchar(45) DEFAULT NULL,
  `dailydose` varchar(45) DEFAULT NULL,
  `storage` varchar(45) DEFAULT NULL,
  `nhsnumber` varchar(45) DEFAULT NULL,
  `patientname` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `patientaddress` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Reference_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital`
--

LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` VALUES ('Acetaminophen','Ref1223','4','8','8787877','12-12-2020','12-12-2022','4','NO','Nh38778','Kamal','01-02-1997','Bingiriya'),('Ativan','Ref123','2','12','45','12-20','12-22','3','HOT','NH1234','Sumith','12-03-1997','bingiriya'),('Acetaminophen','Ref2334','4','8','8787877','12-12-2020','12-12-2022','4','NO','Nh38778','w.isuru dilshan','01-02-1997','Bingiriya');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-11 15:33:53
