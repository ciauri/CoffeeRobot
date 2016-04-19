# Refer to http://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html#gsc.tab=0

# Import is still cv2 when using OpenCV 3.0
import cv2
import numpy as np

imgFile = "coffeePot.jpg"
img = cv2.imread(imgFile, 0)
ret,tresh = cv2.threshold(img,127,255,0)
contours,hiearchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]]

# Gives a dictionary of all moment values calculated
M = cv2.moments(cnt)
print M

# Centroid values
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# Contour area
area = cv2.contourArea(cnt)

# Contour perimeter
perimater = cv2.arcLength(cnt,True)

# Straight Bounding Rectangle (doesn't consider rotation of object, so bounding rectangle won't be minimum)
# (x,y) is the top left coordinate of the rectangle; (w, h) is its width and height
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

# Rotated Rectangle (bounding rectangle is drawn with minimum area, so considers rotation also)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)
