DROP DATABASE shirts;

CREATE DATABASE shirts;


USE shirts;


CREATE TABLE shirts(
shirt_id INT PRIMARY KEY AUTO_INCREMENT,
article VARCHAR(20),
color VARCHAR(20),
shirt_size VARCHAR(10),
last_warn int
);


INSERT INTO shirts(article, color, shirt_size, last_warn)
VALUES ('t-shirt', 'white', 'S', 10),
		('t-shirt', 'green', 'S', 200),
		('polo shirt', 'black', 'M', 10),
		('tank top', 'blue', 'S', 50),
		('t-shirt', 'pink', 'S', 0),
		('polo shirt', 'red', 'M', 5),
		('tank top', 'white', 'S', 200),
		('tank top', 'blue', 'M', 15);

SHOW tables;

DESC shirts;

SELECT * FROM shirts;

INSERT INTO shirts(article, color, shirt_size, last_warn)
VALUES ('polo shirt', 'purple', 'M', 50);

SELECT article, color FROM shirts;

SELECT * FROM shirts;

SELECT article, color, shirt_size, last_warn 
FROM shirts WHERE shirt_size='M';

SELECT * FROM shirts WHERE article='polo shirt';

UPDATE shirts SET shirt_size='L' 
WHERE article='polo shirt';

SELECT * FROM shirts WHERE last_warn=15;

UPDATE shirts SET last_warn=0 WHERE last_warn=15;

SELECT * FROM shirts WHERE color='white';

UPDATE shirts SET shirt_size='XS' WHERE color='white';

DELETE FROM shirts WHERE last_warn=200;

DELETE FROM shirts WHERE article='polo shirt';

DELETE FROM shirts;

DROP DATABASE shirts;

