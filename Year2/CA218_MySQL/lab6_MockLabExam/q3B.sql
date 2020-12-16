SELECT p.productName, SUM(od.quantityOrdered) AS tot, COUNT(DISTINCT c.customerNumber), ROUND((p.MSRP - p.buyPrice) * SUM(od.quantityOrdered), 2) AS profit
FROM products p, orderdetails od, orders o, customers c
WHERE p.productCode = od.productCode AND od.orderNumber = o.orderNumber AND c.customerNumber = o.customerNumber
GROUP BY p.productCode
HAVING tot > (SELECT SUM(quantityOrdered)
				FROM orderdetails
                WHERE productCode = 'S18_3685')
                AND SUM(od.quantityOrdered) > 200
                AND COUNT(DISTINCT c.customerNumber) > 20