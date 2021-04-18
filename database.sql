-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: dbsatnam
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Perfil',7,'add_profile'),(26,'Can change Perfil',7,'change_profile'),(27,'Can delete Perfil',7,'delete_profile'),(28,'Can view Perfil',7,'view_profile'),(29,'Can add Categoria',8,'add_category'),(30,'Can change Categoria',8,'change_category'),(31,'Can delete Categoria',8,'delete_category'),(32,'Can view Categoria',8,'view_category'),(33,'Can add Video',9,'add_video'),(34,'Can change Video',9,'change_video'),(35,'Can delete Video',9,'delete_video'),(36,'Can view Video',9,'view_video'),(37,'Can add Categoria',10,'add_category'),(38,'Can change Categoria',10,'change_category'),(39,'Can delete Categoria',10,'delete_category'),(40,'Can view Categoria',10,'view_category'),(41,'Can add Post',11,'add_post'),(42,'Can change Post',11,'change_post'),(43,'Can delete Post',11,'delete_post'),(44,'Can view Post',11,'view_post'),(45,'Can add Página',12,'add_page'),(46,'Can change Página',12,'change_page'),(47,'Can delete Página',12,'delete_page'),(48,'Can view Página',12,'view_page'),(49,'Can add Paypal Plan',13,'add_paypal'),(50,'Can change Paypal Plan',13,'change_paypal'),(51,'Can delete Paypal Plan',13,'delete_paypal'),(52,'Can view Paypal Plan',13,'view_paypal'),(53,'Can add failed attempt',14,'add_failedattempt'),(54,'Can change failed attempt',14,'change_failedattempt'),(55,'Can delete failed attempt',14,'delete_failedattempt'),(56,'Can view failed attempt',14,'view_failedattempt'),(57,'Can add cron job log',15,'add_cronjoblog'),(58,'Can change cron job log',15,'change_cronjoblog'),(59,'Can delete cron job log',15,'delete_cronjoblog'),(60,'Can view cron job log',15,'view_cronjoblog');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (9,'pbkdf2_sha256$216000$ANaMhrrpxuhI$Rvc5OBEvOrGNL0kNGZP7lF7JiXTxEiqjopApF3g/SKo=','2021-04-18 02:16:54.279231',1,'oscar','','','oscara1706cl@gmail.com',1,1,'2021-02-07 18:35:13.543648'),(10,'pbkdf2_sha256$216000$XCubvuZmaIqK$rbaES0XLtlHABtW8ZAqKjHu+FD12uP/AIHLtmp1QPoU=','2021-02-15 03:32:28.195318',0,'Ricardo','Ricardo','macias','ricardo_macias@gmail.com',0,1,'2021-02-15 02:29:03.077992'),(11,'pbkdf2_sha256$216000$Xo8oZb44iiV1$xYny83a/q0z+gJ0Z1GNFWdyq8DUzIK0XOgCXfnTI4ho=','2021-04-18 02:17:30.537790',0,'arturo','Arturo','villas','artuo123@gmail.com',0,1,'2021-03-16 02:36:26.359587'),(12,'pbkdf2_sha256$216000$kKnapKfBJAWX$YzbNbPAUPG2lNBLAsd+ttqC6CTsI35Exw6lB4WhcP04=','2021-04-12 00:47:33.701602',0,'Pedro','Pedro','Juarez','pedro123@personal.example.com',0,1,'2021-04-12 00:47:26.265862');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brutebuster_failedattempt`
--

