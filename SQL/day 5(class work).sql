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



----- regular expression---
select * from customers
where FirstName like 'A%';

select * from customers
where PhoneNumber like '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]';


select * from customers
where LastName like  '_____'; -----underscore written 5 times 
---data cleaning and manipulating the data----


update customers
set FirstName = LTRIM(RTRIM(Lower(FirstName))),
    LastName = LTRIM(RTRIM(LOWER(LastName)));
                  
select * from orders;

select CustomerID, OrderID, TotalAmount,
       sum (TotalAmount)over(PARTITION BY CustomerID ORDER BY OrderDate) As RunningTotal
from orders;


-----ranking function---(it shows who ordered most as first rank and i will order like wise)

SELECT CustomerID, TotalSales, 
    RANK() OVER (ORDER BY TotalSales DESC) AS SalesRank 
FROM ( 
      SELECT  CustomerID,  SUM(TotalAmount) AS TotalSales 
        FROM Orders1 
        GROUP BY CustomerID 
  ) AS SalesData;

  --- who reports to whome--




  CREATE TABLE Employees1 (

    EmployeeID INT PRIMARY KEY IDENTITY(1,1),

    EmployeeName VARCHAR(100),

    ManagerID INT NULL

);

 
INSERT INTO Employees1 (EmployeeName, ManagerID)

VALUES 

('Amit Sharma', NULL),  -- Top manager

('Priya Mehta', 1),     -- Reports to Amit

('Rohit Kumar', 1),     -- Reports to Amit

('Neha Verma', 2),      -- Reports to Priya

('Siddharth Singh', 2), -- Reports to Priya

('Asha Rao', 3);        -- Reports to Rohit

 
INSERT INTO Employees1 (EmployeeName, ManagerID)

VALUES 

('Vikram Gupta', 4),  -- Reports to Neha

('Rajesh Patel', 5);  -- Reports to Siddharth

 
  WITH RecursiveEmployeeCTE AS (
    SELECT EmployeeID, ManagerID, EmployeeName 
    FROM  Employees1 
    WHERE ManagerID IS NULL
    UNION ALL
    SELECT e.EmployeeID,  e.ManagerID,  e.EmployeeName 
    FROM  Employees1 e 
    INNER JOIN RecursiveEmployeeCTE r ON e.ManagerID = r.EmployeeID
)
SELECT * FROM RecursiveEmployeeCTE;


---- roleup---it will aslo calculate the products which is not belong to any category

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Category VARCHAR(50),
    Amount DECIMAL(10, 2),
    SaleDate DATE
);
 
INSERT INTO Sales (SaleID, ProductID, Category, Amount, SaleDate) 
VALUES 
(1, 101, 'Electronics', 1500.00, '2024-01-15'),
(2, 102, 'Furniture', 800.00, '2024-01-16'),
(3, 103, 'Electronics', 2000.00, '2024-01-17'),
(4, 104, 'Electronics', 1200.00, '2024-02-01'),
(5, 105, 'Furniture', 900.00, '2024-02-03');


select category ,sum(Amount) as Totalsales
from sales
group by rollup(category);

--- find the people who had made more than 1 order (co related subquerry)--

CREATE TABLE Orders2 (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderAmount DECIMAL(10, 2),
    OrderDate DATE
);
 
INSERT INTO Orders2 (OrderID, CustomerID, OrderAmount, OrderDate)
VALUES 
(1, 1, 500.00, '2024-01-15'),
(2, 2, 700.00, '2024-01-16'),
(3, 1, 300.00, '2024-01-17'),
(4, 3, 1200.00, '2024-02-01'),
(5, 2, 900.00, '2024-02-03');


select distinct o1.customerid
from orders2 o1
where(
     select count(*)
	 from orders2 o2
	 where o2.customerId = o1.customerid
	 ) > 1;

---above the table (view)----
CREATE TABLE ProductSales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Amount DECIMAL(10, 2),
    SaleDate DATE
);
 
INSERT INTO ProductSales (SaleID, ProductID, Amount, SaleDate)
VALUES 
(1, 101, 1500.00, '2024-01-15'),
(2, 102, 800.00, '2024-01-16'),
(3, 103, 2000.00, '2024-01-17'),
(4, 104, 1200.00, '2024-02-01'),
(5, 105, 900.00, '2024-02-03');


create view TotalSalesByProduct
 with Schemabinding
  as
  select productID, sum(amount) as Totalsales
from dbo.productsales
group by productID;


select * from TotalSalesByProduct;
