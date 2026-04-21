DROP SCHEMA IF EXISTS lana_dog_walking;
CREATE SCHEMA lana_dog_walking;
USE lana_dog_walking;

CREATE TABLE Customer_Data (
    Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_Name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

CREATE TABLE Dog_Data (
    Dog_ID INT AUTO_INCREMENT PRIMARY KEY,
    Dog_Name VARCHAR(100) NOT NULL,
    Dog_Breed VARCHAR(100),
    Age INT,
    Weight INT,
    Special_Instruction VARCHAR(255),
    Customer_ID INT,
    FOREIGN KEY (Customer_ID) REFERENCES Customer_Data(Customer_ID)
);

CREATE TABLE Appointment_Data (
    Appointment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Appointment_Date DATE,
    Appointment_Time TIME,
    Duration INT,
    Dog_ID INT,
    FOREIGN KEY (Dog_ID) REFERENCES Dog_Data(Dog_ID)
);

CREATE TABLE Payments_Data (
    Payment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Payment_Date DATE,
    Amount DECIMAL(10,2),
    Payment_Status VARCHAR(50),
    Customer_ID INT,
    FOREIGN KEY (Customer_ID) REFERENCES Customer_Data(Customer_ID)
);