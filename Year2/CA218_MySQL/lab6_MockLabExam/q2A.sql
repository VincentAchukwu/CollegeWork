SELECT co.Code, co.Name, ci.Name, ((ci.Population / co.Population) * 100) AS percentageInCity
FROM Country co, City ci
WHERE co.Code = ci.CountryCode AND co.LifeExpectancy > 75
ORDER BY percentageInCity DESC