DROP TABLE IF EXISTS `brutebuster_failedattempt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brutebuster_failedattempt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `IP` char(39) DEFAULT NULL,
  `failures` int unsigned NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BruteBuster_failedattempt_username_IP_db227624_uniq` (`username`,`IP`),
  CONSTRAINT `brutebuster_failedattempt_chk_1` CHECK ((`failures` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brutebuster_failedattempt`
--

LOCK TABLES `brutebuster_failedattempt` WRITE;
/*!40000 ALTER TABLE `brutebuster_failedattempt` DISABLE KEYS */;
INSERT INTO `brutebuster_failedattempt` VALUES (1,'arturo','127.0.0.1',0,'2021-04-18 02:17:30.522163'),(2,'arturo123','127.0.0.1',1,'2021-04-12 00:10:06.424014'),(3,'asfsdaf','127.0.0.1',1,'2021-04-12 00:11:53.042300'),(4,'sfsafasdf','127.0.0.1',1,'2021-04-12 00:11:56.473173'),(5,'assdfsfas','127.0.0.1',1,'2021-04-12 00:12:00.032190'),(6,'asdfdfsfsd','127.0.0.1',1,'2021-04-12 00:12:03.370204'),(7,'asfsafsf','127.0.0.1',1,'2021-04-12 00:12:07.464189'),(8,'adfs','127.0.0.1',1,'2021-04-12 00:12:11.080221');
/*!40000 ALTER TABLE `brutebuster_failedattempt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (94,'2021-02-14 02:21:24.643590','5','Arturo',3,'',7,9),(95,'2021-02-14 17:10:08.595238','1','Plan mensual',1,'[{\"added\": {}}]',13,9),(96,'2021-02-14 17:10:29.507903','2','Plan Anual',1,'[{\"added\": {}}]',13,9),(97,'2021-02-14 17:34:06.623150','2','Plan Anual',3,'',13,9),(98,'2021-02-14 17:34:09.381194','1','Plan mensual',3,'',13,9),(99,'2021-02-14 18:39:11.498697','3','Plan mensual',1,'[{\"added\": {}}]',13,9),(100,'2021-02-14 18:41:36.572935','4','Plan Anual',1,'[{\"added\": {}}]',13,9),(101,'2021-02-14 18:41:44.770996','3','Plan mensual',2,'[]',13,9),(102,'2021-02-14 18:47:00.494611','3','Plan mensual',2,'[]',13,9),(103,'2021-02-14 18:47:06.015400','4','Plan Anual',2,'[]',13,9),(104,'2021-02-15 01:03:46.561114','6','Arturo',3,'',7,9),(105,'2021-02-15 02:41:31.505803','8','Ricardo',2,'[]',7,9),(106,'2021-02-15 02:55:46.571643','8','Ricardo',3,'',7,9),(107,'2021-02-15 02:59:32.072196','9','Ricardo',3,'',7,9),(108,'2021-02-15 03:09:46.473480','10','Ricardo',3,'',7,9),(109,'2021-02-15 03:21:46.169679','11','Ricardo',3,'',7,9),(110,'2021-02-15 03:24:20.785958','12','Ricardo',2,'[]',7,9),(111,'2021-02-15 03:25:34.868515','12','Ricardo',2,'[]',7,9),(112,'2021-02-15 03:30:36.999298','12','Ricardo',3,'',7,9),(113,'2021-03-16 02:31:18.417490','7','Arturo',3,'',7,9),(114,'2021-03-16 02:35:51.380262','8','Arturo',3,'',4,9),(115,'2021-03-16 02:56:59.414816','4','Mantras',1,'[{\"added\": {}}]',10,9),(116,'2021-03-16 02:58:34.438720','4','Mantras',2,'[]',10,9),(117,'2021-03-16 02:59:57.917632','4','Mantras',3,'',10,9),(118,'2021-03-16 03:00:07.035658','6','Mantras',1,'[{\"added\": {}}]',8,9),(119,'2021-03-16 03:20:26.815258','5','video perron de prueba',1,'[{\"added\": {}}]',9,9),(120,'2021-04-18 02:17:06.641473','5','video perron de prueba',3,'',9,9);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(14,'BruteBuster','failedattempt'),(5,'contenttypes','contenttype'),(15,'django_cron','cronjoblog'),(12,'pages','page'),(13,'payments','paypal'),(10,'posts','category'),(11,'posts','post'),(6,'sessions','session'),(7,'users','profile'),(8,'videos','category'),(9,'videos','video');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_cron_cronjoblog`
--

DROP TABLE IF EXISTS `django_cron_cronjoblog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_cron_cronjoblog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(64) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `is_success` tinyint(1) NOT NULL,
  `message` longtext NOT NULL,
  `ran_at_time` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `django_cron_cronjoblog_code_start_time_ran_at_time_8b50b8fa_idx` (`code`,`start_time`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_is_success_ran_at_time_84da9606_idx` (`code`,`is_success`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_start_time_4fc78f9d_idx` (`code`,`start_time`),
  KEY `django_cron_cronjoblog_code_48865653` (`code`),
  KEY `django_cron_cronjoblog_start_time_d68c0dd9` (`start_time`),
  KEY `django_cron_cronjoblog_end_time_7918602a` (`end_time`),
  KEY `django_cron_cronjoblog_ran_at_time_7fed2751` (`ran_at_time`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_cron_cronjoblog`
--

LOCK TABLES `django_cron_cronjoblog` WRITE;
/*!40000 ALTER TABLE `django_cron_cronjoblog` DISABLE KEYS */;
INSERT INTO `django_cron_cronjoblog` VALUES (1,'payments.MyCronJob','2021-04-18 01:40:34.286060','2021-04-18 01:40:34.337071',1,'',NULL);
/*!40000 ALTER TABLE `django_cron_cronjoblog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-01-11 01:48:04.488905'),(2,'auth','0001_initial','2021-01-11 01:48:04.629936'),(3,'admin','0001_initial','2021-01-11 01:48:04.879964'),(4,'admin','0002_logentry_remove_auto_add','2021-01-11 01:48:04.983405'),(5,'admin','0003_logentry_add_action_flag_choices','2021-01-11 01:48:04.989038'),(6,'contenttypes','0002_remove_content_type_name','2021-01-11 01:48:05.044745'),(7,'auth','0002_alter_permission_name_max_length','2021-01-11 01:48:05.077538'),(8,'auth','0003_alter_user_email_max_length','2021-01-11 01:48:05.093541'),(9,'auth','0004_alter_user_username_opts','2021-01-11 01:48:05.099543'),(10,'auth','0005_alter_user_last_login_null','2021-01-11 01:48:05.128554'),(11,'auth','0006_require_contenttypes_0002','2021-01-11 01:48:05.131648'),(12,'auth','0007_alter_validators_add_error_messages','2021-01-11 01:48:05.136557'),(13,'auth','0008_alter_user_username_max_length','2021-01-11 01:48:05.184551'),(14,'auth','0009_alter_user_last_name_max_length','2021-01-11 01:48:05.219597'),(15,'auth','0010_alter_group_name_max_length','2021-01-11 01:48:05.232600'),(16,'auth','0011_update_proxy_permissions','2021-01-11 01:48:05.238034'),(17,'auth','0012_alter_user_first_name_max_length','2021-01-11 01:48:05.343900'),(18,'posts','0001_initial','2021-01-11 01:48:05.389402'),(19,'sessions','0001_initial','2021-01-11 01:48:05.485234'),(20,'users','0001_initial','2021-01-11 01:48:05.513829'),(21,'videos','0001_initial','2021-01-11 01:48:05.588801'),(22,'posts','0002_auto_20210110_2046','2021-01-11 02:46:32.344655'),(23,'videos','0002_video_free_seen','2021-01-24 18:17:35.921676'),(24,'videos','0003_auto_20210131_1737','2021-01-31 23:37:19.820698'),(25,'posts','0003_auto_20210201_1218','2021-02-01 18:18:20.852814'),(26,'pages','0001_initial','2021-02-02 02:16:50.906997'),(27,'users','0002_auto_20210207_1124','2021-02-07 17:34:51.046255'),(28,'users','0003_auto_20210207_1134','2021-02-07 17:34:51.122272'),(29,'users','0004_profile_paypalplanid','2021-02-14 04:49:10.683059'),(30,'payments','0001_initial','2021-02-14 16:57:24.198790'),(31,'users','0005_auto_20210214_1057','2021-02-14 16:57:24.205790'),(32,'payments','0002_paypal_image','2021-02-14 17:35:47.329934'),(33,'payments','0003_paypal_sku','2021-02-14 17:39:27.685544'),(34,'payments','0004_paypal_description','2021-02-14 17:49:44.171756'),(35,'users','0006_auto_20210214_1852','2021-02-15 00:52:53.923436'),(36,'users','0007_auto_20210214_1856','2021-02-15 00:57:01.373696'),(37,'users','0008_auto_20210214_1857','2021-02-15 00:57:35.274458'),(38,'users','0009_auto_20210214_1900','2021-02-15 01:00:58.965642'),(39,'users','0010_auto_20210214_2138','2021-02-15 03:38:25.792655'),(40,'users','0011_auto_20210214_2142','2021-02-15 03:42:51.443886'),(41,'users','0012_auto_20210214_2144','2021-02-15 03:44:31.172776'),(42,'users','0013_auto_20210221_1747','2021-02-21 23:47:40.364880'),(43,'users','0014_auto_20210221_1753','2021-02-21 23:53:12.341219'),(44,'users','0015_profile_paypal_cancel_date','2021-03-08 22:50:56.721820'),(45,'users','0016_auto_20210315_2035','2021-03-16 02:35:16.194442'),(46,'django_cron','0001_initial','2021-04-18 01:35:29.540837'),(47,'django_cron','0002_remove_max_length_from_CronJobLog_message','2021-04-18 01:35:29.607448');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4da4upygix9of17a1bqmotnx7vz4wirr','.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkFdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRvzWidxlTKYjFQkBHWIQErRQQkXQqYU5-UoqC1sY5MILsJNELYYJ1nr0_MnM4mg:1lLzP7:MRyn_K-4TcLxX20JFSAyKvQUN-h49rBsOiK8aJEjRAw','2021-03-30 02:25:53.872129'),('5ew5t81irlj5gn3k9zd0n597ba11zemk','.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkFdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRvzWidxlTKYjFQkBHWIQErRQQkXQqYU5-UoqC1sY5MILsJNELYYJ1nr0_MnM4mg:1lDyJ4:R5kr7hF7iFXfEDmNIbYP9mGP0PL0hgam19YxlDAdWqE','2021-03-07 23:38:30.339862'),('5hcc4z0fsq1pxr6bu9w3h7hgjjr6td4q','.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkFdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRvzWidxlTKYjFQkBHWIQErRQQkXQqYU5-UoqC1sY5MILsJNELYYJ1nr0_MnM4mg:1lBNCF:4U5AjJ_pyyUGxy6RhOGQEGN2o5M3V0-bOR0fBc_IIzI','2021-02-28 19:36:43.341223'),('5ifaogzs6rgeipihmvg47svg358aq24b','.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkFdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRvzWidxlTKYjFQkBHWIQErRQQkXQqYU5-UoqC1sY5MILsJNELYYJ1nr0_MnM4mg:1lBUdS:PIPZLTm5JIA49iR9GRlDoS5yspmWg9FPya9768asJNM','2021-03-01 03:33:18.870274'),('5ik5c4vhz7jt1shw5xef8jg5yyigp4pz','.eJxVjEsOwjAMBe-SNYritLEFS_acobJjhxRQK_Wzqrg7VOoCtm9m3uY6XpfarbNNXa_u4gDc6XcUzk8bdqIPHu6jz-OwTL34XfEHnf1tVHtdD_fvoPJcv7WUBmMhS4VJEIEpFwPFQJEVoWm1hSCkbBIknjUzIAejhCkSq7n3ByUsONw:1lXx06:16ATj5VLMGM2-hehGazgesSLjuS75WC45H0rB24_yFQ','2021-05-02 02:17:30.537790'),('85orao57gynh23mq27u0t9md04r5fu3j','.eJxVjEsOwjAMBe-SNYritLEFS_acobJjhxRQK_Wzqrg7VOoCtm9m3uY6XpfarbNNXa_u4gDc6XcUzk8bdqIPHu6jz-OwTL34XfEHnf1tVHtdD_fvoPJcv7WUBmMhS4VJEIEpFwPFQJEVoWm1hSCkbBIknjUzIAejhCkSq7n3ByUsONw:1lM0TH:qTeG3YmGRqRSfxWQU_qJg8hP9iWxC3-yWj5K7a9JbDA','2021-03-30 03:34:15.771567'),('8wlac9zfm5fcbp3ofxnhp2tfjwnrcmvl','.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkFdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRvzWidxlTKYjFQkBHWIQErRQQkXQqYU5-UoqC1sY5MILsJNELYYJ1nr0_MnM4mg:1lVkGs:cub7MDzRzLEyji08YM4E--AFMByDIEUSTPlsRqtMXlY','2021-04-26 00:17:42.976837'),('jpguoqudcjz519usayviwehan1arpc4k','.eJxVjDsOwjAQBe_iGln-CbyU9JzB8np3cQDZUpxUiLtDpBTQvpl5L5XyutS0Dp7TROqsrFGH3xFzeXDbCN1zu3VdelvmCfWm6J0Ofe3Ez8vu_h3UPOq3Dh6JgSwb7wo6KwadCxkisY3HQkJeIASDBAJgJaIpJ3HiTXAMwav3BxvDOGI:1lBUce:WvoDVTLpoWxuW5TJSFhzZZNKlSIHEpRhoTSPAYzj6T0','2021-03-01 03:32:28.197738'),('ozzwp9j003welvugdukjsuqk0rzmo8oy','.eJxVjMsOwiAQRf-FtSFQ3i7d-w1kBgapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKc2ZkFdvrdENKD2g7yHdqt89TbuszId4UfdPBrz_S8HO7fQYVRvzWidxlTKYjFQkBHWIQErRQQkXQqYU5-UoqC1sY5MILsJNELYYJ1nr0_MnM4mg:1lJ5RZ:39QwZkMgc05B7h4yST8U_PtqBMcRmriODjlvlrCkZ7A','2021-03-22 02:16:25.817117');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_page`
--

DROP TABLE IF EXISTS `pages_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_page` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `order` smallint NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_page`
--

LOCK TABLES `pages_page` WRITE;
/*!40000 ALTER TABLE `pages_page` DISABLE KEYS */;
/*!40000 ALTER TABLE `pages_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments_paypal`
--

DROP TABLE IF EXISTS `payments_paypal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments_paypal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `paypalPlanId` varchar(255) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `SKU` varchar(100) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments_paypal`
--

LOCK TABLES `payments_paypal` WRITE;
/*!40000 ALTER TABLE `payments_paypal` DISABLE KEYS */;
INSERT INTO `payments_paypal` VALUES (3,'Plan mensual','P-68F698811G6881503MAO7MSY','2021-02-14 18:39:11.497388','2021-02-14 18:47:00.474602','plans/plan_mensual.jpeg','PLAN_MENSUAL','plan mensual de satnam Yoga'),(4,'Plan Anual','P-38Y47380P0096173EMAPUM2I','2021-02-14 18:41:36.570934','2021-02-14 18:47:06.014400','plans/plan_anual.jpg','PLAN_ANUAL','Plan para yoga todo el año');
/*!40000 ALTER TABLE `payments_paypal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts_category`
--

DROP TABLE IF EXISTS `posts_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts_category`
--

LOCK TABLES `posts_category` WRITE;
/*!40000 ALTER TABLE `posts_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts_post`
--

DROP TABLE IF EXISTS `posts_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts_post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `published` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `author_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `posts_post_author_id_fe5487bf_fk_auth_user_id` (`author_id`),
  CONSTRAINT `posts_post_author_id_fe5487bf_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts_post`
--

LOCK TABLES `posts_post` WRITE;
/*!40000 ALTER TABLE `posts_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts_post_categories`
--

DROP TABLE IF EXISTS `posts_post_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts_post_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `post_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `posts_post_categories_post_id_category_id_00bce8d0_uniq` (`post_id`,`category_id`),
  KEY `posts_post_categories_category_id_159f5c54_fk_posts_category_id` (`category_id`),
  CONSTRAINT `posts_post_categories_category_id_159f5c54_fk_posts_category_id` FOREIGN KEY (`category_id`) REFERENCES `posts_category` (`id`),
  CONSTRAINT `posts_post_categories_post_id_0ca7af15_fk_posts_post_id` FOREIGN KEY (`post_id`) REFERENCES `posts_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts_post_categories`
--

LOCK TABLES `posts_post_categories` WRITE;
/*!40000 ALTER TABLE `posts_post_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts_post_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile`
--

DROP TABLE IF EXISTS `users_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `active` varchar(20) NOT NULL,
  `stripeCustomerId` varchar(255) DEFAULT NULL,
  `stripeSubscriptionId` varchar(255) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `paypalSubscriptionId` varchar(255) DEFAULT NULL,
  `paypalPlanId` varchar(255) DEFAULT NULL,
  `paypal_cancel_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `users_profile_user_id_2112e78d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile`
--

LOCK TABLES `users_profile` WRITE;
/*!40000 ALTER TABLE `users_profile` DISABLE KEYS */;
INSERT INTO `users_profile` VALUES (13,'user_images/3d9e22075d80221e19d0391d75f54e47.jpg','4535353534535','A','cus_IwrXBU7jrpw5c5','sub_IwrXVUqzSspQ9b','2021-02-15 03:31:29.709510','2021-02-15 03:44:42.184934',10,NULL,NULL,NULL),(15,'user_images/8jfvwuu7vmc11.jpg','11531615','statusChoices.ACTIVE',NULL,NULL,'2021-04-11 23:43:48.634752','2021-04-11 23:49:11.179378',11,'I-E90SUPBJK99S','P-68F698811G6881503MAO7MSY',NULL),(16,'user_images/git-init-git.jpg','1234567851','statusChoices.ACTIVE',NULL,NULL,'2021-04-12 00:48:36.627263','2021-04-12 00:49:01.962611',12,'I-BWC67V13086S','P-38Y47380P0096173EMAPUM2I',NULL);
/*!40000 ALTER TABLE `users_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos_category`
--

DROP TABLE IF EXISTS `videos_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos_category`
--

LOCK TABLES `videos_category` WRITE;
/*!40000 ALTER TABLE `videos_category` DISABLE KEYS */;
INSERT INTO `videos_category` VALUES (6,'Mantras','2021-03-16 03:00:06.995426','2021-03-16 03:00:06.995426');
/*!40000 ALTER TABLE `videos_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos_video`
--

DROP TABLE IF EXISTS `videos_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos_video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `upload` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `free_seen` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos_video`
--

LOCK TABLES `videos_video` WRITE;
/*!40000 ALTER TABLE `videos_video` DISABLE KEYS */;
/*!40000 ALTER TABLE `videos_video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos_video_categories`
--

DROP TABLE IF EXISTS `videos_video_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos_video_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `video_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `videos_video_categories_video_id_category_id_3aead81e_uniq` (`video_id`,`category_id`),
  KEY `videos_video_categor_category_id_7e04058d_fk_videos_ca` (`category_id`),
  CONSTRAINT `videos_video_categor_category_id_7e04058d_fk_videos_ca` FOREIGN KEY (`category_id`) REFERENCES `videos_category` (`id`),
  CONSTRAINT `videos_video_categories_video_id_65ca1df7_fk_videos_video_id` FOREIGN KEY (`video_id`) REFERENCES `videos_video` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos_video_categories`
--

LOCK TABLES `videos_video_categories` WRITE;
/*!40000 ALTER TABLE `videos_video_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `videos_video_categories` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-18 12:32:50
