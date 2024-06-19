-- Creating a database called library_system
create database library_system;

-- Using the library_system database
use library_system;

-- Creating a table named 'books' with columns: book_id, title, author_id, price, stock, location
create table books
(
    book_id int(3) primary key, 
    title varchar(100) not null, 
    author_id int(3), 
    price int(10) not null, 
    stock int(5), 
    location varchar(30) check(location in ('Shelf A', 'Shelf B', 'Shelf C')) -- Location (either Shelf A, Shelf B, or Shelf C)
);

-- Creating a table named 'authors' with columns: author_id, author_name, country
create table authors
(
    author_id int(3) primary key, 
    author_name varchar(50) not null, 
    country varchar(50) 
);

-- Creating a table named 'members' with columns: member_id, member_name, age, address
create table members
(
    member_id int(3) primary key, 
    member_name varchar(30) not null, 
    age int(3), 
    address varchar(50) 
);

-- Creating a table named 'loans' with columns: loan_id, member_id, book_id, loan_date
create table loans
(
    loan_id int(3) primary key, 
    member_id int(3), 
    book_id int(3), 
    loan_date date not null, 
    foreign key(member_id) references members(member_id), 
    foreign key(book_id) references books(book_id) 
);

-- Creating a table named 'payments' with columns: payment_id, loan_id, amount, payment_mode, status
create table payments
(
    payment_id int(3) primary key, 
    loan_id int(3), 
    amount int(10) not null, 
    payment_mode varchar(30) check(payment_mode in('cash','credit','debit')), 
    status varchar(30), -- Payment status
    foreign key(loan_id) references loans(loan_id) 
);

-- Inserting values into books table
insert into books values(1, 'The Catcher in the Rye', 101, 300, 20, 'Shelf A');
insert into books values(2, 'To Kill a Mockingbird', 102, 350, 15, 'Shelf B');
insert into books values(3, '1984', 103, 200, 25, 'Shelf C');
insert into books values(4, 'Pride and Prejudice', 104, 400, 10, 'Shelf A');
insert into books values(5, 'The Great Gatsby', 105, 250, 30, 'Shelf B');

-- Inserting values into authors table
insert into authors values(101, 'J.D. Salinger', 'USA');
insert into authors values(102, 'Harper Lee', 'USA');
insert into authors values(103, 'George Orwell', 'UK');
insert into authors values(104, 'Jane Austen', 'UK');
insert into authors values(105, 'F. Scott Fitzgerald', 'USA');

-- Inserting values into members table
insert into members values(201, 'Alice', 25, '123 Maple St');
insert into members values(202, 'Bob', 30, '456 Oak St');
insert into members values(203, 'Charlie', 35, '789 Pine St');
insert into members values(204, 'David', 40, '101 Birch St');
insert into members values(205, 'Eve', 28, '202 Cedar St');

-- Inserting values into loans table
insert into loans values(301, 201, 1, '2024-06-10');
insert into loans values(302, 202, 2, '2024-06-11');
insert into loans values(303, 203, 3, '2024-06-12');
insert into loans values(304, 204, 4, '2024-06-13');
insert into loans values(305, 205, 5, '2024-06-14');

-- Inserting values into payments table
insert into payments values(401, 301, 300, 'cash', 'completed');
insert into payments values(402, 302, 350, 'credit', 'completed');
insert into payments values(403, 303, 200, 'debit', 'in process');
insert into payments values(404, 304, 400, 'cash', 'completed');
insert into payments values(405, 305, 250, 'credit', 'in process');

-- Displaying details of the various tables
SELECT * FROM books;
SELECT * FROM authors;
SELECT * FROM members;
SELECT * FROM loans;
SELECT * FROM payments;

-- INNER JOIN!
-- Inner Join: Get the names of members who borrowed books
SELECT members.member_id, member_name, loans.loan_id FROM loans 
INNER JOIN members ON loans.member_id = members.member_id;

-- Inner Join: Get the names of members and the books they borrowed
SELECT members.member_id, member_name, books.book_id, title, loans.loan_id FROM loans
INNER JOIN books ON loans.book_id = books.book_id
INNER JOIN members ON loans.member_id = members.member_id;

-- LEFT OUTER JOIN!
-- Left Outer Join: Get book details and the loan date
SELECT books.book_id, title, loan_date, loans.loan_id FROM books
LEFT JOIN loans ON loans.book_id = books.book_id;

-- RIGHT OUTER JOIN!
-- Right Outer Join: Display loan details and their payment status
SELECT * FROM payments 
RIGHT JOIN loans ON loans.loan_id = payments.loan_id;

-- FULL OUTER JOIN!
-- Full Outer Join: Display all loans and book details
SELECT loans.loan_id, books.book_id, title, loan_date, price, stock, location FROM loans
LEFT JOIN books ON loans.book_id = books.book_id
UNION
SELECT loans.loan_id, books.book_id, title, loan_date, price, stock, location FROM loans
RIGHT JOIN books ON loans.book_id = books.book_id;

-- SELF JOIN!
-- Self Join: Display authors and their books
SELECT a1.author_name AS Author, a2.title AS Book FROM authors a1
INNER JOIN books a2 ON a1.author_id = a2.author_id;

-- CROSS JOIN!
-- Cross Join: Display all possible combinations of members and loans where the amount is less than 300
SELECT members.member_id, member_name, loans.loan_id, amount FROM members
CROSS JOIN loans ON members.member_id = loans.member_id
WHERE amount < 300;