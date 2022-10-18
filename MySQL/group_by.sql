
SELECT COUNT(dept_num) , emp_dept
FROM employee
GROUP BY emp_dept;

SELECT COUNT(dept_num) , emp_dept
FROM employee
GROUP BY emp_dept
ORDER BY emp_dept;

SELECT COUNT(dept_num) , emp_dept
FROM employee
GROUP BY emp_dept
ORDER BY emp_dept DESC;