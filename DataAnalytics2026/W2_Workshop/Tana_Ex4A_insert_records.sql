USE lana_dog_Walking;
INSERT INTO Customers (CustomerID, Name, Phone, Address, Email) VALUES
(1, 'John Smith', '4041234567', '123 Main St', 'john@email.com'),
(2, 'Sarah Lee', '6789876543', '456 Oak Ave', 'sarah@email.com'),
(3, 'Michael Brown', '7705551234', '789 Pine Rd', 'michael@email.com'),
(4, 'Emily Davis', '4048882222', '321 Maple St', 'emily@email.com'),
(5, 'David Wilson', '6783334444', '654 Cedar Ln', 'david@email.com');
INSERT INTO Dogs (DogID, Name, Breed, Age, CustomerID) VALUES
(101, 'Max', 'Labrador', 5, 1),
(102, 'Bella', 'Poodle', 3, 2),
(103, 'Rocky', 'Bulldog', 4, 3),
(104, 'Luna', 'Husky', 2, 4),
(105, 'Charlie', 'Beagle', 6, 5);
INSERT INTO Walks (WalkID, Date, Time, Duration, DogID) VALUES
(1001, '2026-04-15', '09:00:00', 30, 101),
(1002, '2026-04-16', '10:00:00', 45, 102),
(1003, '2026-04-17', '08:30:00', 30, 103),
(1004, '2026-04-18', '11:00:00', 60, 104),
(1005, '2026-04-19', '07:45:00', 20, 105);
INSERT INTO Payments (PaymentID, Amount, Date, CustomerID) VALUES
(5001, 25.00, '2026-04-15', 1),
(5002, 40.00, '2026-04-16', 2),
(5003, 30.00, '2026-04-17', 3),
(5005, 20.00, '2026-04-19', 5);