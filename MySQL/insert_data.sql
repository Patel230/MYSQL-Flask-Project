USE Company;

INSERT INTO employee (emp_id, emp_name, emp_salary,  emp_age, emp_gender, emp_dept) 
VALUES ('1', 'Sam', '95000', '45', 'M', 'Operations'),
	   ('2', 'Bob', '80000', '21', 'M', 'Support'),
	   ('3', 'Anne', '125000', '25', 'F', 'Analytics'),
	   ('4', 'Julia', '73000', '30', 'F', 'Analytics'),
	   ('5', 'Matt', '159000', '33', 'M', 'Sales'),
	   ('6', 'Jeff', '112000', '27', 'M', 'Operations');

SELECT * FROM employee;       
       