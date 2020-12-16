SELECT cs.contactFirstName, c.first_name
FROM customers cs, sakila.customer c
WHERE cs.contactFirstName LIKE c.first_name
GROUP BY c.first_name