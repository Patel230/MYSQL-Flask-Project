SELECT * FROM employee;

SELECT emp_name, IFNULL(emp_age, 0)
FROM employee;

SELECT emp_name, COALESCE(emp_age, 0)
FROM employee;