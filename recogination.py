import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)# to take the host laptop video 

if not cap.isOpened():
    raise ValueError(f"video capture is not opened")
    exit()
while True:
    ret,frame = cap.read()

    if not ret:
        print("frames are not comming")
        continue
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('face detection',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

