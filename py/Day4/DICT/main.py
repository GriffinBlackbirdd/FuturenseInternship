# Dictionary Basics
# A dictionary in Python is an unordered collection of key-value pairs.
# It is mutable, meaning you can add, modify, or remove elements after its creation.
# Dictionaries are useful for storing and retrieving data efficiently, especially when you need to associate values with unique keys.

# Creating a Dictionary
# You can create a dictionary using the dict() constructor or by enclosing key-value pairs inside curly braces {}.

# Using the dict() constructor
empty_dict = dict()

# Using curly braces to create a dictionary representing superheroes
superheroes = {
    'hero1': {'name': 'Clark Kent', 'alias': 'Superman', 'powers': ['super strength', 'flight', 'x-ray vision'], 'city': 'Metropolis'},
    'hero2': {'name': 'Bruce Wayne', 'alias': 'Batman', 'powers': ['martial arts', 'intelligence', 'gadgets'], 'city': 'Gotham'}
}
# Accessing and Modifying Values

# Accessing values
print(superheroes['hero1']['alias'])  # Output: Superman
print(superheroes.get('hero2').get('city'))  # Output: Gotham

# Modifying values
superheroes['hero1']['city'] = 'Smallville'
# Adding and Removing Key-Value Pairs
# You can add new key-value pairs or remove existing ones.
# Adding a new superhero
superheroes['hero3'] = {'name': 'Diana Prince', 'alias': 'Wonder Woman', 'powers': ['super strength', 'agility', 'combat skills'], 'city': 'Themyscira'}

# Removing a superhero
removed_hero = superheroes.pop('hero2')
print(removed_hero)  
# Dictionary Methods
# keys(): 
print(superheroes.keys())  
# values(): 
print(superheroes.values()) 

# items():
print(superheroes.items()) 

# get(key, default=None): 
print(superheroes.get('hero2', 'Not found'))  

# pop(key, default=None): 
print(superheroes.pop('hero3', 'Not found'))  

# clear(): 
superheroes.clear()
print(superheroes) 

# copy(): 
superheroes = {
    'hero1': {'name': 'Clark Kent', 'alias': 'Superman', 'powers': ['super strength', 'flight', 'x-ray vision'], 'city': 'Metropolis'},
    'hero2': {'name': 'Bruce Wayne', 'alias': 'Batman', 'powers': ['martial arts', 'intelligence', 'gadgets'], 'city': 'Gotham'}
}
superheroes_copy = superheroes.copy()
print(superheroes_copy)  

# Practical Examples and Use Cases

# 1. Representing Complex Data Structures


library = {
    'book1': {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    'book2': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    'book3': {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925}
}

print(library['book1']['title'])
print(library['book3']['author'])

# 2. Configuration Files


config = {
    'library_name': 'City Library',
    'max_books_per_user': 5,
    'database': {
        'host': 'localhost',
        'user': 'admin',
        'password': 'password123'
    }
}


library_name = config['library_name']
db_host = config['database']['host']

# 3. Counting Occurrences

borrowed_books = ['1984', '1984', 'The Great Gatsby', '1984', 'To Kill a Mockingbird']
book_counts = {}

for book in borrowed_books:
    if book in book_counts:
        book_counts[book] += 1
    else:
        book_counts[book] = 1

print(book_counts)  
# 4. Data Processing
# List of books with their details
books = [
    {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925}
]

# Filtering books published before 1950
filtered_books = [book for book in books if book['year'] < 1950]
print(filtered_books)  
# Dictionary Comprehension
titles = ['1984', 'To Kill a Mockingbird', 'The Great Gatsby']

# Dictionary with titles as keys and their lengths as values
title_lengths = {title: len(title) for title in titles}
print(title_lengths)  

# Nesting Dictionaries
library = {
    'book1': {
        'title': '1984',
        'author': 'George Orwell',
        'year': 1949,
        'availability': {
            'total_copies': 5,
            'borrowed_copies': 2
        }
    },
    'book2': {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year': 1960,
        'availability': {
            'total_copies': 3,
            'borrowed_copies': 1
        }
    }
}

print(library['book1']['availability']['total_copies'])  # Output: 5

# Use Cases and Real World Examples
# 1. Counting Occurrences
borrowed_books = ['1984', '1984', 'The Great Gatsby', '1984', 'To Kill a Mockingbird']
book_counts = {}

for book in borrowed_books:
    if book in book_counts:
        book_counts[book] += 1
    else:
        book_counts[book] = 1

print(book_counts)  
# 2. Data Manipulation and Analysis
books = [
    {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925}
]

# Filtering books published before 1950
filtered_books = [book for book in books if book['year'] < 1950]
print(filtered_books)  # Output: [{'title': '1984', 'author': 'George Orwell', 'year': 1949}, {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925}]

# Solving Problems Using Sets and Dictionaries
# Sets and dictionaries are often used together to solve various problems, such as finding unique elements, counting occurrences, or performing set operations.
# Finding common authors between two lists
authors1 = ['George Orwell', 'Harper Lee', 'F. Scott Fitzgerald']
authors2 = ['F. Scott Fitzgerald', 'J.K. Rowling', 'George Orwell']

set1 = set(authors1)
set2 = set(authors2)

common_authors = set1.intersection(set2)
print(common_authors) 
# Counting unique authors
authors = ['George Orwell', 'Harper Lee', 'George Orwell', 'F. Scott Fitzgerald']
unique_counts = {author: authors.count(author) for author in set(authors)}
print(unique_counts)

# Best Practices for Choosing Between Sets and Dictionaries
# Use sets when dealing with unique elements and set operations.
# Use dictionaries when you need to associate values with keys and perform frequent lookups.

# Use Sets When:

# 1. Storing Unique Elements
# Storing unique authors
unique_authors = set(['George Orwell', 'Harper Lee', 'George Orwell', 'F. Scott Fitzgerald'])
print(unique_authors)

# 2. Checking Membership Efficiently
authors = set(['George Orwell', 'Harper Lee', 'F. Scott Fitzgerald'])
print('George Orwell' in authors)
print('J.K. Rowling' in authors) 

# 3. Removing Duplicate Elements
duplicate_list = ['George Orwell', 'Harper Lee', 'George Orwell', 'F. Scott Fitzgerald']
unique_list = list(set(duplicate_list))
print(unique_list)  
# Use Dictionaries When:
# 1. Associating Values with Keys
book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
print(book['title'])

# 2. Frequent Lookups and Retrievals
library = {
    '1984': {'author': 'George Orwell', 'year': 1949},
    'To Kill a Mockingbird': {'author': 'Harper Lee', 'year': 1960}
}
print(library.get('1984', 'Not found'))  
# 3. Counting Occurrences
borrowed_books = ['1984', '1984', 'The Great Gatsby', '1984', 'To Kill a Mockingbird']
book_counts = {}

for book in borrowed_books:
    if book in book_counts:
        book_counts[book] += 1
    else:
        book_counts[book] = 1

print(book_counts) 
# 4. Representing Complex Data Structures
library = {
    'book1': {
        'title': '1984',
        'author': 'George Orwell',
        'year': 1949,
        'availability': {
            'total_copies': 5,
            'borrowed_copies': 2
        }
    },
    'book2': {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year': 1960,
        'availability': {
            'total_copies': 3,
            'borrowed_copies': 1
        }
    }
}

# Accessing nested data
print(library['book1']['availability']['total_copies'])