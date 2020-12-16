SELECT f.film_id, f.title, f.release_year, ca.name
FROM film f, category ca, film_category fc
WHERE f.description LIKE "%Moose%" AND f.film_id = fc.film_id AND ca.category_id = fc.category_id
ORDER BY f.film_id