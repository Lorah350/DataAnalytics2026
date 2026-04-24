USE northwind;
-- comment 1. What is the product name(s) of the most expensive products?
SELECT ProductName
FROM Products
WHERE UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
);

-- comment 2. What is the product name(s) and categories of the least expensive products?
SELECT p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (
    SELECT MIN(UnitPrice)
    FROM Products
);

-- comment 3.  What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT OrderID, ShipName, ShipAddress
FROM Orders
WHERE ShipVia = (
    SELECT ShipperID
    FROM Shippers
    WHERE CompanyName = 'Federal Shipping'
);

-- comment 4.  What are the order ids of the orders that included "Sasquatch Ale"?
SELECT DISTINCT od.OrderID
FROM `order details` od
WHERE od.ProductID = (
    SELECT ProductID
    FROM products
    WHERE ProductName = 'Sasquatch Ale'
);


-- comment 5. What is the name of the employee that sold order 10266?
SELECT FirstName, LastName
FROM employees
WHERE EmployeeID = (
    SELECT EmployeeID
    FROM orders
    WHERE OrderID = 10266
);

-- comment 6. What is the name of the customer that bought order 10266?
SELECT CompanyName
FROM customers
WHERE CustomerID = (
    SELECT CustomerID
    FROM orders
    WHERE OrderID = 10266
);

SHOW tables;


