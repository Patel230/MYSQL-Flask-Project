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
    cur.execute("SELECT e.emp_id, e.emp_name, e.emp_salary, e.emp_age, e.emp_gender, e.emp_dept, e.dept_num,\
    d.dept_name AS Department, d.dept_loc AS Location \
    FROM employee e, department d \
    WHERE e.dept_num <> d.dept_no")
    mysql.connection.commit()
    cur.close()
    return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True)
