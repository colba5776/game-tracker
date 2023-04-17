use gametrackerdb;

/* Create functions */

DROP function IF EXISTS `get_user_name`;
DROP function IF EXISTS `gametrackerdb`.`get_user_name`;;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_user_name`(user_id int) RETURNS varchar(45) CHARSET utf8mb3
    DETERMINISTIC
BEGIN
	DECLARE user_name VARCHAR(45);
    SELECT userName INTO user_name
		FROM user
        WHERE userId=user_id;
	RETURN user_name;
END$$
DELIMITER ;

DROP function IF EXISTS `get_genre_name`;
DROP function IF EXISTS `gametrackerdb`.`get_genre_name`;;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_genre_name`(genre_id INT) RETURNS varchar(45) CHARSET utf8mb3
    DETERMINISTIC
BEGIN
	DECLARE genre_name VARCHAR(45);
    SELECT genreName INTO genre_name
		FROM genre
        WHERE genreId=genre_id;
	RETURN genre_name;
END$$
DELIMITER ;

DROP function IF EXISTS `get_game_played`;
DROP function IF EXISTS `gametrackerdb`.`get_game_played`;;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_game_played`(game_id INT, user_id INT) RETURNS varchar(3) CHARSET utf8mb3
    DETERMINISTIC
BEGIN
	DECLARE has_played VARCHAR(3);
	DECLARE playthrough_count INT;
    
    SET has_played = "No";
    
    SELECT count(*) INTO playthrough_count
		FROM playthrough 
		WHERE gameId=game_id AND userId=user_id;
        
    IF playthrough_count > 0 THEN
		SET has_played = "Yes";
	END IF;
RETURN has_played;
END$$
DELIMITER ;

DROP function IF EXISTS `get_average_rating`;
DROP function IF EXISTS `gametrackerdb`.`get_average_rating`;;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_average_rating`(game_id INT) RETURNS float
    DETERMINISTIC
BEGIN

	DECLARE average_rating FLOAT;
	SELECT avg(ratingValue) INTO average_rating 
		FROM rating
		WHERE gameId=game_id;
	RETURN average_rating;
END$$
DELIMITER ;

USE `gametrackerdb`;
DROP function IF EXISTS `get_game_title`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE FUNCTION `get_game_title`(game_id int) RETURNS varchar(45)
    DETERMINISTIC
BEGIN
	DECLARE game_title VARCHAR(45);
    SELECT gameTitle INTO game_title
		FROM game
        WHERE gameId=game_id;
	RETURN game_title;
END$$
DELIMITER ;

USE `gametrackerdb`;
DROP function IF EXISTS `get_achievement_completed_percent`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_achievement_completed_percent`(playthrough_id INT) RETURNS float
    DETERMINISTIC
BEGIN
	DECLARE percent_completed FLOAT;
    DECLARE count_complete INT;
    DECLARE count_total INT;
	SELECT count(*) INTO count_complete 
		FROM playthroughachievement
		WHERE playthroughId = playthrough_id AND achievementStatus = 'Complete';
	SELECT count(*) INTO count_total
		FROM playthroughachievement
		WHERE playthroughId = playthrough_id;
	SET percent_completed = 100 * (count_complete / count_total);
	RETURN percent_completed;
END$$
DELIMITER ;

USE `gametrackerdb`;
DROP function IF EXISTS `get_achievement_name`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_achievement_name`(achievement_id INT) RETURNS varchar(45) CHARSET utf8mb3
DETERMINISTIC
BEGIN
	DECLARE achievement_name VARCHAR(45);
    SELECT achievementName INTO achievement_name
		FROM achievement
        WHERE achievementId=achievement_id;
	RETURN achievement_name;
END$$
DELIMITER ;

/* Create stored procedures */

USE `gametrackerdb`;
DROP procedure IF EXISTS `ChangePTName`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE PROCEDURE `ChangePTName`(IN inPTName varchar(45), IN inPTID int)
BEGIN
	update playthrough
    set playthroughName = inPTName
    where playthroughID = inPTID;
END$$
DELIMITER ;

USE `gametrackerdb`;
DROP procedure IF EXISTS `ChangePTDesc`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE PROCEDURE `ChangePTDesc`(IN inPTDesc varchar(45), IN inPTID int)
BEGIN
	update playthrough
    set playthroughDescription = inPTdesc
    where playthroughID = inPTID;
END$$
DELIMITER ;

USE `gametrackerdb`;
DROP procedure IF EXISTS `changePTPERC`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE PROCEDURE `changePTPERC`(IN inPTPERC INT, IN inPTID int)
BEGIN
	update playthrough
    set playthroughCurrentPercent = inPTPERC
    where playthroughID = inPTID;
END$$
DELIMITER ;

USE `gametrackerdb`;
DROP procedure IF EXISTS `changePTPercTarg`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE PROCEDURE `changePTPercTarg`(IN inPTPERCTarg INT, IN inPTID int)
BEGIN
	update playthrough
    set playthroughtargetpercent = inPTPERCTarg
    where playthroughID = inPTID;
END$$
DELIMITER ;

/* Create  Triggers */

DROP TRIGGER IF EXISTS `gametrackerdb`.`user_BEFORE_DELETE`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `user_BEFORE_DELETE` BEFORE DELETE ON `user` FOR EACH ROW BEGIN
	-- Delete any games which were added by this user
    DELETE FROM game WHERE userId=OLD.userId;
    -- Delete any ratings which were created by this user
    DELETE FROM rating WHERE userId=OLD.userId;
    -- Delete any playthroughs which were created by this user
    DELETE FROM playthrough WHERE userId=OLD.userId;
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `gametrackerdb`.`game_BEFORE_DELETE`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `game_BEFORE_DELETE` BEFORE DELETE ON `game` FOR EACH ROW BEGIN
	-- Delete any achievements which belong to this game
    DELETE FROM achievement WHERE gameId=OLD.gameId;
    -- Delete any playthroughs which belong to this game
    DELETE FROM playthrough WHERE gameId=OLD.gameId;
    -- Delete any ratings associated with this game
    DELETE FROM rating WHERE gameId=OLD.gameId;
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `gametrackerdb`.`achievement_BEFORE_DELETE`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER = CURRENT_USER TRIGGER `gametrackerdb`.`achievement_BEFORE_DELETE` BEFORE DELETE ON `achievement` FOR EACH ROW
BEGIN
	-- Delete any playthrough achievements where this achievement appears
    DELETE FROM playthroughachievement WHERE achievementId=OLD.achievementId;
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS `gametrackerdb`.`playthrough_BEFORE_DELETE`;

DELIMITER $$
USE `gametrackerdb`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `playthrough_BEFORE_DELETE` BEFORE DELETE ON `playthrough` FOR EACH ROW BEGIN
	-- Delete any playthrough achievements this playthrough contains
    DELETE FROM playthroughachievement WHERE playthroughId=OLD.playthroughId;
END$$
DELIMITER ;