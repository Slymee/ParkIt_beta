from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
import keras
import pytesseract
from tess_file import displayOCR_Result
import os

from plate_extraction import detectPlate
from character_segment import charSegment
from plate_contours_detect import detectContours
from results import displayResult


#Execute OCR Engine
# os.environ['TESSDATA_PREFIX'] = os.path.normpath(
#     r'D:/Program Files/Tesseract-OCR/tessdata/')
# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
# myConfig = r"--psm 6 -- oem 3"




#kinter GUI window
window = tk.Tk()
window.title("Image Display")

#operate on image filepath 
def detectionModule(filePath):
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


    print(charList)

    # #load up character recognition model
    model=keras.models.load_model('model.h5')
    print(displayResult(model, charList))






#displaying image method
def displayImage():
    
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
    
    detectionModule(filePath)
    




#display main image label
mainImageLabel = tk.Label(window)
mainImageLabel.pack()

#create buttons
selectButton = tk.Button(window, text="Select Image", command=displayImage)
selectButton.pack(pady=10)


window.mainloop()

