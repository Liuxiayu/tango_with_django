-- MySQL dump 10.13  Distrib 5.7.31, for macos10.14 (x86_64)
--
-- Host: localhost    Database: my_blogs
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `my_blogs`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `my_blogs` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `my_blogs`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 用户',6,'add_userinfo'),(22,'Can change 用户',6,'change_userinfo'),(23,'Can delete 用户',6,'delete_userinfo'),(24,'Can view 用户',6,'view_userinfo'),(25,'Can add 文章',7,'add_article'),(26,'Can change 文章',7,'change_article'),(27,'Can delete 文章',7,'delete_article'),(28,'Can view 文章',7,'view_article'),(29,'Can add blog站点',8,'add_blog'),(30,'Can change blog站点',8,'change_blog'),(31,'Can delete blog站点',8,'delete_blog'),(32,'Can view blog站点',8,'view_blog'),(33,'Can add index_page',9,'add_index_page'),(34,'Can change index_page',9,'change_index_page'),(35,'Can delete index_page',9,'delete_index_page'),(36,'Can view index_page',9,'view_index_page'),(37,'Can add 标签',10,'add_tag'),(38,'Can change 标签',10,'change_tag'),(39,'Can delete 标签',10,'delete_tag'),(40,'Can view 标签',10,'view_tag'),(41,'Can add read',11,'add_read'),(42,'Can change read',11,'change_read'),(43,'Can delete read',11,'delete_read'),(44,'Can view read',11,'view_read'),(45,'Can add 评论',12,'add_comment'),(46,'Can change 评论',12,'change_comment'),(47,'Can delete 评论',12,'delete_comment'),(48,'Can view 评论',12,'view_comment'),(49,'Can add 文章分类',13,'add_category'),(50,'Can change 文章分类',13,'change_category'),(51,'Can delete 文章分类',13,'delete_category'),(52,'Can view 文章分类',13,'view_category'),(53,'Can add 文章详情',14,'add_articledetail'),(54,'Can change 文章详情',14,'change_articledetail'),(55,'Can delete 文章详情',14,'delete_articledetail'),(56,'Can view 文章详情',14,'view_articledetail'),(57,'Can add 文章-标签',15,'add_article2tag'),(58,'Can change 文章-标签',15,'change_article2tag'),(59,'Can delete 文章-标签',15,'delete_article2tag'),(60,'Can view 文章-标签',15,'view_article2tag'),(61,'Can add 文章点赞',16,'add_articleupdown'),(62,'Can change 文章点赞',16,'change_articleupdown'),(63,'Can delete 文章点赞',16,'delete_articleupdown'),(64,'Can view 文章点赞',16,'view_articleupdown');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article`
--

DROP TABLE IF EXISTS `blog_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_article` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8 NOT NULL,
  `desc` varchar(255) CHARACTER SET utf8 NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `comment_count` int(11) NOT NULL,
  `up_count` int(11) NOT NULL,
  `down_count` int(11) NOT NULL,
  `read_num` int(11) NOT NULL,
  `today_read_num` int(11) NOT NULL,
  `category_read_num` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_article_category_id_7e38f15e_fk_blog_category_nid` (`category_id`),
  KEY `blog_article_user_id_5beb0cc1_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `blog_article_category_id_7e38f15e_fk_blog_category_nid` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`nid`),
  CONSTRAINT `blog_article_user_id_5beb0cc1_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article`
--

