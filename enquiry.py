from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
from mysql.connector import Error
'''
{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements

'''
app = Flask(__name__)

@app.route('/')
def insertform():
   return render_template("user1.html")

@app.route('/insert',methods = ['POST', 'GET'])
def insertuser1():
   if request.method == 'POST':  
      result = request.form
      try:
        connection = mysql.connector.connect(host='localhost',database='pochireddy',user='root',password='')
        sql_select_Query = """insert into enquiry(firstname,lastname,hno,street,city,pin,cell,email,remarks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor = connection.cursor()
        rec =(result['firstname'],result['lastname'],result['hno'],result['street'],result['city'],result['pin'],result['cell'],result['email'],result['remarks'])
        print(rec)
        cursor.execute(sql_select_Query,rec)
        connection.commit()
        return redirect(url_for('listuser1'))
      except Exception as ex:
        print(ex)
        return render_template("user1.html",result =ex)
      finally:
         if (connection.is_connected()):
             connection.close()
             cursor.close()

@app.route('/deluser1/<enquiryid>',methods = ['POST', 'GET'])
def deluser1(enquiryid):
      try:
        connection = mysql.connector.connect(host='localhost',database='pochireddy',user='root',password='')
        sql_select_Query = """delete from enquiry where enquiryid=%s"""
        cursor = connection.cursor()
        #firstname = request.args.get('firstname')
        rec =(enquiryid,)
        cursor.execute(sql_select_Query,rec)
        connection.commit()
        return redirect(url_for('listuser1'))
      except Exception as ex:
        print(ex)
        return render_template("listuser1.html",error =ex)
      finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()


@app.route('/upuser1/<firstname>',methods = ['POST', 'GET'])
def upuser1(firstname):
      try:
        connection = mysql.connector.connect(host='localhost',database='pochireddy',user='root',password='')
        sql_select_Query = """select * from enquiry where enquiryid=%s"""
        cursor = connection.cursor()
        #firstname = request.args.get('firstname')
        rec =(firstname,)
        cursor.execute(sql_select_Query,rec)
        rec1 = cursor.fetchone()
        print(rec1)
        connection.commit()
        return render_template('upuser1.html',user1=rec1)
      except Exception as ex:
        print(ex)
        return render_template("listuser1.html",error =ex)
      finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

@app.route('/updateuser1',methods = ['POST', 'GET'])
def updateuser1():
   try:
      if request.method == 'POST':
         result = request.form
         connection = mysql.connector.connect(host='localhost',database='pochireddy',user='root',password='')
         sql_select_Query = """update enquiry set remarks=%s,email=%s,cell=%s,pin=%s,city=%s,street=%s,hno=%s,lastname=%s,firstname=%s where enquiryid=%s"""
         cursor = connection.cursor()
         rec =(result['remarks'],result['email'],result['cell'],result['pin'],result['city'],result['street'],result['hno'],result['lastname'],result['firstname'],result['enquiryid'])
         cursor.execute(sql_select_Query,rec)
         connection.commit()
         return redirect(url_for('listuser1'))
   except Exception as ex:
      print(ex)
      return render_template("listuser1.html",error=ex)
   finally:
      if (connection.is_connected()):
          connection.close()
          cursor.close()
            
            
@app.route('/listuser1',methods = ['POST', 'GET'])
def listuser1():
      try:
        connection = mysql.connector.connect(host='localhost',database='pochireddy',user='root',password='')
        sql_select_Query = "select * from enquiry"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        type(records)
        connection.commit()
        return render_template("listuser1.html",result =records)
      except Exception as ex:
        print(ex)
        return render_template("listuser1.html",error =ex)
      finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            

if __name__ == '__main__':
   app.run(debug = True)

