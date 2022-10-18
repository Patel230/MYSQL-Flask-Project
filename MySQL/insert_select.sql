USE Company;

INSERT INTO employee (emp_dept)
SELECT dept_name FROM department 
WHERE dept_no>=15;
