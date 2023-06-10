import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
import pytesseract
import operational_methods


os.environ['TESSDATA_PREFIX'] = os.path.normpath(
    r'D:/Program Files (x86)/Tesseract-OCR/tessdata/')
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
myConfig = r"--psm 6 -- oem 3"


#Load up trained Model
plateCascade = cv.CascadeClassifier("license_plate_model.xml")






def OCRresult(file_path):
    print(file_path)


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
    if file_path:
        image = cv.imread(file_path)
        cvImage = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        OCRresult(file_path)
        # display_image(cvImage)



def display_image(cvImage):
    # Get the window size
    window_width = 800
    window_height = 600

    # Resize the image to fit within the window
    image_height, image_width, _ = cvImage.shape
    aspect_ratio = image_width / image_height

    if image_width > window_width or image_height > window_height:
        if aspect_ratio > 1:
            new_width = window_width
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = window_height
            new_width = int(new_height * aspect_ratio)

        cvImage = cv.resize(cvImage, (new_width, new_height))

    # Create a blank canvas with the window size
    canvas = np.zeros((window_height, window_width, 3), dtype=np.uint8)

    # Calculate the position to ceImage.shape[1]) // 2
    x= (window_width - cvImage.shape[1]) // 2
    y = (window_height - cvImage.shape[0]) // 2

    # Paste the resized image onto the canvas
    canvas[y:y + cvImage.shape[0], x:x + cvImage.shape[1]] = cvImage

    cv.waitKey(0)
    cv.destroyAllWindows()

def generate_roi():
    # TODO: Implement ROI generation logic here
    pass

# Create the main window
window = tk.Tk()
window.title("Image Viewer")

# Create buttons
select_button = tk.Button(window, text="Select Image", command=select_image)
select_button.pack(pady=10)



generate_button = tk.Button(window, text="Generate ROI", command=generate_roi)
generate_button.pack(pady=10)

# Start the main event loop
window.mainloop()

