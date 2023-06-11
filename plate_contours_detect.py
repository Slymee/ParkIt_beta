import numpy as np
import cv2 as cv

#match countours to license plate
def detectContours(dimentions, imageDilate):

    #find contours in the image
    cntrs, _ = cv.findContours(imageDilate.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # retrieve potential dimensions
    lowerWidth = dimentions[0]
    upperWidth = dimentions[1]
    lowerHeight = dimentions[2]
    upperHeight = dimentions[3]

    # check largest 5 or  15 contours for license plate or character respectively
    cntrs = sorted(cntrs, key=cv.contourArea, reverse=True)[:15]

    x_cntrList = []
    targetContours = []


    imgRes = []
    for cntr in cntrs :
        #detects contour in binary image and returns the coordinates of rectangle enclosing it
        intX, intY, intWidth, intHeight = cv.boundingRect(cntr)
        
        #checking the dimensions of the contour to filter out the characters by contour's size
        if True:
        # if intWidth > lowerWidth and intWidth < upperWidth and intHeight > lowerHeight and intHeight < upperHeight :
            x_cntrList.append(intX) #stores the x coordinate of the character's contour, to used later for indexing the contours

            charCopy = np.zeros((44,24))
            #extracting each character using the enclosing rectangle's coordinates.
            char = imageDilate[intY:intY+intHeight, intX:intX+intWidth]
            char = cv.resize(char, (20, 40))

            # Make result formatted for classification: invert colors
            char = cv.subtract(255, char)

            # Resize the image to 24x44 with black border
            charCopy[2:42, 2:22] = char
            charCopy[0:2, :] = 0
            charCopy[:, 0:2] = 0
            charCopy[42:44, :] = 0
            charCopy[:, 22:24] = 0

            imgRes.append(charCopy) #List that stores the character's binary image (unsorted)


    #return characters on ascending order with respect to the x-coordinate (most-left character first)
    
    #arbitrary function that stores sorted list of character indeces
    indices = sorted(range(len(x_cntrList)), key=lambda k: x_cntrList[k])
    imgResCopy = []
    for idx in indices:
        imgResCopy.append(imgRes[idx])# stores character images according to their index
    imgRes = np.array(imgResCopy)


    return imgRes

 