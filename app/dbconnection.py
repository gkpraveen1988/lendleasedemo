import mysql.connector
from mysql.connector import Error

def connecttodb():
    config = {
      'user': 'praveen',
      'password': 'Welcome123',
      'host': 'mysqlserver',
      'database': 'employee',
      'raise_on_warnings': True
    }
    try:
        constatus = 1
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
    except  Error as constatus:
        print(constatus)
    return cursor,db,constatus

if __name__ == "__main__":
    cursor,db,constatus = connecttodb()
    print(cursor,db,constatus)
