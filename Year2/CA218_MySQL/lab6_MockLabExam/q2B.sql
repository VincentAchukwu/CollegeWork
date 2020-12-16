SELECT co.Name, co.Population, COUNT(cl.Language) AS langCount
FROM Country co, CountryLanguage cl
WHERE co.Code = cl.CountryCode AND co.Population > (
									SELECT AVG(Population)
									FROM Country
									)
GROUP BY co.Name
ORDER BY langCount DESC