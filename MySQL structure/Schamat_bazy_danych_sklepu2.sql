CREATE DATABASE  IF NOT EXISTS `sklep_internetowy` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `sklep_internetowy`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: sklep_internetowy
-- ------------------------------------------------------
-- Server version	8.0.15

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
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `inventory` (
  `product` varchar(15) DEFAULT NULL,
  `quantity` int(5) NOT NULL DEFAULT '0',
  `unit` set('kg','szt','m') NOT NULL,
  UNIQUE KEY `product` (`product`),
  UNIQUE KEY `product_2` (`product`),
  CONSTRAINT `product_inventory_FK` FOREIGN KEY (`product`) REFERENCES `products` (`name_p`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('słuchawki01',0,'szt'),('słuchawki02',17,'szt');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_header`
--

DROP TABLE IF EXISTS `order_header`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `order_header` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `customer` int(6) unsigned NOT NULL,
  `street_order` varchar(20) DEFAULT NULL,
  `city_order` varchar(20) DEFAULT NULL,
  `postal_code_order` varchar(6) DEFAULT NULL,
  `street_invoice` varchar(6) DEFAULT NULL,
  `city_invoice` varchar(6) DEFAULT NULL,
  `postal_code_invoice` varchar(6) DEFAULT NULL,
  `tax_number` varchar(15) DEFAULT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `State` set('Nowe','W realizacji','Wysłane','Zafakturowane','Zwrot') DEFAULT 'Nowe',
  `order_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `sent_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_customer_FK` (`customer`),
  CONSTRAINT `order_customer_FK` FOREIGN KEY (`customer`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_header`
--

LOCK TABLES `order_header` WRITE;
/*!40000 ALTER TABLE `order_header` DISABLE KEYS */;
INSERT INTO `order_header` VALUES (1,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-04-15 22:04:29','Wysłane','2019-04-16 22:14:54',NULL),(2,2,'PIEKNA 22','ŁUKÓW','21-400',NULL,NULL,NULL,'2456789898','2019-04-15 23:14:11','Nowe','2019-04-16 22:14:54',NULL);
/*!40000 ALTER TABLE `order_header` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `poprawa_danych_zamowienia` BEFORE INSERT ON `order_header` FOR EACH ROW begin
set new.street_order = upper(trim(new.street_order));
set new.street_invoice = upper(trim(new.street_invoice));
set new.city_order = upper(trim(new.city_order));
set new.city_invoice = upper(trim(new.city_invoice));
set new.postal_code_order = insert( replace(trim(new.postal_code_order),'-','') ,3,0,'-')  ;
set new.postal_code_invoice = insert( replace(trim(new.postal_code_invoice),'-','') ,3,0,'-')  ;
set new.tax_number = replace(trim(new.tax_number), '-',''); 

end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `order_header_lines_update_state` AFTER UPDATE ON `order_header` FOR EACH ROW begin
update order_lines set State = new.State where order_id_fk = new.id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `order_lines`
--

DROP TABLE IF EXISTS `order_lines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `order_lines` (
  `id` int(12) unsigned NOT NULL AUTO_INCREMENT,
  `order_id_fk` int(6) unsigned NOT NULL,
  `product_fk` varchar(15) NOT NULL,
  `quantity` int(5) NOT NULL DEFAULT '0',
  `unit` set('kg','szt','m') NOT NULL,
  `State` set('Nowe','W realizacji','Wysłane','Zafakturowane','Zwrot') DEFAULT 'Nowe',
  PRIMARY KEY (`id`,`order_id_fk`),
  KEY `order_id_FK` (`order_id_fk`),
  KEY `product_FK` (`product_fk`),
  CONSTRAINT `order_id_FK` FOREIGN KEY (`order_id_fk`) REFERENCES `order_header` (`id`),
  CONSTRAINT `product_FK` FOREIGN KEY (`product_fk`) REFERENCES `products` (`name_p`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_lines`
--

LOCK TABLES `order_lines` WRITE;
/*!40000 ALTER TABLE `order_lines` DISABLE KEYS */;
INSERT INTO `order_lines` VALUES (1,1,'słuchawki01',6,'szt','Wysłane'),(2,1,'słuchawki02',6,'szt','Wysłane');
/*!40000 ALTER TABLE `order_lines` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `inventory_update_after_order` AFTER UPDATE ON `order_lines` FOR EACH ROW begin
 if new.State = 'W realizacji' then


    update inventory set quantity = quantity - new.quantity where product =  new.product_fk;
 end if;
  if new.State = 'Zwrot' then


    update inventory set quantity = quantity + new.quantity where product =  new.product_fk;
 end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `product_categories`
--

DROP TABLE IF EXISTS `product_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `product_categories` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name_c` tinytext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_categories`
--

LOCK TABLES `product_categories` WRITE;
/*!40000 ALTER TABLE `product_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `products` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name_p` varchar(15) NOT NULL,
  `description_p` text,
  `price` int(6) DEFAULT NULL,
  `image` text,
  `category_id` int(6) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_p` (`name_p`),
  KEY `product_p_categories_FK` (`category_id`),
  CONSTRAINT `product_p_categories_FK` FOREIGN KEY (`category_id`) REFERENCES `product_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'słuchawki01',NULL,300,NULL,NULL),(2,'słuchawki02',NULL,300,NULL,NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name_u` tinytext NOT NULL,
  `surname_u` tinytext NOT NULL,
  `email` varchar(30) NOT NULL,
  `tax_number` int(10) DEFAULT NULL,
  `role_name` set('Admin','Seller','Customer') NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `postal_code` varchar(6) DEFAULT NULL,
  `pass` varchar(20) NOT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ariel','Semik','semikariel@gmail.com',NULL,'Admin','Długa 5','Warszawa','00-100','12345as','2019-04-15 22:05:22'),(2,'Piotr','Franciszek','piotrfranciszek@gmail.com',NULL,'Customer','Mała 5','Warszawa','00-100','12345as','2019-04-15 22:05:22');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `poprawa_danych_usera` BEFORE INSERT ON `users` FOR EACH ROW begin
set new.name_u = upper(trim(new.name_u));
set new.surname_u = upper(trim(new.surname_u));
set new.email = lower(trim(new.email));
set new.street = upper(trim(new.street));
set new.city = upper(trim(new.city));
set new.postal_code = insert( replace(trim(new.postal_code),'-','') ,3,0,'-')  ;

end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping events for database 'sklep_internetowy'
--

--
-- Dumping routines for database 'sklep_internetowy'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-27 15:40:43
