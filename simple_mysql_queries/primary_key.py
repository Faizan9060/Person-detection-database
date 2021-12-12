import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="password",database="person_detection") 

cursor = db.cursor()

cursor.execute("ALTER TABLE numberplate ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
