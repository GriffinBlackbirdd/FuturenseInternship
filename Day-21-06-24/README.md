# 🎮 Video Games Database

This repository contains SQL scripts to create and manage a `video_games` database. The database includes a table for storing video game details and several stored procedures and functions for various operations.

## 📋 Table Structure

The `video_games` table includes the following columns:
- `game_id` (INT, Primary Key, Auto Increment)
- `title` (VARCHAR(100))
- `genre` (VARCHAR(50))
- `platform` (VARCHAR(50))
- `price` (DECIMAL(10, 2))

## 📥 Inserting Data

Sample data is inserted into the `video_games` table for demonstration purposes.

## 🛠️ Stored Procedures and Functions

### Procedures

1. **printAllFromVideoGame**: Selects all records from the `video_games` table.
    ```sql
    CALL printAllFromVideoGame();
    ```

2. **get_video_game_details**: Retrieves details of a video game by `game_id`.
    ```sql
    CALL get_video_game_details(1);
    ```

3. **get_video_game_count**: Returns the total count of video games.
    ```sql
    CALL get_video_game_count(@game_count);
    SELECT @game_count;
    ```

4. **list_video_game_titles**: Lists all video game titles using a cursor.
    ```sql
    CALL list_video_game_titles();
    ```

### Functions

1. **get_total_revenue**: Calculates the total revenue from all video games.
    ```sql
    SELECT get_total_revenue();
    ```

## 🗑️ Deleting Procedures and Functions

To delete a procedure:
```sql
DROP PROCEDURE IF EXISTS procedure_name;
```

To delete a function:
```sql
DROP FUNCTION IF EXISTS function_name;
```

## 🚀 Getting Started

1. **Create the Table**:
    ```sql
    CREATE TABLE video_games (
        game_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        genre VARCHAR(50),
        platform VARCHAR(50),
        price DECIMAL(10, 2)
    );
    ```

2. **Insert Sample Data**:
    ```sql
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
    ```
Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).