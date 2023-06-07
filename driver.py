import os
import sys
import cv2 as cv
import numpy as np
import pandas as pd
from datetime import datetime
from os import path as directoryPath
import tensorflow as tf

# Dimension Configuration...
frameWidth = 640  # Frame Width
frameHeight = 480   # Frame Height

model = cv.dnn.readNetFromTensorflow('models/license_plate_model_aio.h5')

try:
    # Defining the Camera Capture Object
    camera = cv.VideoCapture(0)
    camera.set(3, frameWidth)
    camera.set(4, frameHeight)
    camera.set(10, 150)
except Exception as error:
    print(f"--[ CAMERA INITIALIZATION ERROR ]--> {error}")
    exit()


while (True):
    try:
        # Capture the camera input Frame by Frame
        ret, frame = camera.read()

        # Display the resulting frame
        cv.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as error:
        print(f"--[ RECOGNITION MODULE ERROR ]--> {error}")
        exit()

# After the loop release the Capture Object
camera.release()

# Destroy all the windows
cv.destroyAllWindows()
