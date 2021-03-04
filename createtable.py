import mysql.connector
from mysql.connector import Error
def CreateTable():
    try:
        connection=mysql.connector.connect(host='localhost',database='charan',user='root',password='')
        cursor=connection.cursor()
        cursor.execute('create table emp(empid int primary key,ename varchar(30), sal int)')
        connection.commit()
        print('Table emp created successfully')
    except mysql.connector.Error as error:
        print('Failed to create table :{}'.format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print('MySQL connection is closed')                                                                                      

def InsertRow(query):
    try:
        connection=mysql.connector.connect(host='localhost',database='charan',user='root',password='')
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Row Inserted successfully')
    except mysql.connector.Error as error:
        print('Failed to insert record from table :{}'.format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
def DeleteRow(query):
    try:
        connection=mysql.connector.connect(host='localhost',database='charan',user='root',password='')
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print('Row  Deleted successfully')
    except mysql.connector.Error as error:
        print('Failed to delete record from table :{}'.format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
            


CreateTable()
InsertRow('insert into emp values(2,"srikanth",6000)')
InsertRow('insert into emp values(3,"rahul",7000)')
InsertRow('insert into emp values(4,"ramesh",8000)')
InsertRow('insert into emp values(5,"rajesh",5000)')
InsertRow('insert into emp values(6,"teja",7000)')
InsertRow('insert into emp values(7,"chiru",9000)')
InsertRow('insert into emp values(8,"ravi",6000)')
InsertRow('insert into emp values(9,"saicharan",7000)')
InsertRow('insert into emp values(10,"saikumar",4000)')
InsertRow('insert into emp values(11,"ruthwik",7000)')
InsertRow('insert into emp values(12,"pochireddy",9000)')
InsertRow('insert into emp values(13,"nikhil",3500)')
InsertRow('insert into emp values(14,"arvind",7000)')
InsertRow('insert into emp values(15,"krishna",6000)')
#DeleteRow('delete from emp where empid=2')
