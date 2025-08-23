CREATE DATABASE hospital_db;

USE hospital_db;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(100)
);

INSERT INTO users (username, password) VALUES ('admin', 'admin123');

CREATE TABLE patients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  gender VARCHAR(10),
  disease VARCHAR(100)
);

INSERT INTO patients (name, age, gender, disease) VALUES
('John Doe', 40, 'Male', 'Fever'),
('Sita Devi', 28, 'Female', 'Asthma');
