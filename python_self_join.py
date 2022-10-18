import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anam@2001",
    database="Company"
)

mycursor = mydb.cursor()

sql = "SELECT e.emp_id, e.emp_name, e.emp_salary, e.emp_age, e.emp_gender, e.emp_dept, e.dept_num,\
        d.dept_name AS Department, d.dept_loc AS Location \
        FROM employee e, department d \
            WHERE e.dept_num <> d.dept_no"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
