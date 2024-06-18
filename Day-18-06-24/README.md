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
    
```sql
    SELECT location, SUM(stock) AS total_stock
    FROM products
    GROUP BY location;
    ```
ad31fc6c-6f4e-4033-9d09-da7cb528519b


2. **Number of products in each price range:**
    
```sql
    SELECT CASE 
        WHEN price BETWEEN 0 AND 10000 THEN '0-10000'
        WHEN price BETWEEN 10001 AND 20000 THEN '10001-20000'
        WHEN price BETWEEN 20001 AND 50000 THEN '20001-50000'
        ELSE '50000+'
    END AS price_range, COUNT(*) AS product_count
    FROM products
    GROUP BY price_range;
    ```
5e60f95d-fa76-41c5-8ace-c08709231f05


3. **Average age of customers grouped by their location:**
    
```sql
    SELECT SUBSTR(addr, 1, 3) AS location, AVG(age) AS avg_age
    FROM customer
    GROUP BY location;
    ```
e988db27-36a7-4297-aad3-698a15227084


### ORDER BY Queries

1. **All products ordered by their price in descending order:**
    
```sql
    SELECT * 
    FROM products
    ORDER BY price DESC;
    ```
8b896dd9-1275-47e8-af6c-e7fc8bccf349


2. **All customers ordered by their age in ascending order:**
    
```sql
    SELECT * 
    FROM customer
    ORDER BY age ASC;
    ```
36be9299-5eaa-47ed-9657-e22ed4fc8cc5


3. **All orders ordered by the order amount in descending order and then by the customer name in ascending order:**
    
```sql
    SELECT o.oid, c.cname, o.amt
    FROM orders o
    JOIN customer c ON o.cid = c.cid
    ORDER BY o.amt DESC, c.cname ASC;
    ```
11f35230-4e38-40d9-b14f-fdad4d5b62ff


### HAVING Queries

1. **Locations where the total stock of products is greater than 20:**
    
```sql
    SELECT location, SUM(stock) AS total_stock
    FROM products
    GROUP BY location
    HAVING SUM(stock) > 20;
    ```
31b95dc2-1cd6-4d4a-9189-233ef0831490


2. **Customers who have placed orders with a total amount greater than 10000:**
    
```sql
    SELECT c.cid, c.cname, SUM(o.amt) AS total_amount
    FROM customer c
    JOIN orders o ON c.cid = o.cid
    GROUP BY c.cid, c.cname
    HAVING SUM(o.amt) > 10000;
    ```
df958011-58b9-48d1-bf96-8f671390de75


3. **Products that have a stock level between 10 and 20 and are located in Mumbai:**
    
```sql
    SELECT p.pid, p.pname, p.stock
    FROM products p
    WHERE p.location = 'Mumbai'
    GROUP BY p.pid, p.pname, p.stock
    HAVING p.stock BETWEEN 10 AND 20;
    ```
95ec2775-641a-43f4-8402-767278f4de57


### Built-in Functions Examples

#### String Functions

1. **CONCAT function example:**
    
```sql
    SELECT 'Hello' || ' ' || 'World';
    ```
4070d7bd-de17-4fe8-b7b6-eff6b058785e


2. **LCASE and LOWER function examples:**
    
```sql
    SELECT LOWER('HELLO');
    ```
49b76e5c-e15b-42aa-ba36-e707aa661060


3. **Extracting substring from 'Hello, World!' from 5th to 10th position:**
    
```sql
    SELECT SUBSTR('Hello, World!', 5, 6);
    ```
6c00586d-5213-49c5-90c1-088e791b88bf


4. **Trimming spaces from ' Hello, World! ':**
    
```sql
    SELECT TRIM(' Hello, World! ');
    ```
eb21080b-95bc-4137-8a13-12b44b5e2dad


#### Date and Time Functions

1. **CURRENT_DATE and SYSDATE function examples:**
    
```sql
    SELECT DATE('now');
    SELECT DATETIME('now');
    ```
a53ce103-d6dd-4035-8d6c-66ab78c7b028


2. **Number of days between '2023-06-15' and '2023-07-20':**
    
```sql
    SELECT JULIANDAY('2023-07-20') - JULIANDAY('2023-06-15');
    ```
80c027f4-9788-435a-85ff-c10e9cd6b9d5


3. **LAST_DAY function example:**
    
```sql
    SELECT DATE('2023-05-01', 'start of month', '+1 month', '-1 day');
    ```
e42f3da4-d782-428f-8864-8c5ffb37b662


4. **Add 3 months to the current date:**
    
```sql
    SELECT DATE('now', '+3 months');
    ```
096a8b5d-0459-4b56-978d-bc79e12c7e93


5. **Extracting time component from a datetime value:**
    
```sql
    SELECT TIME('2023-05-01 12:34:56');
    ```
73002b66-1d9a-4cae-90a1-9cfa25b88966


#### Numeric Functions

1. **AVG and COUNT function examples:**
    
```sql
    SELECT AVG(price) FROM products;
    SELECT COUNT(*) FROM products;
    ```
a2d64e85-72e5-460b-8692-f35d69650fe2


2. **Square root of 144:**
    
```sql
    SELECT SQRT(144);
    ```
22d9ce33-b5ab-40a0-8aae-8ddebd656ebe


3. **Round 3.14159 to two decimal places:**
    
```sql
    SELECT ROUND(3.14159, 2);
    ```
e4cbe805-4d28-4093-b2bd-a5c0dae69284


4. **MIN and MAX function examples with GROUP BY:**
    
```sql
    SELECT MIN(price), MAX(price), location FROM products GROUP BY location;
    ```
75d4048d-e1b1-4bd1-a022-a69744e937c9


5. **Power of 2 raised to the 5th power:**
    
```sql
    SELECT 2.0 * 2.0 * 2.0 * 2.0 * 2.0;
    ```
7b75401c-8ffc-4844-905f-5bf77d30b0dc


Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).

Happy Coding! 🚀