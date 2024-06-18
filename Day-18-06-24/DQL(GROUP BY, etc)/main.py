import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('/Users/eagle/Developer/INTERNSHIP/Day-18-06-24/DQL(GROUP BY, etc)/main.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    cid INTEGER PRIMARY KEY,
    cname TEXT,
    age INTEGER,
    addr TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    pid INTEGER PRIMARY KEY,
    pname TEXT,
    price INTEGER,
    stock INTEGER,
    location TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    oid INTEGER PRIMARY KEY,
    cid INTEGER,
    amt INTEGER,
    FOREIGN KEY(cid) REFERENCES customer(cid)
);
''')

# Insert sample data into tables
cursor.executemany('''
INSERT INTO customer (cid, cname, age, addr) VALUES (?, ?, ?, ?)
''', [
    (1, 'Sharavni', 30, 'New York'),
    (2, 'Zara', 25, 'Los Angeles'),
    (3, 'Vanita', 35, 'Chicago'),
    (4, 'Urvi', 28, 'Mumbai')
])

cursor.executemany('''
INSERT INTO products (pid, pname, price, stock, location) VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Product1', 5000, 10, 'New York'),
    (2, 'Product2', 15000, 5, 'Los Angeles'),
    (3, 'Product3', 7000, 20, 'Chicago'),
    (4, 'Product4', 12000, 15, 'Mumbai'),
    (5, 'Product5', 25000, 8, 'Mumbai')
])

cursor.executemany('''
INSERT INTO orders (oid, cid, amt) VALUES (?, ?, ?)
''', [
    (1, 1, 20000),
    (2, 2, 5000),
    (3, 1, 7000),
    (4, 3, 10000),
    (5, 4, 3000)
])

conn.commit()

# GROUP BY queries

# 1) Find the total stock of products for each location.
print("Total stock of products for each location:")
cursor.execute('''
SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location;
''')
for row in cursor.fetchall():
    print(row)

# 2) Find the number of products in each price range.
print("\nNumber of products in each price range:")
cursor.execute('''
SELECT CASE 
 WHEN price BETWEEN 0 AND 10000 THEN '0-10000'
 WHEN price BETWEEN 10001 AND 20000 THEN '10001-20000'
 WHEN price BETWEEN 20001 AND 50000 THEN '20001-50000'
 ELSE '50000+'
 END AS price_range, COUNT(*) AS product_count
 FROM products
 GROUP BY price_range;
''')
for row in cursor.fetchall():
    print(row)

# 3) Find the average age of customers grouped by their location (based on the address).
print("\nAverage age of customers grouped by their location:")
cursor.execute('''
SELECT SUBSTR(addr, 1, 3) AS location, AVG(age) AS avg_age
FROM customer
GROUP BY location;
''')
for row in cursor.fetchall():
    print(row)

# ORDER BY queries

# 1) Retrieve all products ordered by their price in descending order.
print("\nAll products ordered by their price in descending order:")
cursor.execute('''
SELECT * 
FROM products
ORDER BY price DESC;
''')
for row in cursor.fetchall():
    print(row)

# 2) Retrieve all customers ordered by their age in ascending order.
print("\nAll customers ordered by their age in ascending order:")
cursor.execute('''
SELECT * 
FROM customer
ORDER BY age ASC;
''')
for row in cursor.fetchall():
    print(row)

# 3) Retrieve all orders ordered by the order amount in descending order and then by the customer name in ascending order.
print("\nAll orders ordered by the order amount in descending order and then by the customer name in ascending order:")
cursor.execute('''
SELECT o.oid, c.cname, o.amt
FROM orders o
JOIN customer c ON o.cid = c.cid
ORDER BY o.amt DESC, c.cname ASC;
''')
for row in cursor.fetchall():
    print(row)

# HAVING queries

# 1) Find the locations where the total stock of products is greater than 20.
print("\nLocations where the total stock of products is greater than 20:")
cursor.execute('''
SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location
HAVING SUM(stock) > 20;
''')
for row in cursor.fetchall():
    print(row)

# 2) Find the customers who have placed orders with a total amount greater than 10000.
print("\nCustomers who have placed orders with a total amount greater than 10000:")
cursor.execute('''
SELECT c.cid, c.cname, SUM(o.amt) AS total_amount
FROM customer c
JOIN orders o ON c.cid = o.cid
GROUP BY c.cid, c.cname
HAVING SUM(o.amt) > 10000;
''')
for row in cursor.fetchall():
    print(row)

# 3) Find the products that have a stock level between 10 and 20 and are located in Mumbai.
print("\nProducts that have a stock level between 10 and 20 and are located in Mumbai:")
cursor.execute('''
SELECT p.pid, p.pname, p.stock
FROM products p
WHERE p.location = 'Mumbai'
GROUP BY p.pid, p.pname, p.stock
HAVING p.stock BETWEEN 10 AND 20;
''')
for row in cursor.fetchall():
    print(row)

conn.close()