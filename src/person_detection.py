import cv2
import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
#from PIL import Image
from csv import writer
import datetime

import time


#path = "/home/faizan/dog.mp4"
# image = plt.imread('/home/faizan/people.jpeg')
v=cv2.VideoCapture(0)


classes = None
with open('/home/faizan/Documents/person_detection/coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]



'''out = cv2.VideoWriter(
    '/home/faizan/Documents/person_detection/dog.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video_writer = cv2.VideoWriter("/home/faizan/Documents/person_detection/output.mp4", fourcc, 20, (680, 480))
w1 = v.get(cv2.CAP_PROP_FRAME_WIDTH)
h1 = v.get(cv2.CAP_PROP_FRAME_HEIGHT)
video_writer = cv2.VideoWriter('/home/faizan/Documents/person_detection/output2.avi',fourcc, 15.0, (int(w1),int(h1)))
a=1
image = cv2.imread("/home/faizan/Documents/person_detection/images.jpeg")'''
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
    # y=round(boxes[1])
    # x=round(boxes[0])
    # w=round(boxes[2])
    # h=round(boxes[3])


    
    #check if is people detection
    for i in indices:
        i = i[0]
        
        
        box = boxes[i]
        if class_ids[i]==0:
            counter  = counter +1
            label = str(classes[class_id]) 
            # img = 
            # cv2.imwrite("/home/faizan/Documents/person_detection/crop.png",img)
            rec =cv2.rectangle(image, (round(box[0]),round(box[1])), (round(box[0]+box[2]),round(box[1]+box[3])), (255, 0, 0), 2)
            cv2.putText(image, label, (round(box[0])-10,round(box[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            x= round(box[0])
            w= round(box[2])
            h = round(box[3])
            y = round(box[1])
            
            # new_img=rec[y:y+h , x:x+w]
            # filename1 = "crop_" + str(counter) + ".jpg"
            filename2 = "full_" + str(counter) + ".jpg"
            # print(filename1)
            # location = "/home/faizan/Documents/person_detection/cropped_images/" + filename1
            location2 = "/home/faizan/Documents/person_detection/full_images/" + filename2
            # cv2.imwrite(location,new_img)
            cv2.imwrite(location2,rec)
            
            d =datetime.datetime.now()
            date = d.strftime("%d-%m-%Y")
            print(date)

            t= time.localtime()
            ct = time.strftime("%H:%M:%S",t)
            print(ct)

            data = [location2,date,ct]


    
            
            #appending data into csv
            with open('/home/faizan/Documents/person_detection/database2.csv','+a',newline='') as obj:
                csv_writer = writer(obj)
                csv_writer.writerow(data)
		#cropping images
		    
            # try:

            #     crop = image.crop[round(box[0]),round(box[1]),round(box[0]+box[2]),round(box[1]+box[3])]
            #     cv2.imwrite("/home/faizan/Documents/person_detection/test.png",crop)
            # except:
            #     continue
    # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
  # video_writer.write(image)
    
    cv2.imshow("video",image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

v.release()

# and release the output
#video_writer.release()
cv2.destroyAllWindows()
# cv2.waitKey(1)
