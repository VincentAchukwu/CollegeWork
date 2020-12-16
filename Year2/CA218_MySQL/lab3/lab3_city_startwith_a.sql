SELECT c.Name AS cityName, c.CountryCode AS codeCountry, n.Name AS countryName
FROM City c, Country n
WHERE c.Name LIKE 'A%' AND c.CountryCode = n.Code