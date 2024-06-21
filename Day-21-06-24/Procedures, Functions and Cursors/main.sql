use intern;

CREATE TABLE video_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    platform VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Inserting some data:
INSERT INTO video_games (title, genre, platform, price) VALUES
('The Legend of Zelda: Breath of the Wild', 'Adventure', 'Nintendo Switch', 59.99),
('God of War', 'Action', 'PlayStation 4', 49.99),
('Red Dead Redemption 2', 'Action-Adventure', 'Xbox One', 39.99),
('Minecraft', 'Sandbox', 'PC', 26.95),
('Fortnite', 'Battle Royale', 'PC', 0.00),
('Among Us', 'Party', 'Mobile', 5.00),
('Cyberpunk 2077', 'RPG', 'PC', 59.99),
('Overwatch', 'Shooter', 'PC', 39.99),
('The Witcher 3: Wild Hunt', 'RPG', 'PC', 29.99),
('Animal Crossing: New Horizons', 'Simulation', 'Nintendo Switch', 59.99);

-- DELIMITER COMMAND:
-- • The DELIMITER command is used to change the standard delimiter (;) to another character, such as //, to avoid conflicts when defining procedures and functions, for example:
    -- • The CREATE PROCEDURE command in SQL is a set of statements that can be saved and reused.
DELIMITER //
CREATE PROCEDURE printAllFromVideoGame()
BEGIN
    SELECT * FROM video_games;
END//

-- Here we can call the Procedure Function
CALL printAllFromVideoGame();

-- To delete a procedure, we can run:
DROP PROCEDURE printAllFromVideoGame; 

-- Creating FUNCTIONS:
DELIMITER $$
CREATE FUNCTION get_total_revenue()
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE total_revenue DECIMAL(10,2);
    SELECT SUM(price) INTO total_revenue FROM video_games;
    RETURN total_revenue;
END$$
DELIMITER ; 

-- To execute a function we can run:
SELECT get_total_revenue(); 

-- To delete a function:
DROP FUNCTION IF EXISTS get_total_revenue; 


-- Creating a Procedure with IN Parameter:
	-- • The IN parameter is used in stored procedures and functions to pass input values to them.
DELIMITER //
CREATE PROCEDURE get_video_game_details(IN game_id INT)
BEGIN
    SELECT * FROM video_games WHERE game_id = game_id;
END //
DELIMITER ;

-- Executing the procedure:
CALL get_video_game_details(1);

-- Creating a Procedure with OUT Parameter:
	-- • The OUT parameter in SQL stored procedures allows you to return values from the procedure to the calling environment.
DELIMITER //
CREATE PROCEDURE get_video_game_count(OUT game_count INT)
BEGIN
    SELECT COUNT(*) INTO game_count FROM video_games;
END //
DELIMITER ;

-- Executing the Procedure:
DELIMITER //
CREATE PROCEDURE get_video_game_count(OUT game_count INT)
BEGIN
    SELECT COUNT(*) INTO game_count FROM video_games;
END //
DELIMITER ;

-- Using CURSORS:
	-- • Cursors in SQL are used to retrieve and process rows one by one from the result set of a query.
DELIMITER //
CREATE PROCEDURE list_video_game_titles()
BEGIN
    DECLARE game_title VARCHAR(100);
    DECLARE done INT DEFAULT FALSE;
    DECLARE game_cursor CURSOR FOR SELECT title FROM video_games;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN game_cursor;

    game_loop: LOOP
        FETCH game_cursor INTO game_title;
        IF done THEN
            LEAVE game_loop;
        END IF;
        SELECT game_title;
    END LOOP game_loop;

    CLOSE game_cursor;
END //
DELIMITER ;

-- Executing the Procedure:
CALL list_video_game_titles();    