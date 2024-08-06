import mysql.connector

con = mysql.connector.connect(
    host = "localhost" ,user ='root' ,password ="password",database='emp')

def check_employee(employee_id):
    sql = 'SELECT * FROM employee WHERE id=%s'
    
    cursor = con.cursor(buffered=True)
    data =(employee_id,)
    cursor.execute(sql,data)
    employee =cursor.fetchone()
    cursor.close()
    
    return employee is not None