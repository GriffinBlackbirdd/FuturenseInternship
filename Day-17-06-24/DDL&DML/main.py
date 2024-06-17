import sqlite3
conn = sqlite3.connect('/Users/eagle/Developer/INTERNSHIP/Day-17-06-24/main.db')
cursor = conn.cursor()

# Create the Cats table - DDL
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cats (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    breed TEXT,
    age INTEGER,
    color TEXT
);
''')

# Insert some cat records - DML
cursor.execute("INSERT INTO Cats (name, breed, age, color) VALUES ('Whiskers', 'Siamese', 3, 'white');")
cursor.execute("INSERT INTO Cats (name, breed, age, color) VALUES ('Mittens', 'Tabby', 2, 'brown');")
cursor.execute("INSERT INTO Cats (name, breed, age, color) VALUES ('Shadow', 'Persian', 5, 'black');")

# Commit the changes
conn.commit()

# Select all records - DML
cursor.execute("SELECT * FROM Cats;")
rows = cursor.fetchall()
print("Cats in the database:")
for row in rows:
    print(row)

# Update a record - DML
cursor.execute("UPDATE Cats SET age = 4 WHERE name = 'Whiskers';")
conn.commit()

# Select all records after the update - DML
cursor.execute("SELECT * FROM Cats;")
rows = cursor.fetchall()
print("\nCats in the database after update:")
for row in rows:
    print(row)

# Delete a record - DML
cursor.execute("DELETE FROM Cats WHERE name = 'Mittens';")
conn.commit()

# Select all records after the delete - DML
cursor.execute("SELECT * FROM Cats;")
rows = cursor.fetchall()
print("\nCats in the database after delete:")
for row in rows:
    print(row)

# Alter the table to add a new column - DDL
cursor.execute("ALTER TABLE Cats ADD COLUMN favorite_toy TEXT;")
conn.commit()

cursor.execute("UPDATE Cats SET favorite_toy = 'Feather Wand' WHERE name = 'Whiskers';")
cursor.execute("UPDATE Cats SET favorite_toy = 'Laser Pointer' WHERE name = 'Shadow';")
conn.commit()

# Show the new table structure
cursor.execute("PRAGMA table_info(Cats);")
columns = cursor.fetchall()
print("\nTable structure after altering:")
for column in columns:
    print(column)

# Drop the table - DDL
# cursor.execute("DROP TABLE Cats;")
# conn.commit()
# print('TABLE DROPPED')
# conn.close()