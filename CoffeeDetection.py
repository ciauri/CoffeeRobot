import io
import picamera
import numpy 
import cv2
'''
stream = io.BytesIO()

    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
    camera.resolution = (350, 262)
    camera.capture(stream, format='jpeg')

buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
img = cv2.imdecode(buff, 1)
'''
img = cv2.imread('coffee.jpg')
face_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/coffeePot.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/liquid.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("hello")
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
