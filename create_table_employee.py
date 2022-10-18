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
    cur.execute("CREATE TABLE employee (emp_id INT PRIMARY KEY, emp_name VARCHAR(25), emp_salary INT, "
                " emp_age INT, emp_gender CHAR(1), emp_dept VARCHAR(25), dept_num INT)")
    mysql.connection.commit()
    cur.close()
    return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True)
