#update employee table
#GIT path PythonCode/master/

import pymysql
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Enterprise"
)
cur = mydb.cursor()

#cur.execute("update employee set empid=7 where empname='Krishna'")
#mydb.commit()
cur.execute("delete from employee where empid=7")
mydb.commit()
mydb.close()
