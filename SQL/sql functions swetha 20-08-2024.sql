-- string functions--
SELECT ascii ( 'AB');
SELECT char (66);
SELECT len ( 'example')
SELECT lower ( 'ENGLISH') 
SELECT REPLACE ( 'harini','i','y' )
SELECT reverse ( 'game')
SELECT str (134.56, 6, 2)
SELECT upper ('english')


----date functions---
SELECT dateadd (mm, 2, '2010-04-03')

SELECT datediff ( year, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'))
SELECT datepart (mm, '2008-01-01')
SELECT day ( '2010-03-21')
SELECT month ('2007-04-03')
SELECT year ( '2011-04-17')

CREATE TABLE subjects (
  subid INT,
  subname VARCHAR(255),
  examdate DATETIME,
  location VARCHAR(255)
);





INSERT INTO subjects (subid, subname, examdate, location)
VALUES
(201, 'Science', '2010-04-05 00:00:00.000', 'Mumbai'),
(202, 'English', '2011-04-05 00:00:00.000', 'Lucknow'),
(203, 'Maths', '2010-04-05 00:00:00.000', 'Delhi'),
(204, 'Social Science', '2012-04-05 00:00:00.000', 'Pune');

select subid, DATEPART(yy,'2010-04-05') as year from subjects


---Mathematical functions----


SELECT abs (-79)
SELECT sin(1.5)
SELECT ceiling (14.46)
SELECT exp (4.5)
SELECT floor (15.15)
SELECT log (5.8)


CREATE TABLE workers (
  empid VARCHAR(255),
  designation VARCHAR(255),
  hourrate DECIMAL(10, 4)
);

INSERT INTO workers (empid, designation, hourrate)
VALUES
  ('E201', 'Lead', 13.654),
  ('E202', 'Developer', 10.2364),
  ('E207', 'Consultant', 20.6164),
  ('E250', 'Manager', 22.9876),
  ('E261', 'Unit Head', 45.3211);

  select empid, 'Hourly Rate'= ROUND(hourrate,2) from workers

  ---aggregrate functions---

  --avg---
  select 'Average Rate' =avg(hourrate) from workers

  -- min--
     select 'Minimum Rat'=Min(hourrate) from workers

	 -- max--
     select 'Maximum Rat'=Max(hourrate) from workers

	 -- count---
	 select 'Unique Rate'=COUNT( DISTINCT hourrate) from workers

	 --sum--
	 select 'Sum'=SUM(hourrate) from workers

	 ---- group by---

	 select designation,avg(hourrate)
	 as avg_hourrate
	 from workers
	 group by designation;


	 ----compute--

	select SUM(hourrate) as 
	compute_total_hourrate
	from workers








