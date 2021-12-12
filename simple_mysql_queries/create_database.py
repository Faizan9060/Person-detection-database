import mysql.connector

database = mysql.connector.connect(host="localhost",user="root",password="password")

cursor = database.cursor()

#cursor.execute("CREATE DATABASE practice")
cursor.execute("SHOW DATABASES")

for x in cursor:
	print(x)

