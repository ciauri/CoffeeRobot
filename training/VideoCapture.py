
# See http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2

# open the default camera
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    
    # Quits the program if waited 1 ms and if you press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Save the image
    cv2.imwrite();

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
