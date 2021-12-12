import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="password",database="practice") 

cursor = db.cursor()

cmd ="SELECT * FROM customers Where name ='rani'"

cursor.execute(cmd)

result = cursor.fetchall()
print("specific")
for x in result:
    print(x)

cmd1 = "SELECT * FROM customers Where name ='an'"
cursor.execute(cmd1)
res = cursor.fetchall()
print("wild card characters")
for y in res:
    print(y)
