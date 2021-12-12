import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="password",database="practice") 

cursor = db.cursor()


cursor.execute("SELECT * FROM customers")

result = cursor.fetchall()
print("all records")
for x in result:
    
    print(x)

cursor.execute("SELECT id,name FROM customers")
res = cursor.fetchall()
print("selected columns")
for u in res:
    print(u) 

cursor.execute("SELECT id,name FROM customers")
r = cursor.fetchone()
print("fetching one row")
print(r)


