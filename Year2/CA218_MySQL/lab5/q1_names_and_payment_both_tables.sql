SELECT *
FROM 
(SELECT sc.first_name, sc.last_name, SUM(sp.amount) AS sakilaSum
FROM sakila.customer sc, sakila.payment sp
WHERE sc.customer_id = sp.customer_id
GROUP BY sc.customer_id) AS sakilaTable
UNION ALL
(SELECT c.contactFirstName, c.contactLastName, SUM(p.amount) AS classicSum
FROM customers c, payments p
WHERE c.customerNumber = p.customerNumber
GROUP BY c.customerNumber)
ORDER BY first_name


/*SELECT c.contactFirstName, c.contactLastName, SUM(p.amount), sc.first_name, sc.last_name, SUM(sp.amount)
FROM customers c, payments p, sakila.customer sc, sakila.payment sp
WHERE c.customerNumber = p.customerNumber AND sc.customer_id = sp.customer_id
GROUP BY p.customerNumber, sp.customer_id;*/