from dbfunctions import *
from flask import Flask, request, session, render_template
app = Flask(__name__)
app.secret_key = 'testing@123'

@app.route('/')
def callingMainHtml():
    return render_template("main.html")

@app.route('/createUser.html')
def createuser():
    return render_template('createUser.html')

@app.route('/deleteuser.html')
def deleteuser():
    # deleteUser(inputData)
    return render_template('deleteuser.html')

@app.route('/getuser.html')
def getuser():
    return render_template('getuser.html')

# FUCTIONS TO CALL FROM THE FORM(JAVASCRIPT)
@app.route('/createuserdata', methods=['GET','POST'])
def createuserdata():
    custdata = request.form.to_dict(flat=True)
    result = createUpdateUser(custdata)
    return render_template("showdata.html",result = result)

@app.route('/deleteuserdata', methods=['GET','POST'])
def deleteuserdata():
    custID = request.form
    result = deleteUser(custID)
    print(result)
    return render_template("showdata.html",result = result)

@app.route('/getuserdata', methods=['GET','POST'])
def getuserdata():
    custID = request.form
    result = getUser(custID)
    return render_template("showdata.html",result = result)

if __name__ == '__main__':
   app.run('0.0.0.0',5000,debug = True)
