from logging import debug
from flask import Flask, render_template, request
from pymysql import connections
from pymysql.cursors import Cursor
app = Flask(__name__, template_folder='template')
db_conn = connections.Connection(
    host = "dbmysqlproject.c0edlhsmspoa.us-east-1.rds.amazonaws.com",
    port = 3306,
    user = "projectadmin",
    password = "1Strongpassword.10",
    db = "employee"
)
output = {}
table = 'employee';
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('employee_app.html')

@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_name = request.form['FieldName']
    emp_age = request.form['FieldAge']
    emp_city = request.form['FieldCity']
    emp_county= request.form['FieldCountry']
    
    insert_sql = "insert into employee(name,age,city,country) values(%s,%s,%s,%s)"
    cursor= db_conn.cursor()

    try:
        cursor.execute(insert_sql,(emp_name,emp_age,emp_city,emp_county))
        db_conn.commit()
        print("Data Inserted in MySQL RDS")
    
    except Exception as e:
        return str(e)
    finally:
        cursor.close()

    print("Done")
    return render_template('addEmpOutput.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=80,debug=True)

