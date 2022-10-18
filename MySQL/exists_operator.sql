
SELECT * FROM employee;

SELECT * FROM department;

SELECT emp_name 
FROM employee
WHERE EXISTS (SELECT dept_no FROM department WHERE department.dept_no='35'  AND dept_name='HR');