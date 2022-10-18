SELECT * FROM employee;

SELECT emp_name, emp_age,
CASE
    WHEN emp_age > 30 THEN 'The age is greater than 30'
    WHEN emp_age = 30 THEN 'The age is 30'
    ELSE 'The age is under 30'
END AS AgeText
FROM employee;  