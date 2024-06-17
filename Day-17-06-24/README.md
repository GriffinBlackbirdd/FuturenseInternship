```markdown
# 🐱 Cat Database Project

Welcome to the Cat Database Project! This project demonstrates how to use SQLite in Python to manage a database of cats. 🐾

## 📋 Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Database Operations](#database-operations)
  - [Create Table](#create-table)
  - [Insert Records](#insert-records)
  - [Select Records](#select-records)
  - [Update Records](#update-records)
  - [Delete Records](#delete-records)
  - [Alter Table](#alter-table)
- [Custom Queries](#custom-queries)
- [Conclusion](#conclusion)

## 🐾 Introduction

This project showcases basic CRUD (Create, Read, Update, Delete) operations on a SQLite database using Python. We will manage a table of cats, each with attributes like name, breed, age, and color. Additionally, we will perform some custom queries to fetch specific data.

## 🗃️ Database Operations

### 🐱 Create Table

We start by creating a table named `Cats` with the following attributes:
- `id`: Primary Key
- `name`: Text, Not Null
- `breed`: Text
- `age`: Integer
- `color`: Text

```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cats (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    breed TEXT,
    age INTEGER,
    color TEXT
);
''')
```

### 🐾 Insert Records

We insert some initial records into the `Cats` table.

```python
cursor.execute("INSERT INTO Cats (name, breed, age, color) VALUES ('Whiskers', 'Siamese', 3, 'white');")
cursor.execute("INSERT INTO Cats (name, breed, age, color) VALUES ('Mittens', 'Tabby', 2, 'brown');")
cursor.execute("INSERT INTO Cats (name, breed, age, color) VALUES ('Shadow', 'Persian', 5, 'black');")
conn.commit()
```

### 📋 Select Records

We select and print all records from the `Cats` table.

```python
cursor.execute("SELECT * FROM Cats;")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

### ✏️ Update Records

We update the age of 'Whiskers' to 4.

```python
cursor.execute("UPDATE Cats SET age = 4 WHERE name = 'Whiskers';")
conn.commit()
```

### 🗑️ Delete Records

We delete the record of 'Mittens'.

```python
cursor.execute("DELETE FROM Cats WHERE name = 'Mittens';")
conn.commit()
```

### 🛠️ Alter Table

We add a new column `favorite_toy` to the `Cats` table.

```python
cursor.execute("ALTER TABLE Cats ADD COLUMN favorite_toy TEXT;")
conn.commit()
```

## 🔍 Custom Queries

### Find all Siamese cats that are older than 2 years

```python
cursor.execute("SELECT * FROM Cats WHERE breed = 'Siamese' AND age > 2;")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

### Find all cats whose names start with 'Wh'

```python
cursor.execute("SELECT * FROM Cats WHERE name LIKE 'Wh%';")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

### Find all cats between the ages of 2 and 4

```python
cursor.execute("SELECT * FROM Cats WHERE age BETWEEN 2 AND 4;")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

## 🎉 Conclusion

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).

Happy coding! 🚀

```
