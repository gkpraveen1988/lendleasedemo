from dbconnection import *
import json

# FUNCTION TO RUN THE QUERIES WITH SQL COMMANDS
def runSqlcommand(sql,val,stat):
    mydict = {}
    conncur, conn, constatus = connecttodb()
    try:
        conncur.execute(sql, val)
        conn.commit()
        status = (f"Record {stat} {conncur.rowcount}")
        mydict['status'] = status
    except:
        status = "Error while pushing the data"
    
    mydict['status'] = status
    return mydict

# FUCNTION TO CREATE AND UPDATE THE USER ON DUPLICATE KEY
def createUpdateUser(inputData):
    sql = "insert into customerdata (custnumber,fname,mname,lname,dob,gender,department,location) \
        values (%s,%s,%s,%s,%s,%s,%s,%s)"

    val = (str(inputData['custnumber']),str(inputData['fname']),str(inputData['mname']),\
      str(inputData['lname']),str(inputData['dob']),str(inputData['gender']),str(inputData['department']),\
      str(inputData['location']))

    status = 'Inserted'
    returndict = runSqlcommand(sql,val,status)  # calling another function to execute the sql commands
    return returndict

# FUCTION TO DELETE THE USER
def deleteUser(inputData):
    sql = "delete from customerdata where custnumber like %s"
    val = (inputData['custid'],)
    status = 'Deleted'
    returndict = runSqlcommand(sql,val,status)  # calling another function to execute the sql commands
    return returndict


# FUNCTION TO FETCH THE USER DETAILS
def getUser(inputData):
    cursor,db,constatus = connecttodb()
    cursor = db.cursor(dictionary=True)
    sql = "select * from customerdata"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows[0]
    '''
    sql = "select * from customerdata where custnumber = %s"
    val = (inputData['custid'],)
    cursor.execute(sql,val)
    myresults = cursor.fetchall()
    print(type(myresults))
    return myresults[0]
    '''

if __name__ == "__main__":
    inputData = {}
    inputData['custid'] = 1
    mydict = getUser(inputData)
    print(mydict)
