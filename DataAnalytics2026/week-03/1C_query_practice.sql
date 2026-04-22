USE northwind;
 Write a query to list the product id, product name, and unit price of every product. This
time, display them in ascending order by price.
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY  UnitPrice ASC;

-- comment What are the products that we carry where we have at least 100 units on hand? Order
them in descending order by price. If two or more have the same price, list those in
ascending order by product name.
SELECT productID, ProductName, UnitsInStock, UnitPrice
FROM products 
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- comment  Write a query against the orders table that displays the total number of distinct
customers who have placed orders, based on customer ID. Use an alias to label the
count calculation as CustomerCount.

-- 4. Total number of distinct customers who have placed orders.
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders;

-- comment Write a query against the orders table that displays the total number of distinct
customers who have placed orders, by customer ID, for each country where orders
have been shipped. Again, use an alias to label the count as CustomerCount. Order
the list by the CustomerCount, largest to smallest.

SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

products that we carry where we have less than 25 units on hand, but 1
or more units of them are on order? Write a query that orders them by quantity on
order (high to low), then by product name.

-- 6. Products with less than 25 units in stock and at least 1 unit on order.
--    Ordered by units on order descending, then product name.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25
  AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- comment  Write a query to list each of the job titles in employees, along with a count of how
many employees hold each job title.

-- 7. Job titles and how many employees hold each title.
SELECT Title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title;
 What employees have a monthly salary that is between $2000 and $2500? Write a
query that orders them by job title.

SELECT employeeID, FirstName, LastName, Title, Salary
FROM employees 
WHERE salary between 2000 and 2500
ORDER BY title ASC;



