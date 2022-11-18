-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP VIEW IF EXISTS "main"."vw_top_sellers";
CREATE VIEW vw_top_sellers
AS
SELECT sales_rep, MAX(sale_amount) AS total_sales, CAST(year as integer) as year FROM
(SELECT Employee.FirstName || ' ' || Employee.LastName as sales_rep, SUM(Invoice.Total) AS sale_amount, strftime('%Y', InvoiceDate) as year
FROM Invoice INNER JOIN Customer
ON Customer.CustomerId = Invoice.CustomerId
INNER JOIN Employee
ON Employee.EmployeeId = Customer.SupportRepId
GROUP BY Employee.EmployeeId, strftime('%Y', InvoiceDate)
ORDER BY SUM(Invoice.Total) DESC)
GROUP BY year;