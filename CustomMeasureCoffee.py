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
    blurred = cv2.GaussianBlur(gray, (1,1), 1)
    wide = cv2.Canny(blurred, 10, 50)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)
    # show the images
    return wide

def houghlines(im,x,y,w,h):
    ypos = (h*.25)
    end_ypos = (h*.60)
    
    lineFound = False
    hitList = []
    while (not lineFound and not ypos > end_ypos):
        topVal = (im[ypos, w/2])[2] # + (im[ypos, w/2])[2] + (im[ypos, w/2])[1]
        botVal = (im[ypos + (h * .1), w/2])[2] #+ (im[ypos + (h * .15), w/2])[2] + (im[ypos + (h * .15), w/2])[1]
        if(botVal > 0 and (abs(int(botVal) - int(topVal))/float(botVal)) > .5):
            hitList.append(ypos)
            print("appending!")
        ypos += 5
    median = 0
    if(len(hitList) > 3):
        median = hitList[len(hitList)/2]
    else:
        return -1
    print (hitList)
    print("x: {}, y: {}, h: {}, w: {}, median: {}".format(x,y,h,w, median))
    return (abs(h - median)/float(h)) * 100
    '''
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
    votes = 0
    while True:
        cv2.line(im,(horizontal[i][0],horizontal[i][1]),(horizontal[i][2],horizontal[i][3]),(200,0,0),2)
       
        average = (horizontal[i][1]+horizontal[i][3])/2.0
        percent = average/h
        actual = 100-(percent*100)
        if actual > 80:
            i += 1
            print(actual)
        elif actual < 25:
            print(actual)
            votes +=1
            i +=1
        elif actual <30:
            print("the coffee pot is getting low " + str(actual) + "% full!")
            return votes,actual
        else:
            print("the coffee pot is " + str(actual) + "% full!")
            return votes,actual
            '''
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
    face_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/coffeePot.xml')
    eye_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/liquid.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 500, minSize=(80,100))
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, minSize=(70,50))
        return houghlines(roi_color,x,y,w,h)

while True:
    percent = 0
    tries = 5
    successes = 0
    votes = 0
    t = Twitter()
    for i in range(tries):
        numPercent =detect()
        if(numPercent > 0 and numPercent < 101):
            percent += numPercent
            successes += 1
    if(successes>0):
        percent /= tries
    else:
        percent = 0
    print("********* UPDATING **********")
    if percent < 10:
        onlineCoffee.updateCoffeeSite("We've most likely run out of coffee... I blame Kevin")
        t.tweet("We've mos run out of coffee.. stufff")
    else:
        onlineCoffee.updateCoffeeSite("There's plenty of coffee! It's " + str(int(percent)) + "% full!")
        t.tweet("There's plenty of coffee! It's maybe asdkfljas " + str(int(percent)) + "% full!")
    print(percent)
        
