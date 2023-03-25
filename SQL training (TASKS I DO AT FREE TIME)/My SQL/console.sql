USE tv_db;

CREATE TABLE reviewers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE series (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    released_year YEAR,
    genre VARCHAR(100)
);

CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(2 , 1 ),
    series_id INT,
    reviewer_id INT,
    FOREIGN KEY (series_id)
        REFERENCES series (id),
    FOREIGN KEY (reviewer_id)
        REFERENCES reviewers (id)
);

INSERT INTO series (title, released_year, genre) VALUES
    ('Archer', 2009, 'Animation'),
    ('Arrested Development', 2003, 'Comedy'),
    ("Bob's Burgers", 2011, 'Animation'),
    ('Bojack Horseman', 2014, 'Animation'),
    ("Breaking Bad", 2008, 'Drama'),
    ('Curb Your Enthusiasm', 2000, 'Comedy'),
    ("Fargo", 2014, 'Drama'),
    ('Freaks and Geeks', 1999, 'Comedy'),
    ('General Hospital', 1963, 'Drama'),
    ('Halt and Catch Fire', 2014, 'Drama'),
    ('Malcolm In The Middle', 2000, 'Comedy'),
    ('Pushing Daisies', 2007, 'Comedy'),
    ('Seinfeld', 1989, 'Comedy'),
    ('Stranger Things', 2016, 'Drama');


INSERT INTO reviewers (first_name, last_name) VALUES
    ('Thomas', 'Stoneman'),
    ('Wyatt', 'Skaggs'),
    ('Kimbra', 'Masters'),
    ('Domingo', 'Cortes'),
    ('Colt', 'Steele'),
    ('Pinkie', 'Petit'),
    ('Marlon', 'Crafford');


INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
    (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
    (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
    (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
    (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
    (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
    (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
    (7,2,9.1),(7,5,9.7),
    (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
    (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
    (10,5,9.9),
    (13,3,8.0),(13,4,7.2),
    (14,2,8.5),(14,3,8.9),(14,4,8.9);

SELECT title, rating
FROM reviews
JOIN series ON series.id = reviews.series_id;

SELECT title, AVG(rating)
FROM reviews
JOIN series ON series.id = reviews.series_id
GROUP BY title
ORDER BY AVG(rating);

SELECT first_name, last_name, rating
FROM reviewers
JOIN reviews ON reviewers.id = reviews.reviewer_id;

SELECT series.title AS unreviewed_series
FROM series
LEFT JOIN reviews ON series.id = reviews.series_id
WHERE rating IS NULL;

SELECT series.genre, AVG(reviews.rating)
FROM series
JOIN reviews ON series.id = reviews.series_id
GROUP BY series.genre;

SELECT reviewers.first_name, reviewers.last_name,
       COUNT(reviews.rating) AS COUNT,
       IFNULL(MIN(reviews.rating), 0.0) AS MIN,
       IFNULL(MAX(reviews.rating), 0.0) AS MAX,
       IFNULL(AVG(reviews.rating), 0.0) AS AVG,
CASE
    WHEN COUNT(reviews.rating) = 0 THEN 'INACTIVE'
    ELSE 'ACTIVE'
END AS STATUS
FROM reviewers
LEFT JOIN reviews
ON reviewers.id = reviews.reviewer_id
GROUP BY reviewers.first_name, reviewers.last_name;

SELECT title, rating, CONCAT_WS(' ', reviewers.first_name, reviewers.last_name) AS reviewer
FROM series
JOIN reviews ON series.id = reviews.series_id
JOIN reviewers ON reviews.reviewer_id = reviewers.id
ORDER BY title;

CREATE VIEW full_reviews AS
SELECT title, released_year, genre, rating, first_name, last_name FROM reviews
JOIN series ON series.id = reviews.series_id
JOIN reviewers ON reviewers.id = reviews.reviewer_id;

SELECT * FROM full_reviews;
SELECT * FROM ordered_series;

SHOW TABLE STATUS;
SHOW TABLES;

SELECT genre, AVG(rating) FROM full_reviews GROUP BY genre;

DELETE FROM full_reviews WHERE released_year = 2010;

INSERT INTO ordered_series (title, released_year, genre)
VALUES ('The great 2020', 2020, 'Comedy');

DELETE FROM ordered_series WHERE title = 'The great 2020';

DELETE FROM ordered_series WHERE title = 'General Hospital';

SELECT * FROM ordered_series;

CREATE OR REPLACE VIEW ordered_series AS
SELECT * FROM series ORDER BY released_year DESC;

ALTER VIEW ordered_series AS
SELECT * FROM series ORDER BY released_year;

DROP VIEW ordered_series;

CREATE VIEW ordered_series AS
SELECT * FROM series ORDER BY released_year;

CREATE OR REPLACE VIEW ordered_series AS
SELECT * FROM series ORDER BY released_year DESC;

ALTER VIEW ordered_series AS
SELECT * FROM series ORDER BY released_year;

DROP VIEW ordered_series;

SELECT * FROM full_reviews;

SELECT title, AVG(rating) FROM full_reviews GROUP BY title;

SELECT title, AVG(rating), COUNT(rating) AS review_count FROM full_reviews
GROUP BY title HAVING COUNT(rating) > 1;

SELECT * FROM full_reviews;

SELECT title, AVG(rating) FROM full_reviews GROUP BY title;

SELECT title, AVG(rating), COUNT(rating) AS review_count FROM full_reviews
GROUP BY title HAVING COUNT(rating) > 1;

SELECT title, AVG(rating) FROM full_reviews GROUP BY title;

SELECT title, AVG(rating) FROM full_reviews GROUP BY title WITH ROLLUP;

SELECT title, COUNT(rating) FROM full_reviews GROUP BY title WITH ROLLUP;

SELECT released_year, AVG(rating)
FROM full_reviews
GROUP BY released_year;


SELECT released_year, AVG(rating)
FROM full_reviews
GROUP BY released_year WITH ROLLUP;

SELECT released_year, genre, AVG(rating)
FROM full_reviews
GROUP BY released_year, genre WITH ROLLUP;

SELECT released_year, genre, AVG(rating)
FROM full_reviews
GROUP BY released_year, genre;

SELECT first_name, released_year, genre, AVG(rating)
FROM full_reviews
GROUP BY released_year, genre, first_name WITH ROLLUP;



