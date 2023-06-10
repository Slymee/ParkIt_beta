import cv2 as cv

def detectPlate(cvImage):
    
    vehicleImage=cvImage.copy()

    #load the detector
    plateCascade = cv.CascadeClassifier("license_plate_model.xml")

    #detect and return plate cordinates
    plateCords =plateCascade.detectMultiScale(cvImage, scaleFactor = 1.3, minNeighbors = 7)


    for (x,y,w,h) in plateCords:
        a,b = (int(0.02*cvImage.shape[0]), int(0.025*cvImage.shape[1])) #parameter tuning

        licensePlate = vehicleImage[y+a:y+h-a, x+b:x+w-b, :]

        #representing the detected contours by drawing rectangles around the edges.
        cv.rectangle(vehicleImage, (x,y), (x+w, y+h), (51,51,255), 3)

    #return processed image
    return vehicleImage, licensePlate