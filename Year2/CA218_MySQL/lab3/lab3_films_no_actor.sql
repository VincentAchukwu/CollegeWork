SELECT f.film_id, f.title, f.release_year
FROM film f
WHERE f.film_id NOT IN (SELECT fa.film_id
						FROM film_actor fa)