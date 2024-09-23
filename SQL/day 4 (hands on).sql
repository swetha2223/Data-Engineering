 ---- Hands on---
 create database company1
 use company1;

 CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15)
);

INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber)
VALUES 
('Amit', 'Sharma', 'amit.sharma@example.com', '9876543210'),
('Priya', 'Mehta', 'priya.mehta@example.com', '8765432109'),
('Rohit', 'Kumar', 'rohit.kumar@example.com', '7654321098'),
('Neha', 'Verma', 'neha.verma@example.com', '6543210987'),
('Siddharth', 'Singh', 'siddharth.singh@example.com', '5432109876'),
('Asha', 'Rao', 'asha.rao@example.com', '4321098765');


CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10, 2),
    StockQuantity INT
);

INSERT INTO Products (ProductName, Category, Price, StockQuantity)
VALUES 
('Laptop', 'Electronics', 75000.00, 15),
('Smartphone', 'Electronics', 25000.00, 30),
('Desk Chair', 'Furniture', 5000.00, 10),
('Monitor', 'Electronics', 12000.00, 20),
('Bookshelf', 'Furniture', 8000.00, 8);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    TotalAmount DECIMAL(10, 2),
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Orders (CustomerID, ProductID, Quantity, TotalAmount, OrderDate)
VALUES 
(1, 1, 2, 150000.00, '2024-08-01'),
(2, 2, 1, 25000.00, '2024-08-02'),
(3, 3, 4, 20000.00, '2024-08-03'),
(4, 4, 2, 24000.00, '2024-08-04'),
(5, 5, 5, 40000.00, '2024-08-05');



 --1.Filtering Data using SQL Queries Retrieve all products from the Products table that belong to the category 'Electronics' and have a price greater than 500. --

 select * from products 
 where category = 'electronics ' and price > 500;

 --2.Total Aggregations using SQL Queries Calculate the total quantity of products sold from the Orders table.--

 
select sum(Quantity)as totalquantitysold
from Orders;

 --3.Group By Aggregations using SQL Queries Calculate the total revenue generated for each product in the Orders table

select p.ProductID, p.ProductName, 
  sum(o.Quantity * p.Price) as totalrevenu
from Orders o 
  join Products p on o.ProductID = p.ProductID
group by 
 p.ProductID, p.ProductName;

 ---4.Order of Execution of SQL Queries Write a query that uses WHERE, GROUP BY, HAVING, and ORDER BY clauses and explain the order of execution--

 SELECT 
  p.Category, 
  sum(o.Quantity * p.Price) as totalsales
FROM  Orders o 
  join Products p on o.ProductID = p.ProductID
where
  o.OrderDate >= '2024-07-01'
group by 
  p.Category
having
  sum(o.Quantity * p.Price) > 50000
order by
  totalsales desc;


  --there fore the order of execution will be from and join , where,group by, having ,select and order by--

--5. Rules and Restrictions to Group and Filter Data in SQL Queries Write a query that corrects a violation of using non-aggregated columns without grouping them.

select Category, 
  sum(Price) as TotalPrice
from  Products
group by Category;

---6.Filter Data based on Aggregated Results using Group By and Having Retrieve all customers who have placed more than 5 orders using GROUP BY and HAVING clauses.

select CustomerID, 
 count(OrderID) as numberoforders
from Orders
group by CustomerID
having 
  count (OrderID) > 5;


  ---stored procedure---
  --1.Create a stored procedure named GetAllCustomers that retrieves all customer details from the Customers table.

create procedure  GetAllCustomers
as
begin
   select * from Customers
end;

exec GetAllCustomers;

--2. Create a stored procedure named GetOrderDetailsByOrderID that accepts an OrderID as a parameter and retrieves the order details for that specific order.
create procedure  GetOrderDetailsByOrderID
    @OrderID int
as
begin
    select * from Orders where OrderID = @OrderID;
end;
exec GetOrderDetailsByOrderID 3 ;

--3.  Stored Procedure with Multiple Input Paramete Create a stored procedure named GetProductsByCategoryAndPrice that accepts a product Category and a minimum Price as input parameters and retrieves all products that meet the criteria.

create procedure getproductsbycategoryandprice
     @category varchar(50),
      @minprice decimal (10, 2)
as
begin
      select * from products 
      where category = @category
      and price >= @minprice;

end;
 exec getproductsbycategoryandprice @category = 'electronics', @minprice = 1000.00;

 --4. Create a stored procedure named InsertNewProduct that accepts parameters for ProductName, Category, Price, and StockQuantity and inserts a new product into the Products table

 create procedure  InsertNewProduct
    @ProductName varchar(100),
	@category varchar(50),
    @Price decimal(10, 2),
    @StockQuantity int  
	
as
begin
    insert into Products (ProductName,category, Price, StockQuantity )
    values (@ProductName, @category, @Price, @StockQuantity )
end;

exec   InsertNewProduct 'watch' ,'electronics', 1000.00 , 10 ;

---5.Create a stored procedure named UpdateCustomerEmail that accepts a CustomerID and a NewEmail parameter and updates the email address for the specified customer.
create procedure  UpdateCustomerEmail
    @CustomerID INT,
    @NewEmail VARCHAR(100)
as
begin
    update Customers
    set Email = @NewEmail
   where CustomerID = @CustomerID
end;

exec UpdateCustomerEmail @CustomerID = 3, @NewEmail = 'newemail@example.com'


---6.Create a stored procedure named DeleteOrderByID that accepts an OrderID as a parameter and deletes the corresponding order from the Orders table.
create procedure  DeleteOrderByID
	@productID int
	
as
begin
    delete from products 
	where productID = @ProductID
end;
 
 exec  DeleteOrderByID 1


 ---7. Create a stored procedure named GetTotalProductsInCategory that accepts a Category parameter and returns the total number of products in that category using an output parameter.


create procedure GetTotalProductsInCategory
    @Category VARCHAR(50),
    @TotalProducts INT OUTPUT
as
begin
    select @TotalProducts = count(ProductID)
    from Products
    where Category = @Category
end;

declare  @Total INT
exec GetTotalProductsInCategory @Category = 'Electronics', @TotalProducts = @Total OUTPUT
 select @total as GetTotalProductsInCategory















