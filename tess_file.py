import cv2 as cv
import os 
import pytesseract


#Execute OCR Engine
os.environ['TESSDATA_PREFIX'] = os.path.normpath(
    r'D:/Program Files/Tesseract-OCR/tessdata/')
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
myConfig = r"--psm 6 -- oem 3"


def displayOCR_Result(imageDilate):
    ocrResult = pytesseract.image_to_string(imageDilate, config=myConfig)
    print(ocrResult)
