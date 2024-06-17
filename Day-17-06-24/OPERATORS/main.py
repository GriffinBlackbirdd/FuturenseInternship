import sqlite3
conn = sqlite3.connect('/Users/eagle/Developer/INTERNSHIP/Day-17-06-24/main.db')
cursor = conn.cursor()

# My query: Find all Siamese cats that are older than 2 years
cursor.execute("SELECT * FROM Cats WHERE breed = 'Siamese' AND age > 2;")
rows = cursor.fetchall()
print("Siamese cats older than 2 years:")
for row in rows:
    print(row)

# My query: Find all cats whose names start with 'Wh'
cursor.execute("SELECT * FROM Cats WHERE name LIKE 'Wh%';")
rows = cursor.fetchall()
print("\nCats whose names start with 'Wh':")
for row in rows:
    print(row)

# My query: Find all cats between the ages of 2 and 4
cursor.execute("SELECT * FROM Cats WHERE age BETWEEN 2 AND 4;")
rows = cursor.fetchall()
print("\nCats between the ages of 2 and 4:")
for row in rows:
    print(row)
conn.close()