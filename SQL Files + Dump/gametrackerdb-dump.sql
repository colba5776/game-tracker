-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: gametrackerdb
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Current Database: `gametrackerdb`
--

/*!40000 DROP DATABASE IF EXISTS `gametrackerdb`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `gametrackerdb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `gametrackerdb`;

--
-- Table structure for table `achievement`
--

DROP TABLE IF EXISTS `achievement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `achievement` (
  `achievementId` int NOT NULL AUTO_INCREMENT,
  `achievementName` varchar(45) NOT NULL,
  `achievementDescription` varchar(250) DEFAULT NULL,
  `gameId` int NOT NULL,
  PRIMARY KEY (`achievementId`,`gameId`),
  UNIQUE KEY `achievementId_UNIQUE` (`achievementId`),
  KEY `fk_Achievement_Game1_idx` (`gameId`),
  CONSTRAINT `fk_Achievement_Game1` FOREIGN KEY (`gameId`) REFERENCES `game` (`gameId`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `achievement`
--

LOCK TABLES `achievement` WRITE;
/*!40000 ALTER TABLE `achievement` DISABLE KEYS */;
INSERT INTO `achievement` VALUES (1,'You Got This','Unlock the entrance.',1),(2,'Feels Good','Make it past 1-4 in a non-seeded run.',1),(3,'Skills Improving','Make it past Olmec\'s Lair in a non-seeded run.',1),(4,'Persistent','Reach the Ice Caves in a non-seeded run.',1),(5,'Journeyman','Complete the game in a non-seeded run.',1),(6,'Ironman','Complete the game without using shortcuts in a non-seeded, single-player run.',1),(7,'Speedlunky','Complete the game in 10 minutes or less without shortcuts in a non-seeded, single-player run.',1),(8,'Pilgrim','Reach the Sunken City in a non-seeded, single-player run.',1),(9,'Master','Complete the game by defeating Hundun in a non-seeded, single-player run.',1),(10,'Awakened','Reach the Cosmic Ocean in a non-seeded, single-player run.',1),(11,'Excavator','Complete the Moon Challenge in a non-seeded run.',1),(12,'Torchbearer','Complete the Star Challenge in a non-seeded run.',1),(13,'Survivor','Complete the Sun Challenge in a non-seeded run.',1),(14,'Seen a Lot','Complete 50% of the Journal or more.',1),(15,'Seen it All','Complete the Journal.',1),(16,'Mama\'s Little Helper','Unlock the first shortcut.',1),(17,'Mama\'s Big Helper','Unlock all three shortcuts.',1),(18,'Track Star','Finish the Tutorial Speedrun in under 30 seconds.',1),(19,'Arena Champion','Win a First-to-Five Deathmatch against three bots using the Default ruleset.',1),(20,'Turkey Whisperer','Bring two turkeys to Yang in a non-seeded run.',1),(21,'Support a Local Business','Buy out Yang\'s Pet Shop in a non-seeded run.',1),(22,'VIP','Enter Madame Tusk\'s Palace of Pleasure as a guest (in a non-seeded run).',1),(23,'Shadow Shopper','Reach the Black Market in a non-seeded run.',1),(24,'Legendary','Reach the City of Gold in a non-seeded, single-player run.',1),(25,'Her Favorite','Obtain the Kapala in a non-seeded run.',1),(26,'Divine Right','Obtain some royal headwear in a non-seeded run.',1),(27,'A Second Chance','Obtain the Ankh in a non-seeded run.',1),(28,'Chosen One','Obtain the Tablet of Destiny in a non-seeded run.',1),(29,'Parenthood','Wake the Eggplant Child in a non-seeded run.',1),(30,'The Full Spelunky','Obtain all other trophies.',1),(31,'Low Scorer','Complete the game without collecting any treasure and without using shortcuts in a non-seeded, single-player run.',1),(32,'Millionaire','End a run with $1,000,000 or more in a non-seeded, single-player run.',1),(33,'Celeste','Climb Celeste Mountain.',2),(34,'Forsaken','Complete Chapter 1.',2),(35,'Archaology','Complete Chapter 2.',2),(36,'Checking Out','Complete Chapter 3.',2),(37,'Breathe','Complete Chapter 4.',2),(38,'In the Mirror','Complete Chapter 5.',2),(39,'Reflection','Complete Chapter 6.',2),(40,'Strawberry Badge','Collect 30 Strawberries.',2),(41,'Strawberry Medal','Collect 80 Strawberries.',2),(42,'Impress Your Friends','Collect 175 Strawberries.',2),(43,'Gateway','Collect a Cassette.',2),(44,'1UP!','Get a 1UP.',2),(45,'Real Gamer','Complete Celeste for PICO-8.',2),(46,'Pointless Machines','Collect the Crystal Heart in Chapter 1.',2),(47,'Sever the Skyline','Complete Chapter 1 B-Side.',2),(48,'Resurrections','Collect the Crystal Heart in Chapter 2.',2),(49,'Black Moonrise','Complete Chapter 2 B-Side.',2),(50,'Scattered and Lost','Collect the Crystal Heart in Chapter 3.',2),(51,'Good Karma','Complete Chapter 3 B-Side.',2),(52,'Eye of the Storm','Collect the Crystal Heart in Chapter 4.',2),(53,'Golden Feather','Complete Chapter 4 B-Side.',2),(54,'Quiet and Falling','Collect the Crystal Heart in Chapter 5.',2),(55,'Mirrow Magic','Complete Chapter 5 B-Side.',2),(56,'Heavy and Frail','Collect the Crystal Heart in Chapter 6.',2),(57,'Center of the Earth','Complete Chapter 6 B-Side.',2),(58,'Pink Sunrise','Collect the Crystal Heart in Chapter 7.',2),(59,'No More Running','Complete Chapter 7 B-Side.',2),(60,'Heart of the Mountain','Collect the Crystal Heart in Chapter 8.',2),(61,'Say Goodbye','Complete Chapter 8 B-Side.',2),(62,'Thanks For Playing','Complete all C-Sides.',2),(63,'Farewell','Complete Chapter 9.',2),(64,'Wow','Find the moon berry.',2),(79,'First Achievement','This is our first achievement.',16),(80,'Second Achievement','This is our second achievement.',16);
/*!40000 ALTER TABLE `achievement` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `achievement_BEFORE_DELETE` BEFORE DELETE ON `achievement` FOR EACH ROW BEGIN
	-- Delete any playthrough achievements where this achievement appears
    DELETE FROM playthroughachievement WHERE achievementId=OLD.achievementId;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `gameId` int NOT NULL AUTO_INCREMENT,
  `gameTitle` varchar(45) NOT NULL,
  `gameDescription` varchar(500) DEFAULT NULL,
  `genreId` int NOT NULL,
  `userId` int NOT NULL,
  PRIMARY KEY (`gameId`),
  UNIQUE KEY `gameId_UNIQUE` (`gameId`),
  KEY `fk_Game_Genre1_idx` (`genreId`),
  KEY `fk_Game_User1_idx` (`userId`),
  CONSTRAINT `fk_Game_Genre1` FOREIGN KEY (`genreId`) REFERENCES `genre` (`genreId`),
  CONSTRAINT `fk_Game_User1` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (1,'Spelunky 2','2D platformer roguelike where you explore a mine on the moon in search of your parents (and maybe some treasure too?).',1,1),(2,'Celeste','Help Madeline survive her inner demons on her journey to the top of Celeste Mountain, in this super-tight platformer from the creators of TowerFall. Brave hundreds of hand-crafted challenges, uncover devious secrets, and piece together the mystery of the mountain.',2,2),(16,'Test Game','This is our test game.',1,11);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `game_BEFORE_DELETE` BEFORE DELETE ON `game` FOR EACH ROW BEGIN
	-- Delete any achievements which belong to this game
    DELETE FROM achievement WHERE gameId=OLD.gameId;
    -- Delete any playthroughs which belong to this game
    DELETE FROM playthrough WHERE gameId=OLD.gameId;
    -- Delete any ratings associated with this game
    DELETE FROM rating WHERE gameId=OLD.gameId;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `genreId` int NOT NULL AUTO_INCREMENT,
  `genreName` varchar(45) NOT NULL,
  `genreDescription` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`genreId`),
  UNIQUE KEY `genreName_UNIQUE` (`genreId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Roguelike','Subgenre of role-playin games traditionally characterized by a dungeon crawl through procedurally generated levels, turn-based gameplay, grid-based movement, and permanent death of the player character.'),(2,'Platformer','Sub-genre of action video games in which the core objective is to move the player character between points in an environment. Platform games are characterized by levels that consist of uneven terrain and suspended platforms of varying height that require jumping and climbing to traverse.'),(3,'Horror','Scary games!'),(4,'Survival','Games where you thrive and try not to die.'),(5,'Racing','Games where you go fast!'),(6,'Sandbox','Create anything you want!'),(7,'Puzzle','Get ready to use your brain!');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playthrough`
--

DROP TABLE IF EXISTS `playthrough`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playthrough` (
  `playthroughId` int NOT NULL AUTO_INCREMENT,
  `playthroughName` varchar(45) NOT NULL,
  `playthroughDescription` varchar(250) DEFAULT NULL,
  `playthroughTargetPercent` int DEFAULT NULL,
  `playthroughCurrentPercent` int DEFAULT NULL,
  `playthroughStartDate` date NOT NULL DEFAULT (curdate()),
  `playthroughEndDate` date DEFAULT NULL,
  `gameId` int NOT NULL,
  `userId` int NOT NULL,
  PRIMARY KEY (`playthroughId`,`gameId`,`userId`),
  UNIQUE KEY `playthroughId_UNIQUE` (`playthroughId`),
  KEY `fk_Playthrough_Game1_idx` (`gameId`),
  KEY `fk_Playthrough_User1_idx` (`userId`),
  CONSTRAINT `fk_Playthrough_Game1` FOREIGN KEY (`gameId`) REFERENCES `game` (`gameId`),
  CONSTRAINT `fk_Playthrough_User1` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`),
  CONSTRAINT `endDateCheck` CHECK ((`playthroughEndDate` >= `playthroughStartDate`))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playthrough`
--

LOCK TABLES `playthrough` WRITE;
/*!40000 ALTER TABLE `playthrough` DISABLE KEYS */;
INSERT INTO `playthrough` VALUES (1,'Full Completion','Fully 100% the game and complete all achievements.',100,90,'2023-03-10',NULL,1,1),(2,'Journeyman','Complete the Journeyman achievement.',NULL,NULL,'2022-12-20','2023-02-15',1,2),(3,'Full Completion','Fully 100% the game and complete all achievements.',100,100,'2021-05-23','2021-11-30',2,2),(12,'Full Completion','Fully complete the game and achievements.',100,65,'2023-04-18',NULL,16,11);
/*!40000 ALTER TABLE `playthrough` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `playthrough_BEFORE_DELETE` BEFORE DELETE ON `playthrough` FOR EACH ROW BEGIN
	-- Delete any playthrough achievements this playthrough contains
    DELETE FROM playthroughachievement WHERE playthroughId=OLD.playthroughId;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `playthroughachievement`
--

DROP TABLE IF EXISTS `playthroughachievement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playthroughachievement` (
  `achievementStatus` varchar(45) NOT NULL DEFAULT 'Incomplete',
  `achievementId` int NOT NULL,
  `playthroughId` int NOT NULL,
  PRIMARY KEY (`achievementId`,`playthroughId`),
  KEY `fk_User_has_Achievement_Achievement1_idx` (`achievementId`),
  KEY `fk_UserAchievement_Playthrough1_idx` (`playthroughId`),
  CONSTRAINT `fk_User_has_Achievement_Achievement1` FOREIGN KEY (`achievementId`) REFERENCES `achievement` (`achievementId`),
  CONSTRAINT `fk_UserAchievement_Playthrough1` FOREIGN KEY (`playthroughId`) REFERENCES `playthrough` (`playthroughId`),
  CONSTRAINT `statusCheck` CHECK ((`achievementStatus` in (_utf8mb4'Complete',_utf8mb4'Incomplete')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playthroughachievement`
--

LOCK TABLES `playthroughachievement` WRITE;
/*!40000 ALTER TABLE `playthroughachievement` DISABLE KEYS */;
INSERT INTO `playthroughachievement` VALUES ('Complete',1,1),('Complete',2,1),('Complete',3,1),('Complete',4,1),('Complete',5,1),('Complete',5,2),('Complete',6,1),('Complete',7,1),('Complete',8,1),('Complete',9,1),('Complete',10,1),('Complete',11,1),('Complete',12,1),('Complete',13,1),('Complete',14,1),('Complete',15,1),('Complete',16,1),('Complete',17,1),('Complete',18,1),('Complete',19,1),('Complete',20,1),('Complete',21,1),('Complete',22,1),('Complete',23,1),('Complete',24,1),('Complete',25,1),('Complete',26,1),('Complete',27,1),('Complete',28,1),('Complete',29,1),('Incomplete',30,1),('Incomplete',31,1),('Incomplete',32,1),('Complete',33,3),('Complete',34,3),('Complete',35,3),('Complete',36,3),('Complete',37,3),('Complete',38,3),('Complete',39,3),('Complete',40,3),('Complete',41,3),('Complete',42,3),('Complete',43,3),('Complete',44,3),('Complete',45,3),('Complete',46,3),('Complete',47,3),('Complete',48,3),('Complete',49,3),('Complete',50,3),('Complete',51,3),('Complete',52,3),('Complete',53,3),('Complete',54,3),('Complete',55,3),('Complete',56,3),('Complete',57,3),('Complete',58,3),('Complete',59,3),('Complete',60,3),('Complete',61,3),('Complete',62,3),('Complete',63,3),('Complete',64,3),('Complete',79,12),('Incomplete',80,12);
/*!40000 ALTER TABLE `playthroughachievement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rating` (
  `ratingValue` int NOT NULL,
  `ratingDescription` varchar(1000) DEFAULT NULL,
  `userId` int NOT NULL,
  `gameId` int NOT NULL,
  PRIMARY KEY (`userId`,`gameId`),
  KEY `fk_Rating_Game1_idx` (`gameId`),
  CONSTRAINT `fk_Rating_Game1` FOREIGN KEY (`gameId`) REFERENCES `game` (`gameId`),
  CONSTRAINT `fk_Rating_User1` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`),
  CONSTRAINT `valueCheck` CHECK (((`ratingValue` >= 1) and (`ratingValue` <= 10)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
INSERT INTO `rating` VALUES (9,'Great game! Very challenging.',1,1),(5,'Wow! I love this game!',1,2),(7,'Fun game.',2,1),(7,'This is our test rating.',11,16);
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) NOT NULL,
  `userPassword` varchar(45) NOT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `userName_UNIQUE` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'EpicGamer75','iamthebest'),(2,'BoyILoveGames','games4life'),(11,'TestUser','pass');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `user_BEFORE_DELETE` BEFORE DELETE ON `user` FOR EACH ROW BEGIN
	-- Delete any games which were added by this user
    DELETE FROM game WHERE userId=OLD.userId;
    -- Delete any ratings which were created by this user
    DELETE FROM rating WHERE userId=OLD.userId;
    -- Delete any playthroughs which were created by this user
    DELETE FROM playthrough WHERE userId=OLD.userId;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-21 14:22:04
