USE Company;

SELECT * FROM employee;

SELECT * FROM department;

SELECT emp_dept, dept_num
FROM employee
UNION ALL
SELECT dept_name, dept_no
FROM department;

