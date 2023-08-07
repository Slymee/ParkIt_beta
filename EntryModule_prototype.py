from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
import keras

import os
import time
from datetime import datetime

from plate_extraction import detectPlate
from character_segment import charSegment
from plate_contours_detect import detectContours
from results import displayResult
from db_operations import vehicleEntry , vehicleExit





#kinter GUI window
window = tk.Tk()
window.title("Image Display")

#operate on image filepath 
def entryDetectionModule(filePath):
    cvImage=cv.imread(filePath)

    vehicleImage, licensePlate = detectPlate(cvImage)
    dimentions, imageDilate = charSegment(licensePlate)
    


    
    #diplay image with bounding box
    cv.imshow("Vehicle Image", vehicleImage)
    cv.imshow("Number Plate", licensePlate)
    cv.imshow("Dilated Plate", imageDilate)

    #display result
    # displayOCR_Result(imageDilate)
 
    cv.waitKey(0)
    cv.destroyAllWindows()

    charList = detectContours(dimentions, imageDilate)

    # #load up character recognition model
    model=keras.models.load_model('model.h5')
    plateValue=displayResult(model, charList)
    # print(plateValue)
    vehicleEntry(plateValue, datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M"))







#operate on image filepath 
def exitDetectionModule(filePath):
    cvImage=cv.imread(filePath)

    vehicleImage, licensePlate = detectPlate(cvImage)
    dimentions, imageDilate = charSegment(licensePlate)
    


    
    #diplay image with bounding box
    cv.imshow("Vehicle Image", vehicleImage)
    cv.imshow("Number Plate", licensePlate)
    cv.imshow("Dilated Plate", imageDilate)

    #display result
    # displayOCR_Result(imageDilate)
 
    cv.waitKey(0)
    cv.destroyAllWindows()

    charList = detectContours(dimentions, imageDilate)

    # #load up character recognition model
    model=keras.models.load_model('model.h5')
    plateValue=displayResult(model, charList)
    # print(plateValue)
    
    vehicleExit(plateValue, datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M"))




#displaying image method
def entryDisplayImage():
    
    #getting image path
    filePath = None
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])

    if filePath:
        #open image
        image = Image.open(filePath)
        #resize image
        image.thumbnail((800,600))

        tkImage=ImageTk.PhotoImage(image)

        #image pass label
        mainImageLabel.config(image=tkImage)
        mainImageLabel.image=tkImage

        

    elif filePath==None:
        print("No image selected")
        exit()
    entryDetectionModule(filePath)
    


#displaying image method exit
def exitDisplayImage():
    
    #getting image path
    filePath = None
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])

    if filePath:
        #open image
        image = Image.open(filePath)
        #thumbnail size
        image.thumbnail((800,600))

        tkImage=ImageTk.PhotoImage(image)

        #image pass label
        mainImageLabel.config(image=tkImage)
        mainImageLabel.image=tkImage

        

    elif filePath==None:
        print("No image selected")
        exit()
    exitDetectionModule(filePath)

    


def closeGUI():
    window.destroy()



#display main image label
mainImageLabel = tk.Label(window)
mainImageLabel.pack()

window.attributes('-fullscreen', True)

#create buttons
selectButton = tk.Button(window, text="Entry Vehicle", command=entryDisplayImage)
selectButton.pack(pady=10)

exitButton = tk.Button(window, text="Exit Vehicle", command=exitDisplayImage)
exitButton.pack(pady=10)

closeButton = tk.Button(window, text="Exit Window", command=closeGUI)
closeButton.pack(pady=10)

window.mainloop()

