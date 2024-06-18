import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('/Users/eagle/Developer/INTERNSHIP/Day-18-06-24/DQL(SELECT)/select.db')
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
    pid INTEGER,
    amt INTEGER,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);
''')

# Insert sample data into tables
cursor.executemany('''
INSERT INTO customer (cid, cname, age, addr) VALUES (?, ?, ?, ?)
''', [
    (1, 'Sharavni', 30, 'New York'),
    (2, 'Jhanvi', 25, 'Los Angeles'),
    (3, 'Charvi', 35, 'Chicago'),
    (4, 'Poorvi', 28, 'Mumbai'),
    (5, 'Ravi', 40, 'Delhi')
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
INSERT INTO orders (oid, cid, pid, amt) VALUES (?, ?, ?, ?)
''', [
    (1, 1, 1, 20000),
    (2, 2, 2, 5000),
    (3, 1, 3, 7000),
    (4, 3, 4, 10000),
    (5, 4, 5, 3000),
    (6, 5, 1, 15000)
])

conn.commit()

# DQL queries

# 1) Retrieve the distinct locations of products from the products table.
print("Distinct locations of products:")
cursor.execute('''
SELECT DISTINCT location 
FROM products;
''')
for row in cursor.fetchall():
    print(row)

# 2) Retrieve the customer ID, customer name, and the length of their address as address_length from the customer table.
print("\nCustomer ID, customer name, and the length of their address:")
cursor.execute('''
SELECT cid, cname, LENGTH(addr) AS address_length
FROM customer;
''')
for row in cursor.fetchall():
    print(row)

# 3) Retrieve the order ID, customer name, product name, and the concatenated string 'Order for [product name] by [customer name]' as order_description.
print("\nOrder ID, customer name, product name, and order description:")
cursor.execute('''
SELECT o.oid, c.cname, p.pname, 'Order for ' || p.pname || ' by ' || c.cname AS order_description
FROM orders o
JOIN customer c ON o.cid = c.cid
JOIN products p ON o.pid = p.pid;
''')
for row in cursor.fetchall():
    print(row)

# 4) Retrieve the product ID, product name, price, and a new column price_category that categorizes the products based on their price range.
print("\nProduct ID, product name, price, and price category:")
cursor.execute('''
SELECT pid, pname, price,
       CASE
           WHEN price < 10000 THEN 'Low'
           WHEN price BETWEEN 10000 AND 50000 THEN 'Medium'
           ELSE 'High'
       END AS price_category
FROM products;
''')
for row in cursor.fetchall():
    print(row)

# 5) Retrieve the customer ID, customer name, and the total order amount for each customer.
print("\nCustomer ID, customer name, and total order amount:")
cursor.execute('''
SELECT c.cid, c.cname, (
    SELECT SUM(amt)
    FROM orders o
    WHERE o.cid = c.cid
) AS total_order_amount
FROM customer c;
''')
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()