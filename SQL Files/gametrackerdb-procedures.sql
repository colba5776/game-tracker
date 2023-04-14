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