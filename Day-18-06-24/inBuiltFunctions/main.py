import sqlite3
from datetime import datetime

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('/Users/eagle/Developer/INTERNSHIP/Day-18-06-24/inBuiltFunctions/funcs.db')
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
    (1, 'Jhanvi', 30, 'New York'),
    (2, 'Charvi', 25, 'Los Angeles'),
    (3, 'Charlie', 35, 'Chicago'),
    (4, 'Shamim', 28, 'Mumbai'),
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

# String Functions

# 1) The purpose of the CONCAT() function in SQL with an example
print("CONCAT function example:")
cursor.execute("SELECT 'Hello' || ' ' || 'World';")
print(cursor.fetchone()[0])

# 2) The difference between LCASE() and LOWER() functions
print("\nLCASE and LOWER function examples:")
cursor.execute("SELECT LOWER('HELLO');")
print(cursor.fetchone()[0])

# 3) Extract a substring from the 5th position to the 10th position from "Hello, World!"
print("\nExtracting substring from 'Hello, World!' from 5th to 10th position:")
cursor.execute("SELECT SUBSTR('Hello, World!', 5, 6);")
print(cursor.fetchone()[0])

# 5) Trim both leading and trailing spaces from the string ' Hello, World! '
print("\nTrimming spaces from ' Hello, World! ':")
cursor.execute("SELECT TRIM(' Hello, World! ');")
print(cursor.fetchone()[0])

# Date and Time Functions

# 1) The difference between CURRENT_DATE() and SYSDATE() functions
print("\nCURRENT_DATE and SYSDATE function examples:")
cursor.execute("SELECT DATE('now');")
print(cursor.fetchone()[0])

cursor.execute("SELECT DATETIME('now');")
print(cursor.fetchone()[0])

# 2) Calculate the number of days between '2023-06-15' and '2023-07-20'
print("\nNumber of days between '2023-06-15' and '2023-07-20':")
cursor.execute("SELECT JULIANDAY('2023-07-20') - JULIANDAY('2023-06-15');")
print(int(cursor.fetchone()[0]))

# 3) The purpose of the LAST_DAY() function with an example
print("\nLAST_DAY function example:")
cursor.execute("SELECT DATE('2023-05-01', 'start of month', '+1 month', '-1 day');")
print(cursor.fetchone()[0])

# 4) Add 3 months to the current date
print("\nAdd 3 months to the current date:")
cursor.execute("SELECT DATE('now', '+3 months');")
print(cursor.fetchone()[0])

# 5) Extract the time component from a datetime value
print("\nExtracting time component from a datetime value:")
cursor.execute("SELECT TIME('2023-05-01 12:34:56');")
print(cursor.fetchone()[0])

# Numeric Functions

# 1) The difference between AVG() and COUNT() functions
print("\nAVG and COUNT function examples:")
cursor.execute("SELECT AVG(price) FROM products;")
print(cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM products;")
print(cursor.fetchone()[0])

# 2) Calculate the square root of 144
print("\nSquare root of 144:")
cursor.execute("SELECT SQRT(144);")
print(cursor.fetchone()[0])

# 3) Round the number 3.14159 to two decimal places
print("\nRound 3.14159 to two decimal places:")
cursor.execute("SELECT ROUND(3.14159, 2);")
print(cursor.fetchone()[0])

# 4) The purpose of the MIN() and MAX() functions with examples using GROUP BY
print("\nMIN and MAX function examples with GROUP BY:")
cursor.execute("SELECT MIN(price), MAX(price), location FROM products GROUP BY location;")
for row in cursor.fetchall():
    print(row)

# 5) Calculate the power of 2 raised to the 5th power
print("\nPower of 2 raised to the 5th power:")
cursor.execute("SELECT 2.0 * 2.0 * 2.0 * 2.0 * 2.0;")
print(cursor.fetchone()[0])

# Close the connection
conn.close()