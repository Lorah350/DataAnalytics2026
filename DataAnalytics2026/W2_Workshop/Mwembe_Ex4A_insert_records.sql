USE lana_dog_walking;
INSERT INTO Clients
 (FirstName, LastName, Phone, Email, Address)
VALUES
('Maria', 'Johnson', '704-555-1123', 'maria.johnson@example.com', '1420 Willow Bend Dr'),
('Kevin', 'Brooks', '980-555-4421', 'kevin.brooks@example.com', '88 Park Meadow Ln'),
('Aisha', 'Patel', '704-555-9033', 'aisha.patel@example.com', '2301 Sunset Ridge Ct'),
('Daniel', 'Ortiz', '980-555-7712', 'daniel.ortiz@example.com', '512 Oak Crest Cir'),
('Lauren', 'Smith', '704-555-6644', 'lauren.smith@example.com', '1900 Maple Grove Rd'),
('Jamal', 'Rivers', '980-555-8890', 'jamal.rivers@example.com', '77 Brookside Ave'),
('Tanya', 'Green', '704-555-2211', 'tanya.green@example.com', '14 Willow Oak Dr'),
('Brian', 'Carter', '980-555-7788', 'brian.carter@example.com', '902 Lake Forest Way'),
('Nina', 'Lopez', '704-555-3344', 'nina.lopez@example.com', '300 Pine Hollow Ct'),
('Samuel', 'Turner', '980-555-9912', 'samuel.turner@example.com', '55 Meadow Ridge Ln'),
('Olivia', 'Hughes', '704-555-5567', 'olivia.hughes@example.com', '1200 Brookhaven Rd'),
('Chloe', 'Benson', '980-555-4420', 'chloe.benson@example.com', '88 River Birch Ct'),
('Ethan', 'Miller', '704-555-7781', 'ethan.miller@example.com', '2100 Willow Crest Dr'),
('Jasmine', 'Nguyen', '980-555-6633', 'jasmine.nguyen@example.com', '500 Maple Ridge Cir'),
('Carlos', 'Santos', '704-555-8822', 'carlos.santos@example.com', '900 Oak Valley Rd'),
('Maya', 'Reed', '980-555-9910', 'maya.reed@example.com', '33 Brookhaven Terrace');

SELECT * FROM clients;

INSERT INTO Dogs (ClientID, DogName, Breed, Age, Notes)
VALUES
(1, 'Bella', 'Golden Retriever', 4, 'Friendly, loves fetch'),
(1, 'Max', 'Beagle', 2, 'Pulls on leash'),
(2, 'Rocky', 'Pitbull Mix', 5, 'Strong but gentle'),
(3, 'Luna', 'Husky', 3, 'High energy'),
(4, 'Milo', 'Dachshund', 1, 'Nervous around strangers'),
(5, 'Coco', 'Poodle', 6, 'Very calm');


INSERT INTO Walks (DogID, WalkerID, Date, Time, Duration, Notes)
VALUES
(1, 1, '2026-04-10', '10:00:00', 30, 'Sunny day'),
(3, 2, '2026-04-10', '14:00:00', 45, 'Dog was energetic'),
(5, 3, '2026-04-11', '09:30:00', 20, 'Short walk'),
(2, 1, '2026-04-11', '13:00:00', 30, 'Pulled on leash'),
(6, 4, '2026-04-12', '16:00:00', 60, 'Great behavior'),
(4, 2, '2026-04-12', '11:00:00', 40, 'Needed water break');
DESCRIBE Walks;

INSERT INTO Walks (DogID, WalkerID, Date, Time, Duration, Notes)
VALUES
(1, 1, '2026-04-10', '10:00:00', 30, 'Sunny day'),
(3, 1, '2026-04-10', '14:00:00', 45, 'Dog was energetic'),
(5, 3, '2026-04-11', '09:30:00', 20, 'Short walk'),
(1, 4, '2026-04-11', '13:00:00', 30, 'Pulled on leash'),
(4, 2, '2026-04-12', '16:00:00', 60, 'Great behavior'),
(4, 2, '2026-04-12', '11:00:00', 40, 'Needed water break');

SELECT *FROM walks;


