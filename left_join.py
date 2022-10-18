from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anam@2001'
app.config['MYSQL_DB'] = 'Company'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    # cur.execute("USE Company")
    cur.execute("SELECT emp_id, emp_name, emp_salary, emp_age, emp_gender, emp_dept, dept_num,dept_name AS "
                "Department, dept_loc AS Location FROM employee LEFT JOIN department ON "
                "employee.dept_num=department.dept_no")
    mysql.connection.commit()
    cur.close()
    return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True)
