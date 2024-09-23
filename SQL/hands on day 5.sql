--- hands on---
--1. Join the `Orders` and `Customers` tables to find the total order amount per customer and filter out customers who have spent less than $1,000.

use company1;
select  c.CustomerID, c.FirstName,  c.LastName, 
  sum(o.TotalAmount) AS TotalOrderAmount
from 
  Customers c
  join Orders o on c.CustomerID = o.CustomerID
group by  
  c.CustomerID, 
  c.FirstName, 
  c.LastName
having
 sum(o.TotalAmount) < 1000
order by 
  TotalOrderAmount DESC;

  --2.Create a cumulative sum of the `OrderAmount` for each customer to track the running total of how much each customer has spent.

  select 
    ProductID,
    TotalAmount,
    sum(TotalAmount) over(partition by ProductID order by TotalAmount) as RunningTotal
from
    orders;

	-- 3. Rank the customers based on the total amount they have spent, partitioned by city.

	CREATE TABLE Customers1 (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100)
);

INSERT INTO Customers1 (CustomerID, CustomerName, City) VALUES
(1, 'John Doe', 'New York'),
(2, 'Jane Smith', 'Los Angeles'),
(3, 'Michael Brown', 'Chicago'),
(4, 'Emily Davis', 'Houston'),
(5, 'James Wilson', 'Phoenix'),
(6, 'Sophia Johnson', 'Philadelphia'),
(7, 'Daniel Taylor', 'San Antonio'),
(8, 'Emma Moore', 'San Diego'),
(9, 'Olivia Garcia', 'Dallas'),
(10, 'Ava Martinez', 'Mumbai');

select
  c.CustomerID, 
  c.City, 
  s.TotalSales, 
  rank() over(PARTITION BY c.City ORDER BY s.TotalSales DESC) as SalesRank
from 
  Customers1 c
 join(select CustomerID, 
      sum(TotalAmount) as TotalSales
    from Orders
    group by CustomerID
  ) as s on c.CustomerID = s.CustomerID
order by
  c.City, SalesRank;

  ---4. Calculate the total amount of all orders (overall total) and the percentage each customer's total spending contributes to the overall total.
  
select CustomerID, TotalSales, 
 sum(TotalSales) over () as OverallTotal, 
  (TotalSales / sum(TotalSales) OVER ()) * 100 as PercentageContribution
from ( select
      CustomerID, 
      sum(TotalAmount) as TotalSales
   from
      Orders
    group by
      CustomerID
  ) as SalesData
order by 
  TotalSales DESC;

  ---- 5.  Rank all customers based on the total amount they have spent, without partitioning.


  select CustomerID, TotalSales, 
    rank() over (order by TotalSales DESC) as SalesRank 
from ( 
     select  CustomerID,  sum(TotalAmount) as TotalSales 
       from Orders
        group by CustomerID 
  ) as SalesData;

  ----6.  Write a query that joins the `Orders` and `Customers` tables, calculates the average order amount for each city, and orders the results by the average amount in descending order.

select  c.City, 
  avg(o.TotalAmount)as AverageOrderAmount
from Customers1 c
  join Orders o on c.CustomerID = o.CustomerID
group by
  c.City
order by
  AverageOrderAmount DESC;

  ---- 7.Write a query to find the top 3 customers who have spent the most, using `ORDER BY` and `LIMIT`.

 select top 3 
  c.CustomerID, 
  c.FirstName, 
  c.LastName, 
  sum(o.TotalAmount) as TotalSpending
from  Customers c
  JOIN Orders o on c.CustomerID = o.CustomerID
group by c.CustomerID,  c.FirstName,  c.LastName
order by TotalSpending DESC;

--8. Write a query that groups orders by year (using OrderDate), calculates the total amount of orders for each year, and orders the results by year.
select
  year(o.OrderDate) as OrderYear, 
  SUM(o.TotalAmount) as TotalOrders
from 
  Orders o
group by 
  year(o.OrderDate)
order by
  OrderYear;


  ---9.Write a query that ranks customers by their total spending, but only for customers located in "Mumbai". The rank should reset for each customer in "Mumbai".

select C.CustomerID, C.CustomerName, C.City, 
    sum(O.totalAmount) AS TotalSpent,
    rank() over (order by sum(O.totalAmount)desc) as CustomerRank
from Customers1  C
join Orders O 
on C.CustomerID = O.CustomerID
where C.City = 'Mumbai'
group by C.CustomerID, C.CustomerName,C.City;



  ---10.   Write a query that calculates each customer's total order amount and compares it to the average order amount for all customers.
with  CustomerTotals as (
   select C.CustomerID, C.CustomerName, 
        SUM(O.totalAmount) AS TotalSpent
   from Customers1 C
    join Orders O 
    on C.CustomerID = O.CustomerID
   group by  C.CustomerID, C.CustomerName
)
select CustomerID, 
    CustomerName, 
    TotalSpent,
    AVG(TotalSpent) over() as AverageOrderAmount,
    TotalSpent - avg(TotalSpent) over()as DifferenceFromAverage
from CustomerTotals;













