--- 23/08/2024---

--- 1. total amount spend by each customer---
select c.Name, sum(p.Price * s.Quantity) AS TotalSpent
from Customers c
join Sales s on c.CustomerID = s.CustomerID
join Products p on s.ProductID = p.ProductID
group by c.Name;

----2.  find customer who have spent more than 1000 in total---

select  c.Name
from Customers c
join Sales s on c.CustomerID = s.CustomerID
join Products p on  s.ProductID = p.ProductID
group by c.Name
having sum(p.Price * s.Quantity) > 1000;

---- 3. product category with more than 5 products--
select  Category
from Products
group by Category
having count(ProductID) > 5;

----- 4. Total Number of Products for Each Category and Supplier Combination---

select Category, Supplier, count (ProductID) as TotalProducts
from Products
group by  Category, Supplier;


-----5. Summarize Total Sales by Product and Customer ----
select   p.ProductName,  e.FirstName as Customer,  sum(o.Quantity * p.Price) AS TotalSales
from Products p
join Orders o on p.ProductID = o.ProductID
join Employees e on o.EmployeeID = e.EmployeeID
group by   p.ProductName,  e.FirstName;

select sum(TotalSales)as OverallTotal
from( select sum(o.Quantity * p.Price)as TotalSales
from Products p
join Orders o on p.ProductID = o.ProductID
 join Employees e on o.EmployeeID = e.EmployeeID) as TotalSales;




 --- stored procedure ---

 ---1 . stored procedure with insert operation----


create procedure  sp_InsertProduct
    @ProductName varchar(100),
    @Price decimal(10, 2),
    @StockQuantity int,
	@productID int,
	@category varchar(50)
as
begin
    insert into Products (ProductName, Price, StockQuantity ,productID,category)
    values (@ProductName, @Price, @StockQuantity , @productID, @category )
end;
 
 exec  sp_InsertProduct 'watch' , 1000.00 , 10 , 6 ,'electronics';


 ---2 . stored procedure with update operation-----

 create procedure  sp_updateproduct
    @ProductName varchar(100),
    @Price decimal(10, 2),
    @StockQuantity int,
	@productID int,
	@category varchar(50)
as
begin
     update Products
    set ProductName = @ProductName,
        Price = @Price,
        StockQuantity = @StockQuantity,
		category = @category
    where ProductID = @ProductID
end;


exec sp_updateproduct  'landline' ,1200.00 , 4, 2, 'electronics' ; 

select * from  products

----3. stored procedure with delete operation----


create procedure  sp_deleteProduct
	@productID int
	
as
begin
    delete from products 
	where productID = @ProductID
end;
 
 exec  sp_deleteProduct 6;

