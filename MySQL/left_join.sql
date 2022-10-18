SELECT * FROM employee;

SELECT * FROM department;

SELECT emp_id, emp_name, emp_salary, emp_age, emp_gender, emp_dept, dept_num, 
dept_name AS Department, dept_loc AS Location
FROM employee LEFT JOIN department
ON employee.dept_num=department.dept_no;