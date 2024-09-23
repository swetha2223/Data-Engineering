--- day 4 functions---
use company;

select productName , price,Round(price, 2) as RoundedPrice
from products;

select productName , price, sqrt(price) as RoundedPrice
from products;

select productName , price,ceiling(price) as RoundedPrice
from products;

select productName , price,Round(price, 2) as RoundedPrice
from products;

select productName , price,floor(price) as RoundedPrice
from products;

select productName , price,power(price, 2) as RoundedPrice
from products;

---muduloo which gives reminder as an output--
select productName , price, price %5 as moduloPrice
from products;

---abs eliminate neg value---

select abs(Max(price) -min(price)) as pricedifference
from products

select productName , price,round(rand() *100 ,2)  as randomdiscountPrice
from products


select productName , price,log(price) as logerthamicPrice
from products ;

---Scenario: Apply a 15% discount, round the discounted price to 2 decimal places, and show both the ceiling and floor values of the final discounted price.----
 
select productName , price , round (price * 0.85, 2)  as discountprice ,
ceiling (round(price* 0.85,2))as  ceiledprice ,
floor ( round(price *0.85 ,2))as roundedprice
from products;


---AGGREGATE FUNCTION---
select sum(TotalAmount) as totalAmount
from orders;

select avg(price) as taverageprice
from products;

select count(orderid) as totalorderid
from orders;


select min( price) as minprice ,max(price) as maxprice
from products;

select category , count (productid ) as product 
from products;


-- pre complile the code  (stored procedure)   cshasey temprary storage of data ---
create  procedure  getallproduct
as
begin
   select* from products;

end;
exec getallproduct


----for multiple code---
create  procedure  getallproducts22
as
begin
   select* from products;
   select * from 

end;
exec getallproducts22

---- accepting a parameter---


create procedure getproductbyID
     @productID int
as
begin
     select* from products
     where productID = @productID;
end;

      exec getproductbyID @ProductID = 1 ;



	  Create procedure getprobyid
	@ProductID INT
as
begin 
	select * from Products
	where ProductID=@ProductID;
end;

exec getprobyid @ProductID = 2

----products by category and price---
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

--- sp outside of table----

create procedure gettotalproductsIncategory
  @category varchar(50),
  @totalproducts int output

  as
  begin
     select @totalproducts = count(*)
     from products
     where category = @category;
  end;


  declare @total int;
  exec gettotalproductsIncategory @category = 'electronics' , @totalproducts = @total output;
  select @total as totalproductsIncategory;

  ------
  CREATE PROCEDURE GetTotalProductss
	@Category VARCHAR(50),
	@TotalProducts INT OUTPUT
AS
BEGIN
	SELECT @TotalProducts =COUNT(*)
	FROM Products
	WHERE Category=@Category;
END;

DECLARE @Total INT;
EXEC GetTotalProductss 'Electronics' ,@Total OUTPUT;
SELECT @Total AS Totalproducts;


----- transaction - doing multiple task------ multiple dependent statement will wraped in transaction---

CREATE PROCEDURE ProcessOrder 
    @ProductID INT,
    @Quantity INT,
    @OrderDate DATE
AS
BEGIN
    BEGIN TRANSACTION;
    BEGIN TRY
        -- Insert order
        INSERT INTO Orders (ProductID, Quantity, OrderDate)
        VALUES (@ProductID, @Quantity, @OrderDate);

        -- Update product stock
        UPDATE Products
        SET StockQuantity = StockQuantity - @Quantity
        WHERE ProductID = @ProductID;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        -- Handle errors here, such as logging or returning an error message
        THROW;
    END CATCH;
END;

--- adjustment -- adding or subracting from stock----with an condition  if else block----

CREATE PROCEDURE AdjustStock 
    @ProductID INT, 
    @Adjustment INT
AS
BEGIN
    IF @Adjustment > 0
    BEGIN
        -- Add to stock
        UPDATE Products
        SET StockQuantity = StockQuantity + @Adjustment
        WHERE ProductID = @ProductID;
    END
    ELSE IF @Adjustment < 0
    BEGIN
        -- Subtract from stock
        UPDATE Products
        SET StockQuantity = StockQuantity +  @Adjustment
        WHERE ProductID = @ProductID;
    END
END;

-- Example usage:
EXEC AdjustStock @ProductID = 1, @Adjustment = 5; -- Increase stock by 5
EXEC AdjustStock @ProductID = 1, @Adjustment = -3; -- Decrease stock by 3
