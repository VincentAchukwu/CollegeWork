SELECT pl.productLine, pl.textDescription, COUNT(od.quantityOrdered) AS myCount
FROM productlines pl, products p, orderdetails od
WHERE pl.productLine = p.productLine AND p.productCode = od.productCode
GROUP BY pl.productLine
ORDER BY myCount DESC
LIMIT 3