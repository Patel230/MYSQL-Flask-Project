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
    cur = mysql.connection.cursor()
    # cur.execute("USE Company")
    cur.execute("INSERT INTO department (dept_no, dept_name, dept_loc) VALUES "
                "('5', 'Operations', 'New York'),"
                "('10', 'Support', 'Chicago'),"
                "('15', 'Development', 'San Diego'),"
                "('20', 'Support', 'Dallas'),"
                "('25', 'Sales', 'San Jose'),"
                "('30', 'Analytics', 'Phoenix'),"
                "('35', 'HR', 'Chicago'),"
                "('40', 'Support', 'Los Angeles')")

    mysql.connection.commit()
    cur.close()
    return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True)