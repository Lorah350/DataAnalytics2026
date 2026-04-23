USE northwind;

-- comment list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name.

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products AS p
JOIN categories AS c
  ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName ASC, p.ProductName ASC;

 -- comment list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name.

SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products AS p
JOIN suppliers AS s
  ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName ASC;

-- comment list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name.

SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.CompanyName AS SupplierName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN Suppliers s ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;

-- 4. Orders shipped to Germany with shipper name
SELECT 
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    sh.CompanyName AS Shipper
FROM Orders o
JOIN Shippers sh ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName;

--  Same as #4, but omit OrderID and group by ship name.
-- 5    Count how many orders were shipped for each ship name.
SELECT 
    o.ShipName,
    COUNT(*) AS TotalOrders
FROM Orders o
JOIN Shippers sh ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName
ORDER BY o.ShipName;

-- 6. List order id, order date, ship name, and ship address of all orders
--    that included Sasquatch Ale. Requires joining 3 tables.
SELECT 
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM Orders o
JOIN `Order Details` od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale'
ORDER BY o.OrderID;
