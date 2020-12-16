SELECT productName
FROM `classicmodels42`.`products`
WHERE quantityInStock > (SELECT AVG(quantityInStock) FROM `classicmodels42`.`products`);