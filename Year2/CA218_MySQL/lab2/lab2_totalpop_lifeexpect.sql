SELECT SUM(Population), Region, AVG(LifeExpectancy)
FROM Country
GROUP BY Region
ORDER BY AVG(LifeExpectancy) DESC