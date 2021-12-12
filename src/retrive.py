import mysql.connector


#function to convert binary image to proper format
def write_file(data,filename):
	with open(filename,'wb') as file:
		file.write(data)

#function to read blob data
def readblob(id,image_path,cursor):
	
	
	query = "SELECT * FROM people WHERE id=%s"
	values = (id,)
	cursor.execute(query,values)
	record = cursor.fetchall()
	for row in record:
		binary_image = row[0]
		print("date = ",row[1])
		print("time = ",row[2])
		print("id = ",row[3])
		
		write_file(binary_image,image_path)

connection = mysql.connector.connect(host='localhost',user='root',password='password',database='person_detection')

cursor=connection.cursor()

count_query = "SELECT * FROM people"
cursor.execute(count_query)
count = cursor.fetchall()

for key in range(0,len(count)+1):
	image_name = "person_" + str(key) + ".jpg"
	image_path = "/home/faizan/Documents/person_detection/retrived_images/" + image_name
	readblob(key,image_path,cursor)
	

