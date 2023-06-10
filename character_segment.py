import cv2 as cv


#find characters in result image

def charSegment(plateImage):
    #preprocess detected license plate
    licensePlate = cv.resize(plateImage,(333,75))
    #convert to binary image
    _, plateBinary=cv.threshold(cv.cvtColor(licensePlate,cv.COLOR_BGR2GRAY),200,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #plate dilation
    plateDilate = cv.dilate(cv.erode(plateBinary,(3,3)), (3,3))

    LP_WIDTH = plateDilate.shape[0]
    LP_HEIGHT = plateDilate.shape[1]

    #emphasizing white borders
    plateDilate[0:3,:] = 255
    plateDilate[:,0:3] = 255
    plateDilate[72:75,:] = 255
    plateDilate[:,330:333] = 255

    #estimating character countour sizes of the detected license plate
    dimentions = [LP_WIDTH/6, LP_WIDTH/2, LP_HEIGHT/10, 2*LP_HEIGHT/3]

    return dimentions, plateDilate