# Toy Database Fun! 🎉

Welcome to the Toy Database Fun! This README will guide you through the creation and querying of two tables: **Toy Owners** and **Toy Details**. Let's dive into the world of toys and their owners! 🧸🤖

## Database Setup 🛠️

### Step 1: Create the Toy Owners Table

First, we create the `ToyOwners` table to store information about toy owners and their purchases.

```sql
USE intern;

CREATE TABLE ToyOwners (
    OwnerID INT PRIMARY KEY,
    OwnerName VARCHAR(50),
    ToyID INT,
    PurchaseDate DATE
);
```

### Step 2: Insert Sample Data into Toy Owners

Let's add some sample data to our `ToyOwners` table.

```sql
INSERT INTO ToyOwners (OwnerID, OwnerName, ToyID, PurchaseDate) VALUES
(1, 'Arreyan', 101, '2023-06-15'),
(2, 'Hemanth', 102, '2022-11-20'),
(3, 'Muskan', 103, '2021-05-10');
```

### Step 3: Create the Toy Details Table

Next, we create the `ToyDetails` table to store information about the toys.

```sql
CREATE TABLE ToyDetails (
    ToyID INT PRIMARY KEY,
    ToyName VARCHAR(50),
    ToyType VARCHAR(50)
);
```

### Step 4: Insert Sample Data into Toy Details

Let's add some sample data to our `ToyDetails` table.

```sql
INSERT INTO ToyDetails (ToyID, ToyName, ToyType) VALUES
(101, 'Teddy Bear', 'Plush'),
(102, 'Robot', 'Electronic'),
(104, 'Puzzle', 'Wooden');
```

## Querying the Database 🔍

### Practice Problem 1: List Owners and Their Plush Toys 🧸

We want to list owners and their toys but only show toys that are "Plush".

```sql
SELECT ToyOwners.OwnerName, PlushToys.ToyName, PlushToys.ToyType
FROM ToyOwners
INNER JOIN (
    SELECT ToyID, ToyName, ToyType
    FROM ToyDetails
    WHERE ToyType = 'Plush'
) AS PlushToys ON ToyOwners.ToyID = PlushToys.ToyID;
```

### Practice Problem 2: Count the Number of Toys Each Owner Has 📊

We need to find out how many toys each owner has using the `COUNT` aggregate function.

```sql
SELECT ToyOwners.OwnerName, COUNT(ToyDetails.ToyID) AS ToyCount
FROM ToyOwners
LEFT JOIN ToyDetails ON ToyOwners.ToyID = ToyDetails.ToyID
GROUP BY ToyOwners.OwnerName;
```

### Practice Problem 3: Find Toys Purchased in the Last Year 📅

We want to find out the toys that were purchased in the last year.

```sql
SELECT ToyOwners.OwnerName, ToyDetails.ToyName, ToyOwners.PurchaseDate
FROM ToyOwners
INNER JOIN ToyDetails ON ToyOwners.ToyID = ToyDetails.ToyID
WHERE ToyOwners.PurchaseDate >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);
```

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).