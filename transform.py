import numpy as np
import argparse
import glob
import cv2
import io
import picamera
from Twitter import Twitter
import onlineCoffee
import time
def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged
def r(image):
    #image = cv2.imread('2.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (101,101), 1)
    wide = cv2.Canny(blurred, 20,50)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)
    # show the images
    cv2.imshow("Original", image)
    cv2.imshow("Edges", np.hstack([wide, tight, auto]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return wide

def houghlines(im,h):
    #im = cv2.imread('2.jpg')
    #ret,gray = cv2.threshold(im,40,255,cv2.THRESH_TOZERO_INV)
    #gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(gray,10,200)
    def getKey(item):
        return abs(item[1]-item[3])
    edges = r(im)
    lines = cv2.HoughLines(edges,20,np.pi/190,100)
    horizontal = []
    for line in lines:
        for rho,theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))   # Here i have used int() instead of rounding the decimal value, so 3.8 --> 3
            y1 = int(y0 + 1000*(a))    # But if you want to round the number, then use np.around() function, then 3.8 --> 4.0
            x2 = int(x0 - 1000*(-b))   # But we need integers, so use int() function after that, ie int(np.around(x))
            y2 = int(y0 - 1000*(a))
            #cv2.line(im,(x1,y1),(x2,y2),(0,255,0),2)
            #print(str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
            horizontal.append((x1,y1,x2,y2))
            
            #cv2.imshow('houghlines',im)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
    horizontal = sorted(horizontal,key=getKey)
    i = 0
    while True:
        cv2.line(im,(horizontal[i][0],horizontal[i][1]),(horizontal[i][2],horizontal[i][3]),(200,0,0),2)
        cv2.imshow('houghlines',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("line.jpg",im)
        average = (horizontal[i][1]+horizontal[i][3])/2.0
        percent = average/h
        actual = 100-(percent*100)
        if actual > 80 or actual < 20:
            i += 1
            print(actual)
        elif actual <30:
            print("the coffee pot is getting low " + str(actual) + "% full!")
            
        else:
            print("the coffee pot is " + str(actual) + "% full!")
            onlineCoffee.updateCoffeeSite("The coffee pot is " + str(int(actual)) + "% full!")
            break
def detect():
    stream = io.BytesIO()

        #Get the picture (low resolution, so it should be quite fast)
        #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (700, 525)
        camera.capture(stream, format='jpeg')

    buff = np.fromstring(stream.getvalue(), dtype=np.uint8)

    #Now creates an OpenCV image
    img = cv2.imdecode(buff, 1)


    #img = cv2.imread('coffee.jpg')
    face_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/liquid.xml')
    eye_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/liquid.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 500, minSize=(80,100))
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, minSize=(70,50))
        houghlines(roi_color,h)
        print(str(x) +" "+str(y)+" "+str(w)+" "+str(h))
        '''for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            roi_liquid_color = roi_color[ey:ey+eh, ex:ex+ew]
            cv2.imshow('img',roi_liquid_color) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imshow('img',img) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            houghlines(roi_liquid_color)
            '''
    cv2.imshow('img',img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    detect()
