import cv2

def binary(filename):
	with open(filename,'rb') as file:
		binary_data = file.read()
		return binary_data

b = binary("/home/faizan/Documents/person_detection/full_images/full_1.jpg")
print(b)
