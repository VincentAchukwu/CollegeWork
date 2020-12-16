SELECT f.title, c.name
FROM film f, film_category fc, category c
WHERE f.film_id = fc.film_id AND fc.category_id = c.category_id AND f.title LIKE 'A%'
ORDER BY f.title