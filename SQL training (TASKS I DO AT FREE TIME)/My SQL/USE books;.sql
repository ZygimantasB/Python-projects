USE books;

DROP TABLE books;

SELECT * FROM books;

CREATE TABLE books 
	(
		book_id INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);


SELECT REVERSE(UCASE('Why does my cat look at me with such hatred?'))

SELECT * FROM books;

SELECT REPLACE(title, ' ', '->') FROM books 

SELECT author_lname AS forwards, REVERSE(author_lname) AS backwards 
FROM books;

SELECT UCASE(CONCAT_WS(' ', author_fname, author_lname)) 
AS 'full name in caps' FROM books;

SELECT CONCAT_WS(' was released in ', title, released_year) AS blurp
FROM books;

SELECT title, CHAR_LENGTH(title) FROM books;


SELECT CONCAT(LEFT(title, 10), '...') AS 'short title',
CONCAT_WS(',' ,author_lname, author_fname) AS author,
CONCAT(CHAR_LENGTH(title), ' in stock') AS quantity
FROM books;

INSERT INTO books
    (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);


SELECT DISTINCT released_year, COUNT(released_year) 
FROM books GROUP BY released_year;

SELECT book_id, author_fname, author_lname, pages FROM books ORDER BY 3;

SELECT title FROM books WHERE title LIKE '%stories%';

SELECT * FROM books;

SELECT title, pages FROM BOOKS WHERE pages = (SELECT MAX(pages) FROM books);

SELECT CONCAT_WS(' - ', title, released_year) FROM books 
ORDER BY released_year DESC LIMIT 3;

SELECT title, released_year, author_lname FROM books 
WHERE author_lname LIKE '% %';

SELECT title, author_lname FROM books ORDER BY author_lname, title; 

SELECT UCASE(CONCAT('My favorite author is' , ' ', 
CONCAT_WS(' ', author_fname, author_lname))) AS yell
FROM books
ORDER BY author_lname;

SELECT COUNT(DISTINCT(released_year)) FROM books;

SELECT COUNT(*) FROM books;

SELECT released_year, count(*) FROM books GROUP BY released_year
ORDER BY count(*) DESC;

SELECT SUM(stock_quantity) FROM books;

SELECT CONCAT_WS(' ',author_lname, author_fname) AS full_name,
AVG(released_year)
FROM books
GROUP BY full_name;

SELECT CONCAT_WS(' ',author_lname, author_fname) AS full_name,
SUM(pages) FROM books
GROUP BY full_name
ORDER BY SUM(pages) DESC
LIMIT 1;

SELECT CONCAT_WS(' ', author_lname, author_fname) AS full_name,
pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);

SELECT released_year, COUNT(released_year), AVG(pages) FROM books
GROUP BY released_year
ORDER BY released_year;


SELECT * FROM books WHERE released_year < 1980;

SELECT * FROM books WHERE author_lname='Eggers' 
OR author_lname='Chabon';

SELECT * FROM books WHERE author_lname='Lahiri' 
AND released_year > 2000;

SELECT * FROM books WHERE pages BETWEEN 100 AND 200;

SELECT author_lname FROM books WHERE author_lname LIKE 'C%' OR
author_lname LIKE 'S%';

SELECT title, author_lname,
CASE
    WHEN title LIKE '%Stories%' THEN 'Shorten Stories'
    WHEN title LIKE '%Just Kids%%' THEN 'Memoir'
    ELSE 'Novel'
    END AS TYPE
FROM books;


SELECT author_fname, author_lname,
CASE 
    WHEN COUNT(title) = 1 THEN '1 Book'
    ELSE CONCAT_WS(' ',COUNT(title), 'books')
END AS COUNT
FROM books
GROUP BY author_fname, author_lname;
