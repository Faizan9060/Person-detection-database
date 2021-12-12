import cv2
import numpy as np
from csv import writer
import datetime
import mysql.connector
import time

db = mysql.connector.connect(host="localhost",user="root",password="password",database="person_detection")

cursor = db.cursor()

insert = "INSERT INTO people (image,date,time) VALUES (%s,%s,%s)"

v=cv2.VideoCapture(0)


def binary_data(filename):
    with open(filename,'rb') as file:
        binarydata = file.read()
        return binarydata



classes = None
with open('/home/faizan/Documents/person_detection/coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

counter = 0
while True:

    check,image = v.read()
    
    Width = image.shape[1]
    Height = image.shape[0]
    # print(check)
    #print(frame)
    # read pre-trained model and config file
    net = cv2.dnn.readNet('/home/faizan/Documents/person_detection/yolov3.weights', '/home/faizan/Documents/person_detection/yolov3.cfg')

    # create input blob 
    # set input blob for the network
    net.setInput(cv2.dnn.blobFromImage(image, 0.00392, (416,416), (0,0,0), True, crop=True))

    # run inference through the network
    # and gather predictions from output layers

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    outs = net.forward(output_layers)


    class_ids = []
    confidences = []
    boxes = []

    #create bounding box 
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.1:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])


    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)


    
    #check if is people detection
    for i in indices:
        i = i[0]
        
        
        box = boxes[i]
        if class_ids[i]==0:
            counter  = counter +1
            label = str(classes[class_id]) 
            # cv2.imwrite("/home/faizan/Documents/person_detection/crop.png",img)
            rec =cv2.rectangle(image, (round(box[0]),round(box[1])), (round(box[0]+box[2]),round(box[1]+box[3])), (255, 0, 0), 2)
            cv2.putText(image, label, (round(box[0])-10,round(box[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            x = round(box[0])
            w = round(box[2])
            h = round(box[3])
            y = round(box[1])
            
            filename = "full_" + str(counter) + ".jpg"
            location= "/home/faizan/Documents/person_detection/full_images/" + filename
            cv2.imwrite(location,rec)
            

            #for binary image 
            binary_image = binary_data(location)

            # for current date
            d =datetime.datetime.now()
            date = d.strftime("%d-%m-%Y")
            print(date)

            #for current time
            t= time.localtime()
            ct = time.strftime("%H:%M:%S",t)
            print(ct)
             
            # data = [location2,date,ct]
            data = (binary_image,date,ct)
            cursor.execute(insert,data)

            db.commit()
            
    cv2.imshow("video",image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

v.release()

cv2.destroyAllWindows()

