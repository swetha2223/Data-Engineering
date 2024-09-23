use company;

CREATE TABLE Customers (
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber)
VALUES
(1, 'Amit', 'Sharma', 'amit.sharma@example.com', '9876543210'),
(2, 'Priya', 'Mehta', 'priya.mehta@example.com', '8765432109'),
(3, 'Rohit', 'Kumar', 'rohit.kumar@example.com', '7654321098'),
(4, 'Neha', 'Verma', 'neha.verma@example.com', '6543210987'),
(5, 'Siddharth', 'Singh', 'siddharth.singh@example.com', '5432109876'),
(6, 'Asha', 'Rao', 'asha.rao@example.com', '4321098765');


select* from customers;