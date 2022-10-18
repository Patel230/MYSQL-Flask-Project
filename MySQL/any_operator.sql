
SELECT * FROM employee;

SELECT * FROM department;

SELECT emp_name 
FROM employee
WHERE dept_num = ANY (SELECT dept_no FROM department WHERE department.dept_no<='15');