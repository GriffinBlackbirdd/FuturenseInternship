# SQL Topics - DQL and In-Built Functions 📊

Welcome to the SQL Database Project! This project demonstrates how to create and manipulate an SQLite database using Python. The database consists of three tables: `customer`, `products`, and `orders`. We will perform various SQL operations including `GROUP BY`, `ORDER BY`, `HAVING`, and use built-in functions to manipulate and retrieve data.

## Database Structure 🗂️

### Tables

1. **customer**
    - `cid` (INTEGER, PRIMARY KEY)
    - `cname` (TEXT)
    - `age` (INTEGER)
    - `addr` (TEXT)

2. **products**
    - `pid` (INTEGER, PRIMARY KEY)
    - `pname` (TEXT)
    - `price` (INTEGER)
    - `stock` (INTEGER)
    - `location` (TEXT)

3. **orders**
    - `oid` (INTEGER, PRIMARY KEY)
    - `cid` (INTEGER, FOREIGN KEY references `customer(cid)`)
    - `pid` (INTEGER, FOREIGN KEY references `products(pid)`)
    - `amt` (INTEGER)

## Sample Data 📋

### customer Table
| cid | cname    | age | addr        |
|-----|----------|-----|-------------|
| 1   | Sharavni | 30  | New York    |
| 2   | Zara     | 25  | Los Angeles |
| 3   | Vanita   | 35  | Chicago     |
| 4   | Urvi     | 28  | Mumbai      |

### products Table
| pid | pname    | price | stock | location    |
|-----|----------|-------|-------|-------------|
| 1   | Product1 | 5000  | 10    | New York    |
| 2   | Product2 | 15000 | 5     | Los Angeles |
| 3   | Product3 | 7000  | 20    | Chicago     |
| 4   | Product4 | 12000 | 15    | Mumbai      |
| 5   | Product5 | 25000 | 8     | Mumbai      |

### orders Table
| oid | cid | pid | amt  |
|-----|-----|-----|------|
| 1   | 1   | 1   | 20000|
| 2   | 2   | 2   | 5000 |
| 3   | 1   | 3   | 7000 |
| 4   | 3   | 4   | 10000|
| 5   | 4   | 5   | 3000 |
| 6   | 5   | 1   | 15000|

## SQL Queries Examples 📝

### GROUP BY Queries

1. **Total stock of products for each location:**
    
    SELECT location, SUM(stock) AS total_stock
    FROM products
    GROUP BY location;


2. **Number of products in each price range:**
    

    SELECT CASE 
        WHEN price BETWEEN 0 AND 10000 THEN '0-10000'
        WHEN price BETWEEN 10001 AND 20000 THEN '10001-20000'
        WHEN price BETWEEN 20001 AND 50000 THEN '20001-50000'
        ELSE '50000+'
    END AS price_range, COUNT(*) AS product_count
    FROM products
    GROUP BY price_range;



3. **Average age of customers grouped by their location:**
    
    SELECT SUBSTR(addr, 1, 3) AS location, AVG(age) AS avg_age
    FROM customer
    GROUP BY location;


### ORDER BY Queries

1. **All products ordered by their price in descending order:**
    
    SELECT * 
    FROM products
    ORDER BY price DESC;


2. **All customers ordered by their age in ascending order:**
    

    SELECT * 
    FROM customer
    ORDER BY age ASC;



3. **All orders ordered by the order amount in descending order and then by the customer name in ascending order:**
    
    SELECT o.oid, c.cname, o.amt
    FROM orders o
    JOIN customer c ON o.cid = c.cid
    ORDER BY o.amt DESC, c.cname ASC;



### HAVING Queries

1. **Locations where the total stock of products is greater than 20:**
    

    SELECT location, SUM(stock) AS total_stock
    FROM products
    GROUP BY location
    HAVING SUM(stock) > 20;



2. **Customers who have placed orders with a total amount greater than 10000:**
    
    SELECT c.cid, c.cname, SUM(o.amt) AS total_amount
    FROM customer c
    JOIN orders o ON c.cid = o.cid
    GROUP BY c.cid, c.cname
    HAVING SUM(o.amt) > 10000;



3. **Products that have a stock level between 10 and 20 and are located in Mumbai:**
    
    SELECT p.pid, p.pname, p.stock
    FROM products p
    WHERE p.location = 'Mumbai'
    GROUP BY p.pid, p.pname, p.stock
    HAVING p.stock BETWEEN 10 AND 20;



### Built-in Functions Examples

#### String Functions

1. **CONCAT function example:**
    
    SELECT 'Hello' || ' ' || 'World';



2. **LCASE and LOWER function examples:**
    
    SELECT LOWER('HELLO');



3. **Extracting substring from 'Hello, World!' from 5th to 10th position:**
    
    SELECT SUBSTR('Hello, World!', 5, 6);



4. **Trimming spaces from ' Hello, World! ':**
    
    SELECT TRIM(' Hello, World! ');


#### Date and Time Functions

1. **CURRENT_DATE and SYSDATE function examples:**
    
    SELECT DATE('now');
    SELECT DATETIME('now');


2. **Number of days between '2023-06-15' and '2023-07-20':**
    
    SELECT JULIANDAY('2023-07-20') - JULIANDAY('2023-06-15');


3. **LAST_DAY function example:**
    
    SELECT DATE('2023-05-01', 'start of month', '+1 month', '-1 day');


4. **Add 3 months to the current date:**
    
    SELECT DATE('now', '+3 months');


5. **Extracting time component from a datetime value:**
    
    SELECT TIME('2023-05-01 12:34:56');


#### Numeric Functions

1. **AVG and COUNT function examples:**
    
    SELECT AVG(price) FROM products;
    SELECT COUNT(*) FROM products;


2. **Square root of 144:**
    
    SELECT SQRT(144);


3. **Round 3.14159 to two decimal places:**
    
    SELECT ROUND(3.14159, 2);


4. **MIN and MAX function examples with GROUP BY:**
    
    SELECT MIN(price), MAX(price), location FROM products GROUP BY location;


5. **Power of 2 raised to the 5th power:**
    
    SELECT 2.0 * 2.0 * 2.0 * 2.0 * 2.0;


Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).

Happy Coding! 🚀
