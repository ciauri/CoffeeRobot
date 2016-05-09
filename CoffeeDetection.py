import io
import picamera
import time
import numpy 
import cv2
import onlineCoffee
import Twitter

def detectCoffee():
    stream = io.BytesIO()
    
        #Get the picture (low resolution, so it should be quite fast)
        #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        # camera.start_preview()
        camera.resolution = (700, 525)
        camera.awb_mode = "auto"
        camera.iso = 800
        camera.capture(stream, format='jpeg')
    
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
    
    #Now creates an OpenCV image
    img = cv2.imdecode(buff, 1)
    
    #img = cv2.imread('coffee.jpg')
    face_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/coffeePot.xml')
    eye_cascade = cv2.CascadeClassifier('/home/pi/Documents/OpenCV_Projects/XML_Files/liquid.xml')
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb_val = 0
    faces = face_cascade.detectMultiScale(gray, 1.2, 200, minSize=(30, 50))
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # minPotWidth = w*0.8
        # minPotHeight = minPotWidth
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, minSize=(w, minPotHeight))
        rgb_val = 0
        numPots = 0
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            roi_liquid_color = img[ey:ey+eh, ex:ex+ew]
            mean = cv2.mean(roi_liquid_color)
            rgb_val += mean[0] +mean[1] +mean[2]
            numPots += 1
        if(numPots == 0):
            numPots += 1
        rgb_val /= numPots
        print(rgb_val)
    return rgb_val
    
def getAVGcoffee(numPics):
    if(numPics > 0):
        avg_rgb_val = 0
        good_vals = 0
        for i in range(numPics):
            next_rgb_val = 0
            next_rgb_val = detectCoffee()
            if(next_rgb_val > 0):
                avg_rgb_val += next_rgb_val
                good_vals += 1
            time.sleep(1)
        avg_rgb_val /= good_vals
        return avg_rgb_val
    
#Main Prog Loop
loops = 0
constant_empty_rgb_val = 0
while(True):
    if(loops < 2):
        if(loops == 0):
            print("Calibrating, please ensure pot is EMPTY,")
            raw_input("Press ENTER when pot is EMPTY...")
            constant_empty_rgb_val += getAVGcoffee(4)
        else:
            constant_empty_rgb_val += getAVGcoffee(4)
            constant_empty_rgb_val /= 2
    else:
        print("Checking for coffee... ")
        currentCoffeeLevel = getAVGcoffee(4)
        percentDiff = (abs(constant_empty_rgb_val - currentCoffeeLevel)/float(constant_empty_rgb_val))*100.0
        print("RGB val of pot is: " + str(currentCoffeeLevel))
        print("There is approximately %d% coffee in the pot {}".format(percentDiff))
        time.sleep(3)
    loops += 1
