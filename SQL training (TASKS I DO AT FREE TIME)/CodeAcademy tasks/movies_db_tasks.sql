-- 1. Išfiltruoti visus filmus, kuriuose vaidino Sandra (filmų lentelė:
-- ‚film‘, kuriuose filmuose vaidino aktorė ‚film_actor‘, filmų sąrašas
-- – lentelė film).

SELECT actor.first_name, film.title
FROM film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE actor.first_name = 'SANDRA';

-- 2. Suskaičiuoti kiek filmų yra Comedy kategorijoje;

SELECT * FROM film;
SELECT * FROM category;

SELECT name, count(*)
FROM film_category
JOIN category ON category.category_id = film_category.category_id
JOIN film ON film_category.film_id = film.film_id
GROUP BY name
HAVING name='Comedy';

-- 3. Suskaičiuoti už kokią sumą nupirko April Burns (customer lentelėje
-- yra klientai, payment lentelė yra kada ir koks inventorius nuomotas,
-- rental lentelėje yra koks inventorius, inventory lentelėje yra koks
-- filmo id) vasaros mėnesiais. Patikrinti kokios kategorijos filmus ji pirko.

SELECT first_name, last_name, ROUND(SUM(amount), 2) AS APRIL_BOUGHT FROM payment
JOIN customer ON customer.customer_id = payment.customer_id
WHERE first_name = 'APRIL'
GROUP BY first_name, last_name
ORDER BY APRIL_BOUGHT;

-- 4. Pervadinti aktoriaus vardą „Gary“ į „Garis“.

SELECT * FROM actor
WHERE first_name = 'GARY';

UPDATE actor SET first_name='GARIS'
WHERE first_name='GARY';

-- 5. Sukurti naują lentelę, kurioje būtų aktoriaus vardas,
-- aktoriaus pavardė ir kokią sumą jis sugeneravo
-- (suma yra payment lentelėje).

SELECT first_name, last_name, ROUND(SUM(amount), 2) AS AMOUNT
FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN inventory ON inventory.film_id = film_actor.film_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY first_name, last_name
ORDER BY AMOUNT DESC;

-- 6. Suskaičiuoti TOP penkias šalis (payment turi customer_id,
-- customer lentele turi address id, address turi city_id,
-- city turi country id, country id turi šalies pavadinimą).

SELECT country, ROUND(SUM(amount), 2) AS COUNTRY_SUM FROM payment
JOIN customer ON customer.customer_id = payment.payment_id
JOIN address ON address.address_id = customer.customer_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id
GROUP BY country
ORDER BY COUNTRY_SUM DESC
LIMIT 5;

-- 7. Lentelėje category pridėkime naują žandrą – Lithuanian movies;

SELECT * FROM category;
INSERT INTO category(category_id, name, last_update)
VALUES (17, 'Lithuanian movies', '2021-03-06 15:52:00')

-- 8. Prie sukurtos 5-tame punkte lentelės pridėti nauja stulpelį,
-- kuriame būtų kaina Eurais (tarkime, kad dabartinė suma yra doleriais.
-- Imkime kursą 0,91).

CREATE VIEW actor_generator AS
SELECT first_name, last_name, ROUND(SUM(amount), 2) AS AMOUNT
FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN inventory ON inventory.film_id = film_actor.film_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY first_name, last_name
ORDER BY AMOUNT DESC;

SELECT * FROM actor_generator;

SELECT first_name, last_name,
ROUND((AMOUNT * 0.91),  2) || ' Eur' AS 'AMOUNT EUR'
FROM actor_generator;

-- 9. Iš kokio miesto ir valstybės (miestas valstybėje)
-- yra daugiausia klientų?

SELECT customer.customer_id, country.country, COUNT(*)
FROM city
JOIN country ON country.country_id = city.country_id
JOIN address ON city.city_id = address.city_id
JOIN customer ON customer.customer_id = address.address_id
GROUP BY city.city
ORDER BY COUNT(*) DESC;

SELECT country, city, COUNT(*)
FROM city
JOIN country ON country.country_id = city.country_id
GROUP BY country, city
ORDER BY COUNT(*) DESC;


SELECT city, COUNT(*)
FROM city
JOIN country ON country.country_id = city.country_id
GROUP BY city
ORDER BY COUNT(*) DESC;

SELECT country, COUNT(*) FROM city
JOIN country ON country.country_id = city.country_id
GROUP BY country
ORDER BY COUNT(*) DESC;
