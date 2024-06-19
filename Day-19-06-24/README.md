# 📚 Library & Movie Rental System Database Setup

Welcome to the **Library & Movie Rental System** database setup! This README will guide you through the SQL scripts to create and populate tables for a library system and a movie rental system. Let's dive in! 🚀

## 📖 Library System

### Database Creation
First, we create a database called `library_system` and switch to it:
```sql
CREATE DATABASE library_system;
USE library_system;
```

### Tables Creation
We create the following tables:
- `books`
- `authors`
- `members`
- `loans`
- `payments`

```sql
-- Creating books table
CREATE TABLE books (
    book_id INT(3) PRIMARY KEY, 
    title VARCHAR(100) NOT NULL, 
    author_id INT(3), 
    price INT(10) NOT NULL, 
    stock INT(5), 
    location VARCHAR(30) CHECK(location IN ('Shelf A', 'Shelf B', 'Shelf C'))
);

-- Creating authors table
CREATE TABLE authors (
    author_id INT(3) PRIMARY KEY, 
    author_name VARCHAR(50) NOT NULL, 
    country VARCHAR(50)
);

-- Creating members table
CREATE TABLE members (
    member_id INT(3) PRIMARY KEY, 
    member_name VARCHAR(30) NOT NULL, 
    age INT(3), 
    address VARCHAR(50)
);

-- Creating loans table
CREATE TABLE loans (
    loan_id INT(3) PRIMARY KEY, 
    member_id INT(3), 
    book_id INT(3), 
    loan_date DATE NOT NULL, 
    FOREIGN KEY(member_id) REFERENCES members(member_id), 
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);

-- Creating payments table
CREATE TABLE payments (
    payment_id INT(3) PRIMARY KEY, 
    loan_id INT(3), 
    amount INT(10) NOT NULL, 
    payment_mode VARCHAR(30) CHECK(payment_mode IN('cash','credit','debit')), 
    status VARCHAR(30), 
    FOREIGN KEY(loan_id) REFERENCES loans(loan_id)
);
```

### Data Insertion
Let's add some data to our tables:
```sql
-- Inserting values into books table
INSERT INTO books VALUES (1, 'The Catcher in the Rye', 101, 300, 20, 'Shelf A');
-- ... (more insert statements)

-- Inserting values into authors table
INSERT INTO authors VALUES (101, 'J.D. Salinger', 'USA');
-- ... (more insert statements)

-- Inserting values into members table
INSERT INTO members VALUES (201, 'Alice', 25, '123 Maple St');
-- ... (more insert statements)

-- Inserting values into loans table
INSERT INTO loans VALUES (301, 201, 1, '2024-06-10');
-- ... (more insert statements)

-- Inserting values into payments table
INSERT INTO payments VALUES (401, 301, 300, 'cash', 'completed');
-- ... (more insert statements)
```

### Queries
Let's run some interesting queries:
```sql
-- Inner Join: Get the names of members who borrowed books
SELECT members.member_id, member_name, loans.loan_id 
FROM loans 
INNER JOIN members ON loans.member_id = members.member_id;

-- Left Outer Join: Get book details and the loan date
SELECT books.book_id, title, loan_date, loans.loan_id 
FROM books
LEFT JOIN loans ON loans.book_id = books.book_id;

-- Full Outer Join: Display all loans and book details
SELECT loans.loan_id, books.book_id, title, loan_date, price, stock, location 
FROM loans
LEFT JOIN books ON loans.book_id = books.book_id
UNION
SELECT loans.loan_id, books.book_id, title, loan_date, price, stock, location 
FROM loans
RIGHT JOIN books ON loans.book_id = books.book_id;
```

## 🎬 Movie Rental System

### Tables Creation
We create the following tables:
- `Rentals`
- `Customers`
- `Movies`
- `Payments`

```sql
-- Creating Rentals table
CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY,
    CustomerID INT,
    MovieID INT,
    RentalDate DATE,
    ReturnDate DATE
);

-- Creating Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

-- Creating Movies table
CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    MovieTitle VARCHAR(100)
);

-- Creating Payments table
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    RentalID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID)
);
```

### Data Insertion
Let's add some data to our tables:
```sql
-- Inserting values into Rentals table
INSERT INTO Rentals VALUES (1, 101, 201, '2024-06-01', '2024-06-05');
-- ... (more insert statements)

-- Inserting values into Customers table
INSERT INTO Customers VALUES (101, 'Arreyan Hamid');
-- ... (more insert statements)

-- Inserting values into Movies table
INSERT INTO Movies VALUES (201, 'Lapata Ladies');
-- ... (more insert statements)

-- Inserting values into Payments table
INSERT INTO Payments VALUES (301, 1, 15.00, '2024-06-01');
-- ... (more insert statements)
```

### Queries
Let's run some interesting queries:
```sql
-- Get a well-developed enrollment information
SELECT e.EnrollmentID, s.StudentName, c.CourseName, c.InstructorName
FROM Enrollments e
JOIN Students s ON e.StudentID = s.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;
```


Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).

Happy querying! 😄
