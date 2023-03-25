
SELECT * FROM reviews;

CREATE DATABASE animals;
USE animals;

CREATE TABLE cats(
    name VARCHAR(50),
    age INT
);

CREATE TABLE dogs(
    name VARCHAR(50),
    age INT
);

SHOW TABLES;

DROP TABLE dogs;

CREATE TABLE pastires(
name VARCHAR(50),
quantity INT
);

DESC cats;

INSERT INTO cats(name, age)
    VALUES('James', 15),
    ('Miau', 17),
    ('Fire', 22);

CREATE TABLE people(
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT
);

INSERT INTO people(first_name, last_name, age)
VALUES ('Tina', 'Belcher', 13);

INSERT INTO people(first_name, last_name, age)
VALUES ('Linda', 'Belcher', 45),
('Philip', 'Frond', 38),
('Calvin', 'Fischoeder', 70);

SELECT * FROM people;

SHOW TABLES;

DESC people;

CREATE TABLE cats1(
    name VARCHAR(20) DEFAULT 'Missing name',
    surname VARCHAR(20) DEFAULT 'Missing surname',
    age INT DEFAULT 15
);

INSERT INTO cats1 (name)
VALUES ('c');

SELECT * FROM cats1;

CREATE TABLE cats2(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL,
    age INT NOT NULL);

DESC cats4;

CREATE TABLE cats4(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE employees(
id INT AUTO_INCREMENT PRIMARY KEY,
last_name VARCHAR(20) NOT NULL,
first_name VARCHAR(20) NOT NULL,
middle_name VARCHAR(20),
age INT NOT NULL,
current_status VARCHAR(30) DEFAULT 'employed'
);

INSERT INTO employees(last_name, first_name, age)
VALUES('Tom', 'Lincoln', 17);

SELECT * FROM employees;

DROP TABLE cats;

SELECT * FROM cats;

SELECT * FROM cats WHERE name = 'Egg';

SELECT name, breed FROM cats;

SELECT name, age FROM cats;

SELECT cat_id, age FROM cats WHERE cat_id=age; 

UPDATE cats SET breed='Shorthair' WHERE breed='Tabbgy'

UPDATE cats SET name='Jack' WHERE name='Jackson';

SELECT * FROM cats WHERE name='Ringo';

UPDATE cats SET breed='British Shorthair' WHERE name='Ringo';

SELECT * FROM cats WHERE breed='Maine Coon';

UPDATE cats SET age=12 WHERE breed='Maine Coon';

SELECT * FROM cats WHERE age = 4;

DELETE FROM cats WHERE age = 4;

SELECT * FROM cats WHERE age=cat_id;

DELETE FROM cats WHERE age=cat_id;

DELETE FROM cats;