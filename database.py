import mysql.connector
from mysql.connector import Error

def Createdatabase():
    try:
        connection=mysql.connector.connect(host='localhost',user='root',password='')
        cursor=connection.cursor()
        cursor.execute('Create database krishna') 
        connection.commit()
        print('Database krishna created successfully')
    except mysql.connector.Error as error:
        print('Failed to create database:{}'.format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
Createdatabase()
