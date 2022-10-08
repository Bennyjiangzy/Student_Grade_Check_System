create database assign;
use assign;

CREATE USER 'test'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON assign.* TO 'test'@'%';

CREATE TABLE user
(id INT NOT NULL AUTO_INCREMENT, 
username VARCHAR(250) NOT NULL,
password VARCHAR(250) NOT NULL,
CONSTRAINT blood_pressure_pk PRIMARY KEY (id));


CREATE TABLE grade
(id INT NOT NULL AUTO_INCREMENT, 
studentID VARCHAR(250) NOT NULL,
name VARCHAR(250) NOT NULL,
grade INT NOT NULL,
date_created VARCHAR(100) NOT NULL,
CONSTRAINT blood_pressure_pk PRIMARY KEY (id));