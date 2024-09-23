--- aggregate functions( 21/08/2024) ---

use demo;
 CREATE TABLE Sales (
  salesid INT,
  product VARCHAR(255),
  quantity INT,
  price DECIMAL(10, 2)
);

INSERT INTO Sales (salesid, product, quantity, price)
VALUES
  (1, 'Phone', 2, 500.00),
  (2, 'Laptop', 1, 1000.00),
  (3, 'Tablet', 3, 300.00),
  (4, 'Phone', 1, 500.00),
  (5, 'Laptop', 2, 1000.00),
  (6, 'Tablet', 2, 300.00);


  --AVg--

  select avg(price) as avg_price from sales;
  select avg (quantity) as avg_quantity from sales;

  --count--
  select count(*) as COUNT 
  from sales 
  where quantity > 1;

  select product , count(*) as COUNT 
  from sales
  group by product;

  --- distinct---
   select distinct product ,price 
   from sales 
   order by   product;


   ---Max---
   select max(price) from sales;

   select product, max (price) as max_price
   from sales
   group by product;

---min---

select min(quantity) as min_quantity 
from sales;


--- sum---
select sum(price) as total 
from sales;


-----order of execution---

SELECT product, AVG(price) AS avg_price
FROM Sales
WHERE quantity > 0
GROUP BY product
HAVING AVG(price) > 50
ORDER BY avg_price DESC;

SELECT product, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product
ORDER BY total_quantity ASC
OFFSET 1 ROW ;





