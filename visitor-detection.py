import cv2,time
from datetime import datetime

f_f = None
start = time.time()
visitors = 0
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video =cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    img = frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if f_f is None:
        f_f = gray
        continue
    faces = face_cascade.detectMultiScale(gray,1.05,5)
    for x,y,w,h in faces:
        frame=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
    done = time.time()
    elapsed = done - start
    print(elapsed%10)
    if int(elapsed%10) == 0:
        try:
            visitors = faces.shape[0]
            if visitors>=1:
                cv2.imshow('visitors',img)

        except AttributeError:
            continue


    key = cv2.waitKey(1)
    if key ==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
