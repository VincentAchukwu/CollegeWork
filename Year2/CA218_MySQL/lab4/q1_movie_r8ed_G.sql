SELECT f.title, f.release_year, c.name, f.description
FROM film f, category c, film_category fc
WHERE f.rating="G" AND f.film_id = fc.film_id AND c.category_id = fc.category_id
/*ORDER BY f.film_id*/