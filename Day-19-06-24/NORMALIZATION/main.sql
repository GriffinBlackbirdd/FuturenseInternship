-- Let us suppose that we have "MOVIE RENTAL SYSTEM", we will create various tables in it as we move on that will handle the Movies, Customers, Rentals and Payments!
-- Let us also assume that all those data regarding the Movies, Customers, Rentals and Payments are stored in a single table for now.
-- The various rows include - RentalID, CustomerID, CustomerName, MovieID, MovieTitle, RentalDate, ReturnDate, PaymentID, Amount, PaymentDate.
-- But each row has only atomic entry.
-- THIS ENSURE THAT THE TABLE FOLLOWS 1NF!

-- We will perform 2NF now,
-- In our case, RentalID can be the primary key for the entire table. However, there are partial dependencies:

	-- •    CustomerName depends only on CustomerID.
	-- •	MovieTitle depends only on MovieID.
	-- •	Amount and PaymentDate depend only on PaymentID.

-- We will split the table to remove Partial Dependencies

-- RENTALS TABLE
CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY,
    CustomerID INT,
    MovieID INT,
    RentalDate DATE,
    ReturnDate DATE
);

-- CUSTOMERS TABLE
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

-- MOVIES TABLE
CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    MovieTitle VARCHAR(100)
);

-- PAYMENTS TABLE
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    RentalID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID)
);

-- Insert data into Rentals table
INSERT INTO Rentals VALUES (1, 101, 201, '2024-06-01', '2024-06-05');
INSERT INTO Rentals VALUES (2, 102, 202, '2024-06-02', '2024-06-06');
INSERT INTO Rentals VALUES (3, 101, 203, '2024-06-03', '2024-06-07');

-- Insert data into Customers table
INSERT INTO Customers VALUES (101, 'Arreyan Hamid');
INSERT INTO Customers VALUES (102, 'Gumuddu Hemanth');

-- Insert data into Movies table
INSERT INTO Movies VALUES (201, 'Lapata Ladies');
INSERT INTO Movies VALUES (202, '3 Idiots');
INSERT INTO Movies VALUES (203, 'Tumbaad');

-- Insert data into Payments table
INSERT INTO Payments VALUES (301, 1, 15.00, '2024-06-01');
INSERT INTO Payments VALUES (302, 2, 20.00, '2024-06-02');
INSERT INTO Payments VALUES (303, 3, 10.00, '2024-06-03');

-- This ensure that the tables follow 2NF and that there are no Partial Dependencies.

-- We will perform 3NF,
-- For that we will need to perform if there are any Transitive Dependencies - A transitive dependency occurs when a non-key column depends on another non-key column, which in turn depends on the primary key.
-- Checking for Transitive Dependencies:
	-- •	Rentals Table: No transitive dependencies as all non-key columns depend only on RentalID.
	-- •	Customers Table: No transitive dependencies as CustomerName depends only on CustomerID.
	-- •	Movies Table: No transitive dependencies as MovieTitle depends only on MovieID.
	-- •	Payments Table: No transitive dependencies as all non-key columns depend only on PaymentID.


-- But to practice 3NF we will do tackle another example set, 
-- Let's assume again that we have a Students and Courses database, the structure of the table currently has - EnrollmentID, StudentID, StudentName, CourseID, CourseName, InstructorName.
-- Here EnrollmentID is the PRIMARY KEY, but we have TWO Transitive Dependencies and those are - CourseID -> CourseName, and CourseID -> InstructorName
-- We will split the current table into different tables to eliminate the Transitive Dependencies.

-- STUDENTS TABLE!
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100)
);

INSERT INTO Students (StudentID, StudentName) VALUES
(101, 'Arreyan'),
(102, 'Hemanth'),
(103, 'Muskan');

-- COURSES TABLE!
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    InstructorName VARCHAR(100)
);

INSERT INTO Courses (CourseID, CourseName, InstructorName) VALUES
(201, 'Math', 'Neelam'),
(202, 'SQL', 'Soumya'),
(203, 'DSA', 'Ziyaad');

-- ENROLLMENTS TABLE!
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID) VALUES
(1, 101, 201),
(2, 102, 202),
(3, 101, 203),
(4, 103, 201);

-- USE OF EACH TABLE: 
	-- •	Students Table: Contains unique information about each student. StudentID is the primary key.
	-- •	Courses Table: Contains unique information about each course and its instructor. CourseID is the primary key.
	-- •	Enrollments Table: Links students to courses, capturing the many-to-many relationship between students and courses. EnrollmentID is the primary key, and StudentID and CourseID are foreign keys referencing the Students and Courses tables, respectively.

-- We can run the following code to get a well-developed enrollment information.
SELECT e.EnrollmentID, s.StudentName, c.CourseName, c.InstructorName
FROM Enrollments e
JOIN Students s ON e.StudentID = s.StudentID
JOIN Courses c ON e.CourseID = c.CourseID;