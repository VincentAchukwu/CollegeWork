SELECT co.Name, cl.Language, cl.Percentage
FROM Country co, CountryLanguage cl
WHERE co.Code = cl.CountryCode AND cl.Percentage IN (SELECT MAX(Percentage)
													FROM CountryLanguage
                                                    GROUP BY CountryCode)
GROUP BY cl.CountryCode