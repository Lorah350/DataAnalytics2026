DROP SCHEMA IF EXISTS lana_dog_walking;
CREATE SCHEMA lana_dog_walking;
USE lana_dog_walking;
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);
CREATE TABLE Walkers (
    WalkerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100)
);
CREATE TABLE Dogs (
    DogID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT,
    DogName VARCHAR(50),
    Breed VARCHAR(50),
    Age INT,
    Notes VARCHAR(255),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);
CREATE TABLE Walks (
    WalkID INT AUTO_INCREMENT PRIMARY KEY,
    DogID INT,
    WalkerID INT,
    Date DATE,
    Time TIME,
    Duration INT,
    Notes VARCHAR(255),
    FOREIGN KEY (DogID) REFERENCES Dogs(DogID),
    FOREIGN KEY (WalkerID) REFERENCES Walkers(WalkerID)
);
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    WalkID INT,
    Amount DECIMAL(10,2),
    PaymentMethod VARCHAR(50),
    PaymentDate DATE,
    FOREIGN KEY (WalkID) REFERENCES Walks(WalkID)
);

