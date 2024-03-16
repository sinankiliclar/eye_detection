import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("D:\opencv_udemy/07_eye_detection/frontalface.xml")
eye_cascade=cv2.CascadeClassifier("D:\opencv_udemy/07_eye_detection\eye.xml")


while True:
   while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(480,360))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    roi_frame=frame[y:y+h,x:x+w]
    roi_gray=gray[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray)
    
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    cv2.imshow("Video",frame)

    if cv2.waitKey(5) & 0XFF==ord("q"):
        breakq

cap.release()
cv2.destroyAllWindows()