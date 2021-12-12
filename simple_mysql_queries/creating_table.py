import mysql.connector

mysql = mysql.connector.connect(host="localhost",user = "root",password= "password",database = "person_detection")

cursor=mysql.cursor()

cursor.execute("CREATE TABLE people (image LONGBLOB,date VARCHAR(255),time VARCHAR(255))")
# cursor.execute("SHOW TABLES")

# for x in cursor:
# 	print(x)
