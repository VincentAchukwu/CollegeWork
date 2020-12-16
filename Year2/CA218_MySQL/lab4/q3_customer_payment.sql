SELECT c.first_name, c.last_name, p.amount
FROM customer c, payment p
WHERE c.customer_id = p.customer_id AND p.amount > (SELECT MAX(pc.amount)
													FROM payment pc, customer cu
                                                    WHERE pc.customer_id = cu.customer_id
                                                     AND c.first_name = "Mary")