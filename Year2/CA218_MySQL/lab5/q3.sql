SELECT pl.productLine, SUM((od.priceEach - p.buyPrice) * od.quantityOrdered) AS income
FROM productlines pl, products p, orderdetails od
WHERE pl.productLine = p.productLine AND p.productCode = od.productCode
GROUP BY p.productLine
ORDER BY income DESC
LIMIT 1