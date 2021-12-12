import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="password",database="practice") 

cursor = db.cursor()

insert = "INSERT INTO customers (name,time) VALUES (%s,%s)"

value = [("x","12.35"),("y","2.30"),("z","3.32")]

cursor.executemany(insert,value)

db.commit()

print(cursor.rowcount," inserted")
