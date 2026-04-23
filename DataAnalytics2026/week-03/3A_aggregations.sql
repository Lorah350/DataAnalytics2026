USE northwind;
-- comment 1.  find the price of the cheapest item that Northwind sells. 
SELECT MIN(UnitPrice) AS CheapestPrice
FROM products;
-- comment b. -- 1b. Find the name of the product with that price.
SELECT ProductName,UnitPrice
FROM products 
WHERE Unitprice = (SELECT MIN(UnitPrice) AS CheapestPrice);

-- 2. Find the average price of all items Northwind sells.
SELECT AVG(UnitPrice) AS Averageprice
FROM products;


--  comment b. Bonus: Round the average price to the nearest cent.
SELECT ROUND(AVG(UnitPrice), 2) AS RoundedAveragePrice
FROM Products;

-- comment  3. Find the price of the most expensive item Northwind sells.
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM Products;

-- comment b. Find the product name and supplier name for that item.
SELECT 
    p.ProductName,
    p.UnitPrice,
    s.CompanyName AS SupplierName
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM Products);
SELECT * FROM employees;

-- comment 4. Find total monthly payroll (sum of all employees' monthly salaries).
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;

-- comment  5. Identify the highest and lowest salary amounts.
SELECT 
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employees;

-- comment 6. Find the name and supplier ID of each supplier and the number of items they supply.
SELECT 
    s.SupplierID,
    s.CompanyName,
    COUNT(p.ProductID) AS NumberOfItemsSupplied
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

-- comment 7. List all category names and the average price for items in each category.
SELECT 
    c.CategoryName,
    ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

--  comment 8. Suppliers that provide at least 5 items
SELECT 
    s.CompanyName AS SupplierName,
    COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5
ORDER BY NumberOfItems DESC;

-- comment 9. Products currently in inventory with inventory value
SELECT 
    ProductID,
    ProductName,
    (UnitPrice * UnitsInStock) AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;


