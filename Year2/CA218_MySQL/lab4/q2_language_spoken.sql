/* SELECT cl.Language, co.Name, cl.CountryCode, ((cl.percentage / 100) * co.Population) AS langPop
FROM CountryLanguage cl, Country co
WHERE cl.CountryCode = co.Code
HAVING langPop > 1000000
ORDER BY langPop DESC */

/* EVEN MORE SIMPLIFIED*/
SELECT cl.Language, c.Name AS country, c.Code, cl.CountryCode	/*just to see how it looks..*/
FROM CountryLanguage cl, Country c
WHERE cl.CountryCode = c.Code AND ((cl.Percentage / 100) * c.Population) > 1000000
ORDER BY ((cl.Percentage / 100) * c.Population) DESC