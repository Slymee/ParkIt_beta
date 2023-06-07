import cv2 as cv
import numpy as np
import pytesseract
import os


os.environ['TESSDATA_PREFIX'] = os.path.normpath(
    r'D:/Program Files (x86)/Tesseract-OCR/tessdata/')
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
myConfig = r"--psm 6 -- oem 3"

# define height and width for visual frame
frameWidth = 800  # Frame Width
frameHeight = 600   # Frame Height

# load up the trained model
plateCascade = cv.CascadeClassifier("license_plate_model.xml")

minArea = 500

# initialize properties for the computer vision
vid = cv.VideoCapture(0)
vid.set(3, frameWidth)
vid.set(4, frameHeight)
vid.set(10, 150)

# Initialize Computer Vision
while True:
    success, img = vid.read()

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    imgRoi = None

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(img, "NumberPlate", (x, y-5),
                       cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            plateRoi = img[y:y+h, x:x+w]

            # Image Processing
            imgRoiGray = cv.cvtColor(plateRoi, cv.COLOR_BGR2GRAY)
            # Image Brightning
            imgRoiGray = np.clip(imgRoiGray * 0.8, 0, 255).astype(np.uint8)
            # Image Saturation
            imgRoiGray[:, 1] = np.clip(
                imgRoiGray[:, 1]*0.7, 0, 255).astype(np.uint8)
            cv.imshow("License Plate", imgRoiGray)

    cv.imshow("Result", img)

    try:
        if cv.waitKey(1) & 0xFF == ord('s'):

            # Image Processing
            imgRoiGray = cv.cvtColor(plateRoi, cv.COLOR_BGR2GRAY)
            # Image Brightning
            imgRoiGray = np.clip(imgRoiGray * 1.2, 0, 255).astype(np.uint8)
            # Image Saturation
            imgRoiGray[:, 1] = np.clip(
                imgRoiGray[:, 1]*0.7, 0, 255).astype(np.uint8)

            # Perform OCR
            ocrResult = pytesseract.image_to_string(
                imgRoiGray, config=myConfig)
            print(ocrResult)



    except Exception as error:
        print(f"--[ Pytesseract INITIALIZATION ERROR ]--> {error}")
        exit()

    import time
    time.sleep(0.05)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
