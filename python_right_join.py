import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anam@2001",
    database="Company"
)

mycursor = mydb.cursor()

sql = "SELECT emp_id, emp_name, emp_salary, emp_age, emp_gender, emp_dept, dept_num,\
        dept_name AS Department, dept_loc AS Location \
         FROM employee RIGHT JOIN department \
            ON employee.dept_num=department.dept_no"

mycursor.execute(sql)


myresult = mycursor.fetchall()

for x in myresult:
    print(x)
