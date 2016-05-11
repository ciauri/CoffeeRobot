# CoffeeRobot
RaspberryPi CV module that tracks the state of a coffee pot

## Prerequisites

- [Setup OpenCV 3 for Python](http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/)
- [Setup Numpy on Raspberry Pi](http://wyolum.com/numpyscipymatplotlib-on-raspberry-pi/)
- ...other things (setup email/notification service, camera, wifi, etc...)

## Training Process
### Cascade Classifier
- Provided 500 positive images and 250 negative images to classifier trainer
- Trained 2 classifiers: One to detect coffee maker, and one to detect coffee pot

## Horizontal Line Detection

- Scanned from the top of the detected coffee pot to find change from light to dark RGB values
- Draw line where significant change occurs
- Divide distance from detected y position by coffee pot total height to estimate percent full

## Notification
- Tweeted @raspicoffeebot coffee status
