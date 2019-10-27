
# source: https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57

import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('river.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if currentFrame % 20 == 0:
    # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()