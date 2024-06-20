-- Let us suppose that we have two tables, Toy Owners and Toy Details.

-- Toy Owners: 
    -- OwnerID (unique ID for each owner)
    -- OwnerName (name of the owner)
    -- ToyID (ID of the toy they own)
    -- PurchaseDate (Date of the toy purchase)

-- Toy Details:
    -- ToyID (unique ID for each toy)
    -- ToyName (name of the toy)
    -- ToyType (type of the toy)

-- Let's create the Toy Owners table first:
USE intern;

CREATE TABLE ToyOwners (
    OwnerID INT PRIMARY KEY,
    OwnerName VARCHAR(50),
    ToyID INT,
    PurchaseDate DATE
);

-- Inserting some sample data:
INSERT INTO ToyOwners (OwnerID, OwnerName, ToyID, PurchaseDate) VALUES
(1, 'Arreyan', 101, '2023-06-15'),
(2, 'Hemanth', 102, '2022-11-20'),
(3, 'Muskan', 103, '2021-05-10');


-- Let's create the Toy Details table now:
CREATE TABLE ToyDetails (
    ToyID INT PRIMARY KEY,
    ToyName VARCHAR(50),
    ToyType VARCHAR(50)
);

-- Inserting some sample data in it:
INSERT INTO ToyDetails (ToyID, ToyName, ToyType) VALUES
(101, 'Teddy Bear', 'Plush'),
(102, 'Robot', 'Electronic'),
(104, 'Puzzle', 'Wooden');

-- Joins with SubQueries:
    -- SubQueries as the name suggest are the queries that are used within an already written SQL query.

-- Practice Problem 1:
-- Suppose we want to list owners and their toys but only show toys that are "Electronic", the code for that would be:
SELECT ToyOwners.OwnerName, PlushToys.ToyName, PlushToys.ToyType
FROM ToyOwners
INNER JOIN (
    SELECT ToyID, ToyName, ToyType
    FROM ToyDetails
    WHERE ToyType = 'Plush'
) AS PlushToys ON ToyOwners.ToyID = PlushToys.ToyID;

-- Joins with Aggregate Functions:
    -- Aggregate functions like COUNT, SUM, AVG, MIN, and MAX can be used with joins to perform calculations on groups of data.

-- Practice Problem 2:
-- Suppose we have to find out how many toys each owner has, for that we can use the `COUNT` aggregate function.
SELECT ToyOwners.OwnerName, COUNT(ToyDetails.ToyID) AS ToyCount
FROM ToyOwners
LEFT JOIN ToyDetails ON ToyOwners.ToyID = ToyDetails.ToyID
GROUP BY ToyOwners.OwnerName;

-- Joins with Date and Time Functions:
    -- Date and time functions can be used in joins to filter or format date-related data.

-- Practice Problem 3:
-- Suppose we have to find out the toys that were purchased in the last year.
SELECT ToyOwners.OwnerName, ToyDetails.ToyName, ToyOwners.PurchaseDate
FROM ToyOwners
INNER JOIN ToyDetails ON ToyOwners.ToyID = ToyDetails.ToyID
WHERE ToyOwners.PurchaseDate >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