LOCK TABLES `blog_article` WRITE;
/*!40000 ALTER TABLE `blog_article` DISABLE KEYS */;
INSERT INTO `blog_article` VALUES (1,'linux测试文章','CPU方面 处理器指标 CPU使用率: 每个处理器的利用率 user time: CPU执行用户代码的时间，包括nice time system time: CPU执行内核代码的时间，包括IRQ和softirq time waiting: CPU等待IO的时间 Idle time: CPU空闲并等待任务的时间 nice time: CPU花在改变进程优先级以及执行顺序的时间 load average: 任务队列中，等待被CPU执行的任务的总数，以及那些等待不可中断任务完成的任务的总数，它们的平均值。也就是','2021-04-25 17:13:07.123511',0,0,0,40,37,37,1,3),(2,'docker测试文章2','docker测试文章2的详情','2021-04-25 17:21:21.935066',0,1,0,4,1,1,2,3),(4,'aaaaaa','                aaaaa    \r\n		## bbbb\r\n    \r\n    ...','2021-04-25 19:03:26.187467',0,0,0,7,6,6,1,3),(5,'markdown测试日记','  哈哈哈这是我的博客\r\n  ### 嗷嗷\r\n  \r\n  \r\n  ``` echo \" test \"```\r\n  \r\n  \r\n  \r\n  \r\n  \r\n  ...','2021-04-25 20:17:38.583988',0,0,0,5,4,4,1,3),(7,'markdown测试日记3','\r\n\r\n\r\n### 我爱你\r\n```yibuxiaoxin 爱```\r\n...','2021-04-26 01:13:27.159555',0,0,0,3,3,3,1,3);
/*!40000 ALTER TABLE `blog_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article2tag`
--

DROP TABLE IF EXISTS `blog_article2tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_article2tag` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `blog_article2tag_article_id_tag_id_b0745f42_uniq` (`article_id`,`tag_id`),
  KEY `blog_article2tag_tag_id_389b9a96_fk_blog_tag_nid` (`tag_id`),
  CONSTRAINT `blog_article2tag_article_id_753a2b60_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`),
  CONSTRAINT `blog_article2tag_tag_id_389b9a96_fk_blog_tag_nid` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article2tag`
--

LOCK TABLES `blog_article2tag` WRITE;
/*!40000 ALTER TABLE `blog_article2tag` DISABLE KEYS */;
INSERT INTO `blog_article2tag` VALUES (1,1,1);
/*!40000 ALTER TABLE `blog_article2tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_articledetail`
--

DROP TABLE IF EXISTS `blog_articledetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_articledetail` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8 NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `article_id` (`article_id`),
  CONSTRAINT `blog_articledetail_article_id_56993a97_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_articledetail`
--

LOCK TABLES `blog_articledetail` WRITE;
/*!40000 ALTER TABLE `blog_articledetail` DISABLE KEYS */;
INSERT INTO `blog_articledetail` VALUES (2,'                aaaaa    \r\n		## bbbb\r\n    \r\n    ',4),(3,'  哈哈哈这是我的博客\r\n  ### 嗷嗷\r\n  \r\n  \r\n  ``` echo \" test \"```\r\n  \r\n  \r\n  \r\n  \r\n  \r\n  ',5),(5,'\r\n\r\n\r\n### 我爱你\r\n```yibuxiaoxin 爱```\r\n',7);
/*!40000 ALTER TABLE `blog_articledetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_articleupdown`
--

DROP TABLE IF EXISTS `blog_articleupdown`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_articleupdown` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `is_up` tinyint(1) NOT NULL,
  `article_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `blog_articleupdown_article_id_user_id_fa3d0c08_uniq` (`article_id`,`user_id`),
  KEY `blog_articleupdown_user_id_2c0ebe49_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `blog_articleupdown_article_id_9be1a8a2_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`),
  CONSTRAINT `blog_articleupdown_user_id_2c0ebe49_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_articleupdown`
--

LOCK TABLES `blog_articleupdown` WRITE;
/*!40000 ALTER TABLE `blog_articleupdown` DISABLE KEYS */;
INSERT INTO `blog_articleupdown` VALUES (1,1,2,3);
/*!40000 ALTER TABLE `blog_articleupdown` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blog`
--

DROP TABLE IF EXISTS `blog_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blog` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) CHARACTER SET utf8 NOT NULL,
  `site` varchar(32) CHARACTER SET utf8 DEFAULT NULL,
  `theme` varchar(32) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `site` (`site`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blog`
--

LOCK TABLES `blog_blog` WRITE;
/*!40000 ALTER TABLE `blog_blog` DISABLE KEYS */;
INSERT INTO `blog_blog` VALUES (1,'xiayu_title','xiayu_site','xiayu_theme');
/*!40000 ALTER TABLE `blog_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category`
--

DROP TABLE IF EXISTS `blog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_category` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8 NOT NULL,
  `rate` decimal(4,2) DEFAULT NULL,
  `process_color` varchar(32) CHARACTER SET utf8 DEFAULT NULL,
  `category_color` varchar(32) CHARACTER SET utf8 DEFAULT NULL,
  `blog_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_category_blog_id_80f0723a_fk_blog_blog_nid` (`blog_id`),
  CONSTRAINT `blog_category_blog_id_80f0723a_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category`
--

LOCK TABLES `blog_category` WRITE;
/*!40000 ALTER TABLE `blog_category` DISABLE KEYS */;
INSERT INTO `blog_category` VALUES (1,'Linux',85.71,'red','label-primary',1),(2,'docker',14.29,'green','label-primary',1),(3,'测试',0.00,NULL,'label-primary',1);
/*!40000 ALTER TABLE `blog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_comment`
--

DROP TABLE IF EXISTS `blog_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_comment` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8 NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `article_id` int(11) NOT NULL,
  `parent_comment_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_comment_article_id_3d58bca6_fk_blog_article_nid` (`article_id`),
  KEY `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_nid` (`parent_comment_id`),
  KEY `blog_comment_user_id_59a54155_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `blog_comment_article_id_3d58bca6_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`),
  CONSTRAINT `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_nid` FOREIGN KEY (`parent_comment_id`) REFERENCES `blog_comment` (`nid`),
  CONSTRAINT `blog_comment_user_id_59a54155_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_comment`
--

LOCK TABLES `blog_comment` WRITE;
/*!40000 ALTER TABLE `blog_comment` DISABLE KEYS */;
INSERT INTO `blog_comment` VALUES (1,'<input type=\"text\" id=\"textinput\" style=\"display: none\"><p>1</p>','2021-04-25 17:21:57.835089',2,NULL,3);
/*!40000 ALTER TABLE `blog_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_index_page`
--

DROP TABLE IF EXISTS `blog_index_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_index_page` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `visit_num` int(11) NOT NULL,
  `visit_time` date DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_index_page`
--

LOCK TABLES `blog_index_page` WRITE;
/*!40000 ALTER TABLE `blog_index_page` DISABLE KEYS */;
INSERT INTO `blog_index_page` VALUES (1,1,'2021-04-25'),(2,1,'2021-04-25'),(3,1,'2021-04-25'),(4,1,'2021-04-25'),(5,1,'2021-04-25'),(6,1,'2021-04-25'),(7,1,'2021-04-25'),(8,1,'2021-04-25'),(9,1,'2021-04-25'),(10,1,'2021-04-25'),(11,1,'2021-04-25'),(12,1,'2021-04-25'),(13,1,'2021-04-25'),(14,1,'2021-04-25'),(15,1,'2021-04-25'),(16,1,'2021-04-25'),(17,1,'2021-04-25'),(18,1,'2021-04-25'),(19,1,'2021-04-25'),(20,1,'2021-04-25'),(21,1,'2021-04-25'),(22,1,'2021-04-25'),(23,1,'2021-04-25'),(24,1,'2021-04-25'),(25,1,'2021-04-25'),(26,1,'2021-04-25'),(27,1,'2021-04-25'),(28,1,'2021-04-25'),(29,1,'2021-04-25'),(30,1,'2021-04-25'),(31,1,'2021-04-25'),(32,1,'2021-04-25'),(33,1,'2021-04-25'),(34,1,'2021-04-25'),(35,1,'2021-04-25'),(36,1,'2021-04-25'),(37,1,'2021-04-25'),(38,1,'2021-04-25'),(39,1,'2021-04-25'),(40,1,'2021-04-25'),(41,1,'2021-04-25'),(42,1,'2021-04-25'),(43,1,'2021-04-25'),(44,1,'2021-04-25'),(45,1,'2021-04-25'),(46,1,'2021-04-26'),(47,1,'2021-04-26'),(48,1,'2021-04-26'),(49,1,'2021-04-26'),(50,1,'2021-04-26'),(51,1,'2021-04-26'),(52,1,'2021-04-26'),(53,1,'2021-04-26'),(54,1,'2021-04-26'),(55,1,'2021-04-26');
/*!40000 ALTER TABLE `blog_index_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_read`
--

DROP TABLE IF EXISTS `blog_read`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_read` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `read_num` int(11) NOT NULL,
  `read_time` date NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_read_article_id_e1e8fd7e_fk_blog_article_nid` (`article_id`),
  CONSTRAINT `blog_read_article_id_e1e8fd7e_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_read`
--

LOCK TABLES `blog_read` WRITE;
/*!40000 ALTER TABLE `blog_read` DISABLE KEYS */;
INSERT INTO `blog_read` VALUES (1,1,'2021-04-25',1),(2,1,'2021-04-25',1),(3,1,'2021-04-25',2),(4,1,'2021-04-25',2),(5,1,'2021-04-25',2),(7,1,'2021-04-25',1),(9,1,'2021-04-25',4),(11,1,'2021-04-25',5),(12,1,'2021-04-26',1),(13,1,'2021-04-26',2),(20,1,'2021-04-26',1),(21,1,'2021-04-26',1),(22,1,'2021-04-26',1),(40,1,'2021-04-26',7),(41,1,'2021-04-26',1),(42,1,'2021-04-26',1),(43,1,'2021-04-26',1),(44,1,'2021-04-26',1),(45,1,'2021-04-26',1),(46,1,'2021-04-26',1),(47,1,'2021-04-26',1),(48,1,'2021-04-26',1),(49,1,'2021-04-26',1),(50,1,'2021-04-26',1),(51,1,'2021-04-26',1),(52,1,'2021-04-26',1),(53,1,'2021-04-26',1),(54,1,'2021-04-26',1),(55,1,'2021-04-26',1),(56,1,'2021-04-26',1),(57,1,'2021-04-26',1),(58,1,'2021-04-26',1),(59,1,'2021-04-26',1),(60,1,'2021-04-26',1),(61,1,'2021-04-26',1),(62,1,'2021-04-26',1),(63,1,'2021-04-26',1),(64,1,'2021-04-26',1),(65,1,'2021-04-26',1),(66,1,'2021-04-26',1),(67,1,'2021-04-26',1),(68,1,'2021-04-26',1),(69,1,'2021-04-26',1),(70,1,'2021-04-26',1),(71,1,'2021-04-26',1),(72,1,'2021-04-26',1),(73,1,'2021-04-26',1),(74,1,'2021-04-26',7),(76,1,'2021-04-26',7),(77,1,'2021-04-26',4),(78,1,'2021-04-26',4),(79,1,'2021-04-26',4),(80,1,'2021-04-26',4),(81,1,'2021-04-26',4),(82,1,'2021-04-26',4),(83,1,'2021-04-26',5),(84,1,'2021-04-26',5),(85,1,'2021-04-26',5),(86,1,'2021-04-26',5);
/*!40000 ALTER TABLE `blog_read` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_tag`
--

DROP TABLE IF EXISTS `blog_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_tag` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8 NOT NULL,
  `blog_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_tag_blog_id_a8c60c42_fk_blog_blog_nid` (`blog_id`),
  CONSTRAINT `blog_tag_blog_id_a8c60c42_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_tag`
--

LOCK TABLES `blog_tag` WRITE;
/*!40000 ALTER TABLE `blog_tag` DISABLE KEYS */;
INSERT INTO `blog_tag` VALUES (1,'系统',1);
/*!40000 ALTER TABLE `blog_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_userinfo`
--

DROP TABLE IF EXISTS `blog_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_userinfo` (
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
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) DEFAULT NULL,
  `avatar` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `blog_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `blog_id` (`blog_id`),
  CONSTRAINT `blog_userinfo_blog_id_aa34488f_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_userinfo`
--

LOCK TABLES `blog_userinfo` WRITE;
/*!40000 ALTER TABLE `blog_userinfo` DISABLE KEYS */;
INSERT INTO `blog_userinfo` VALUES ('pbkdf2_sha256$260000$YNrVKP0pXWznfayBwNkyMH$sa15vzdpexxMamzL722+jC8kxypapVupY4YbjhdtkSA=','2021-04-26 10:59:59.938088',1,'root','','','',1,1,'2021-04-25 16:58:52.835728',1,NULL,'avatars/default.png','2021-04-25 16:58:53.058545',NULL),('pbkdf2_sha256$260000$0In0quJT19hROj7ozjONGt$0G73j6IlmOIb58GpOngJyiH/D4ElA2zIssUj555nUYA=','2021-04-26 11:00:28.028129',1,'xiayu','','','876833129@qq.com',1,1,'2021-04-25 18:11:00.000000',3,'18150379247','avatars/学习-表情包.png','2021-04-25 18:11:51.554356',1);
/*!40000 ALTER TABLE `blog_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_userinfo_groups`
--

DROP TABLE IF EXISTS `blog_userinfo_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_userinfo_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_userinfo_groups_userinfo_id_group_id_5f60ecec_uniq` (`userinfo_id`,`group_id`),
  KEY `blog_userinfo_groups_group_id_1fb5e93a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `blog_userinfo_groups_group_id_1fb5e93a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `blog_userinfo_groups_userinfo_id_f6f0498b_fk_blog_userinfo_nid` FOREIGN KEY (`userinfo_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_userinfo_groups`
--

LOCK TABLES `blog_userinfo_groups` WRITE;
/*!40000 ALTER TABLE `blog_userinfo_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_userinfo_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_userinfo_user_permissions`
--

DROP TABLE IF EXISTS `blog_userinfo_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_userinfo_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_userinfo_user_permi_userinfo_id_permission_i_7d343093_uniq` (`userinfo_id`,`permission_id`),
  KEY `blog_userinfo_user_p_permission_id_ace80f7e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `blog_userinfo_user_p_permission_id_ace80f7e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `blog_userinfo_user_p_userinfo_id_57e76697_fk_blog_user` FOREIGN KEY (`userinfo_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_userinfo_user_permissions`
--

LOCK TABLES `blog_userinfo_user_permissions` WRITE;
/*!40000 ALTER TABLE `blog_userinfo_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_userinfo_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-04-25 17:08:02.861618','1','liuxiayu_title',1,'[{\"added\": {}}]',8,1),(2,'2021-04-25 17:08:31.534336','2','liuxiayu',1,'[{\"added\": {}}]',6,1),(3,'2021-04-25 17:13:01.473953','1','Linux',1,'[{\"added\": {}}]',13,1),(4,'2021-04-25 17:13:07.124391','1','linux测试文章',1,'[{\"added\": {}}]',7,1),(5,'2021-04-25 17:14:09.100841','1','Linux',2,'[{\"changed\": {\"fields\": [\"Rate\"]}}]',13,1),(6,'2021-04-25 17:20:39.203919','1','Linux',2,'[{\"changed\": {\"fields\": [\"Rate\"]}}]',13,1),(7,'2021-04-25 17:21:18.612149','2','docker',1,'[{\"added\": {}}]',13,1),(8,'2021-04-25 17:21:21.935771','2','docker测试文章2',1,'[{\"added\": {}}]',7,1),(9,'2021-04-25 18:17:25.932044','1','xiayu_title',2,'[{\"changed\": {\"fields\": [\"Title\", \"Site\", \"Theme\"]}}]',8,3),(10,'2021-04-25 18:17:32.312725','2','docker测试文章2',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',7,3),(11,'2021-04-25 18:17:39.287709','2','docker测试文章2',2,'[]',7,3),(12,'2021-04-25 18:17:44.286054','1','linux测试文章',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',7,3),(13,'2021-04-25 18:18:08.387469','1','系统',1,'[{\"added\": {}}]',10,3),(14,'2021-04-25 18:18:10.807829','1','linux测试文章-系统',1,'[{\"added\": {}}]',15,3),(15,'2021-04-25 18:18:24.681800','1','ArticleUpDown object (1)',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',16,3),(16,'2021-04-25 18:18:35.436502','1','<input type=\"text\" id=\"textinput\" style=\"display: none\"><p>1</p>',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',12,3),(17,'2021-04-25 18:19:20.080785','2','liuxiayu',3,'',6,3),(18,'2021-04-25 18:19:32.433837','3','xiayu',2,'[{\"changed\": {\"fields\": [\"Last login\", \"Phone\", \"\\u5934\\u50cf\", \"Blog\"]}}]',6,3),(19,'2021-04-25 18:20:55.586241','3','xiayu',2,'[{\"changed\": {\"fields\": [\"\\u5934\\u50cf\"]}}]',6,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(7,'blog','article'),(15,'blog','article2tag'),(14,'blog','articledetail'),(16,'blog','articleupdown'),(8,'blog','blog'),(13,'blog','category'),(12,'blog','comment'),(9,'blog','index_page'),(11,'blog','read'),(10,'blog','tag'),(6,'blog','userinfo'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-25 16:04:52.130737'),(2,'contenttypes','0002_remove_content_type_name','2021-04-25 16:04:52.164601'),(3,'auth','0001_initial','2021-04-25 16:04:52.272266'),(4,'auth','0002_alter_permission_name_max_length','2021-04-25 16:04:52.290876'),(5,'auth','0003_alter_user_email_max_length','2021-04-25 16:04:52.296138'),(6,'auth','0004_alter_user_username_opts','2021-04-25 16:04:52.301608'),(7,'auth','0005_alter_user_last_login_null','2021-04-25 16:04:52.306648'),(8,'auth','0006_require_contenttypes_0002','2021-04-25 16:04:52.308627'),(9,'auth','0007_alter_validators_add_error_messages','2021-04-25 16:04:52.314524'),(10,'auth','0008_alter_user_username_max_length','2021-04-25 16:04:52.319884'),(11,'auth','0009_alter_user_last_name_max_length','2021-04-25 16:04:52.325182'),(12,'auth','0010_alter_group_name_max_length','2021-04-25 16:04:52.343787'),(13,'auth','0011_update_proxy_permissions','2021-04-25 16:04:52.349827'),(14,'auth','0012_alter_user_first_name_max_length','2021-04-25 16:04:52.356299'),(15,'blog','0001_initial','2021-04-25 16:04:52.909444'),(16,'admin','0001_initial','2021-04-25 16:04:52.970986'),(17,'admin','0002_logentry_remove_auto_add','2021-04-25 16:04:52.985371'),(18,'admin','0003_logentry_add_action_flag_choices','2021-04-25 16:04:52.998162'),(19,'sessions','0001_initial','2021-04-25 16:04:53.027316');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('zk7fcqx651bunpaws37aohjh5gm7h17r','.eJxVjMsOgjAQRf9l1qShdGypS_d-QzPTlocaSOjgxvjvQkJi2J5z7v1AL6Hk5Z2XUIRkLXDVFawbCmOCK0guAhUEWmUIf2zOjCk-87SL9KCpn1WcJ1lGVnuiDlvUfU75dTva08FAZdjWpDtPtfcco2fHF9dkz0zJobG2jVHXDVk0aD12GtnYJm2dNUStw0gI3x_mFkUg:1larU4:hMBJJ-53m2uWSiXzvTiHaimIBkE19jWoOqc2bPsdAcg','2021-05-10 11:00:28.028968');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-26 12:53:15
