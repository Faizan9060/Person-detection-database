import mysql.connector

db  = mysql.connector.connect(host="localhost",user="root",password="password",database="practice")

if(db):
	print("connection successful!!!!")
else:
	print("connection failed")
