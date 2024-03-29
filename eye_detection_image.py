import cv2
import numpy as numpy

img=cv2.imread("D:\opencv_udemy/07_eye_detection\eye.png")
eye_cascade=cv2.CascadeClassifier("D:\opencv_udemy/07_eye_detection\eye.xml")
face_cascade=cv2.CascadeClassifier("D:\opencv_udemy/07_eye_detection/frontalface.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

img2= img[y:y+h,x:x+w]
gray2=gray[y:y+h,x:x+w]

eyes=eye_cascade.detectMultiScale(gray2,1.3,5)

for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()