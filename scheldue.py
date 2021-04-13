
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors
import pymysql
from pymysql import cursors
from datetime import datetime
import mysql.connector
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
# app.config['MYSQL_DB'] = 'cts'
# mysql = MySQL(app) 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="cts"
    )
@app.route('/')
def home():
    return "a"
def ac():
 
    # title = "a"
    # des = "Anh yeu em"
    # startday = "2021-04-04"
    # endday = "2021-04-04"
    # state = 1
    # limit = 7
    # point = 100
    # mycursor = mydb.cursor()
    # mycursor.execute('insert INTO  mission\
    #             (`Title`, `Description`, `StartDate`, EndDate,`State`, `Limit`, `Point`) \
    #                 VALUES (%s, %s, %s,%s,%s,%s,%s)',\
    #                 (title,des,startday,endday,state,limit,point,))
    # mydb.commit()

    print("record inserted.")

if __name__ == "__main__":
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(ac,'interval',seconds=5)
    sched.start()

    app.run()