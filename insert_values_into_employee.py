from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anam@2001'
app.config['MYSQL_DB'] = 'Company'

mysql = MySQL(app)


@app.route('/')
def index(cur=None):
    # employee_id = 16 employee_name = "Devid" employee_age = 21 cur = mysql.connection.cursor() cur.execute("USE
    # company") cur.execute("INSERT INTO employee(emp_id, name, age) VALUES (%s,%s,%s)", (employee_id, employee_name,
    # employee_age))
    cur = mysql.connection.cursor()
    # cur.execute("USE Company")
    cur.execute("INSERT INTO employee (emp_id, emp_name, emp_salary,  emp_age, "
                "emp_gender, emp_dept, dept_num) VALUES "
                "('1', 'Sam', '95000', '45', 'M', 'Operations', '5'),"
                "('2', 'Bob', '80000', '21', 'M', 'Support', '15'),"
                "('3', 'Anne', '125000', '25', 'F', 'Analytics', '10'),"
                "('4', 'Julia', '73000', '30', 'F', 'Analytics', '20'),"
                "('5', 'Matt', '159000', '33', 'M', 'Sales', '30'),"
                "('6', 'Jeff', '112000', '27', 'M', 'Operations', '25')")

    mysql.connection.commit()
    cur.close()
    return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True)
