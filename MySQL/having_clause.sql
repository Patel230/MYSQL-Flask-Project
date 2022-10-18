USE Company;

SELECT * FROM employee;

SELECT * FROM department;

SELECT COUNT(dept_name)
FROM department
GROUP BY dept_name
HAVING COUNT(dept_name)>2;

