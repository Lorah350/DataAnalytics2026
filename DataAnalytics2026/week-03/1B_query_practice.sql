USE northwind;
-- comment. Write a query to list the product id, product name, and unit price of every product that

SELECT ProductID, ProductName, UnitPrice
FROM Products;
-- comment . Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductID, ProductName, UnitPrice
 FROM products 
 WHERE UnitPrice <= 7.50;
-- comment  What are the products that we carry where we have no units on hand, but 1 or more are on backorder? Write a query that answers this question.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock =0
AND UnitsOnOrder >0;
-- comment . Examine the products table. How does it identify the type (category) of each item
sold? Where can you find a list of all categories? Write a set of queries to answer these
questions, ending with a query that creates a list of all the seafood items we carry.
SELECT * FROM categories;
SELECT p.ProductID, p.ProductName, p.UnitPrice
FROM products AS p
JOIN categories AS c
  ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';
SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE CategoryID = 8;
-- comment Examine the products table again. How do you know what supplier each product
comes from? Where can you find info on suppliers? Write a set of queries to find the
specific identifier for "Tokyo Traders" and then find all products from that supplier.
SELECT * FROM suppliers;
SELECT supplierID
FROM suppliers
WHERE CompanyName = 'Tokyo Traders';

SELECT p.ProductID, p.ProductName, p.UnitPrice
FROM products AS p
JOIN suppliers AS s
  ON p.SupplierID = s.SupplierID
WHERE s.CompanyName = 'Tokyo Traders';
-- comment How many employees work at northwind? What employees have "manager"
somewhere in their job title? Write queries to answer each question.

SELECT * FROM employees;
SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE Title LIKE '%manager%';

-- comment  How many employees work at northwind?
SELECT COUNT(*) AS total_employees
FROM employees;



