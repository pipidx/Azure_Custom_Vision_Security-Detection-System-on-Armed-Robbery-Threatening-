from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from collections import namedtuple
import time
import cv2
import numpy as np

import azure_blob 
import utility
import credential



#reading testing video
cap = cv2.VideoCapture("new1.mp4")

# img_path = "/home/fidx/Documents/I_Testing/Azure/cognitive-services-quickstart-code/python/CustomVision/ObjectDetection/Azure_Custom_Vision_Security-Detection-System-on-Armed-Robbery-Threatening/img_0.jpg"
i = 0
count = 0

# path = '/home/fidx/Documents/I_Testing/Azure/cognitive-services-quickstart-code/python/CustomVision/ObjectDetection/Azure_Custom_Vision/images/'
# azqqq
predictor, project_id, iteration_name  = credential.predictor()

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #write frame as image for processing 
    cv2.imwrite("img_"+str(i)+".jpg",frame)
    
    #convert image to (width, height) to get fit when drawing bounding box
    img = cv2.resize(frame, (290, 290), interpolation = cv2.INTER_LINEAR)
    
    print("\nframe:", count)
    with open("img_"+str(i)+".jpg", mode="rb") as test_data:
        results = predictor.detect_image_with_no_store(project_id = project_id, published_name = iteration_name, image_data=test_data)

    gun_list = []
    person_list = []

    for prediction in results.predictions:
        
        if prediction.tag_name == "person":
            threshold = 65
        else:
            threshold = 15

        if prediction.probability * 100 > threshold :

            print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))

            x1, y1, x2, y2 = utility.find_actual_bbox_value(prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height, img)
            label = prediction.tag_name + ":  {0:.2f}%".format(prediction.probability * 100)

            if prediction.tag_name == "gun":
                gun_list.append([x1, y1, x2, y2])
            else:
                person_list.append([x1, y1, x2, y2])
    
    strong_gun = utility.adaptive_gun_detection(gun_list, person_list)
    
    if len(strong_gun) > 0 : 
        for i in range(len(strong_gun)):
            center = utility.find_center(strong_gun[i][0], strong_gun[i][1], strong_gun[i][2], strong_gun[i][3])
            cv2.circle(img,(int(center.x), int(center.y)), 1, (255,0,255), -1)
            cv2.rectangle(img, (strong_gun[i][0], strong_gun[i][1]), (strong_gun[i][2], strong_gun[i][3]),(0,0,255),2)
            cv2.putText(img, "Gun",(strong_gun[i][0], strong_gun[i][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.3,(255,128,0),1, cv2.LINE_AA)


    if len(person_list) > 0: 
        for i in range(len(person_list)):
            cv2.rectangle(img, (person_list[i][0], person_list[i][1]), (person_list[i][2], person_list[i][3]),(0,255,0),1)
            cv2.putText(img, "Person",(person_list[i][0], person_list[i][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.3,(255,128,0),1, cv2.LINE_AA)
  
    count += 1
    print ("gun_list", gun_list)
    print ("person_list", person_list)
    #"""HH """

    cv2.putText(img,"Threathening Level: ",(5,10), cv2.FONT_HERSHEY_SIMPLEX, 0.3,(255,0,255),1,cv2.LINE_AA)
    cv2.imshow("frame", img)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
    elif cv2.waitKey(5) & 0xFF == ord(" "):
        cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
