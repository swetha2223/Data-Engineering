create database Stocks_project;
use Stocks_project;

-- company table --
CREATE TABLE company (
company_id INT PRIMARY KEY,
company_name VARCHAR(255),
ticker_symbol VARCHAR(10)
);

-- stocks table (consider the calculations are done based on week )
CREATE TABLE stocks (
stock_id INT PRIMARY KEY,
company_id INT,
stock_price DECIMAL(10, 2),
trading_volume BIGINT,  -- (No of shares brought on the period)
moving_avg DECIMAL(10, 2), -- ( average number os shares brought in the period of time)
rsi DECIMAL(5, 2), 	-- ( realtive Strength Index means the willingness of people to buy these stocks)
market_cap DECIMAL(15, 2), -- (total value of outstanding shares of the comapny)
record_time TIMESTAMP -- (when the stocks are brought) 
);

-- inserting data into companies table
INSERT INTO company (company_id, company_name, ticker_symbol) VALUES
(1, 'Hexaware', 'HEXA'),
(2, 'Infosys', 'INFY'),
(3, 'Google', 'GOOGL'),
(4, 'Microsoft', 'MSFT'),
(5, 'Accenture', 'ACN'),
(6, 'Cognizant', 'CTSH');

-- insertion of data into stocks table
INSERT INTO stocks (stock_id, company_id, stock_price, trading_volume, moving_avg, rsi, market_cap, record_time) VALUES
(1, 1, 182.91, 5000000, 4800000, 65.32, 28750000000, '2024-08-19 10:00:00'), -- Hexaware
(2, 2, 330.43, 30000000, 29500000, 60.25, 248000000000, '2024-08-19 10:00:00'), -- Infosys
(3, 2, 332.12, 31000000, 30000000, 61.58, 249500000000, '2024-08-26 10:00:00'), -- Infosys
(4, 3, 140.86, 60000000, 59000000, 55.44, 1440000000000, '2024-08-19 10:00:00'), -- Google
(5, 3, 141.50, 61000000, 59500000, 56.01, 1450000000000, '2024-08-26 10:00:00'), -- Google
(6, 4, 255.99, 15000000, 14800000, 52.16, 812000000000, '2024-08-19 10:00:00'), -- Microsoft
(7, 4, 258.12, 15500000, 15000000, 53.45, 815000000000, '2024-08-26 10:00:00'), -- Microsoft
(8, 4, 259.30, 15700000, 15200000, 54.70, 817000000000, '2024-09-02 10:00:00'), -- Microsoft
(9, 5, 132.68, 22000000, 21500000, 48.23, 1720000000000, '2024-08-19 10:00:00'), -- Accenture
(10, 5, 133.75, 22500000, 22000000, 49.80, 1730000000000, '2024-08-26 10:00:00'), -- Accenture
(11, 6, 270.02, 18000000, 17500000, 64.10, 780000000000, '2024-08-19 10:00:00'), -- Cognizant
(12, 6, 272.10, 18500000, 17800000, 65.50, 785000000000, '2024-08-26 10:00:00'), -- Cognizant
(13, 6, 273.85, 19000000, 18200000, 66.80, 790000000000, '2024-09-02 10:00:00'), -- Cognizant
(14, 2, 334.55, 31500000, 30500000, 62.70, 251000000000, '2024-09-02 10:00:00'), -- Infosys
(15, 1, 184.10, 5300000, 4950000, 67.02, 28900000000, '2024-09-02 10:00:00'); -- Hexaware

-- Average Stocks price
SELECT company_name, AVG(stock_price) AS avg_stock_price
FROM stocks sf
JOIN company cd ON sf.company_id = cd.company_id
GROUP BY company_name
ORDER BY avg_stock_price DESC;

-- Top performning company in the last week 
SELECT c.company_name, SUM(s.trading_volume) AS total_stocks_sold
FROM company c
JOIN stocks s ON c.company_id = s.company_id
WHERE s.record_time >= NOW() - INTERVAL 7 DAY
GROUP BY c.company_name
ORDER BY total_stocks_sold DESC
LIMIT 1;

-- Order of willigness of customer for the companies based on the trend
select distinct company_name from company c 
join stocks s on c.company_id=s.company_id
group by company_name
order by avg(rsi);  


-- 
