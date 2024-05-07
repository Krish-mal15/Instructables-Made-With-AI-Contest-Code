import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy
import math
import pyfirmata2
from time import sleep



img = cv2.VideoCapture(1)
# 640 x 480

colorFinder = ColorFinder(False)

openAngle = 100
closeAngle = 180



hsvVals = {"hmin": 0, "smin": 0, "vmin": 242, "hmax": 179, "smax": 255, "vmax": 255}


while True:

    ret, frame = img.read()

    imgColor, mask = colorFinder.update(frame, hsvVals)

    imgContours, contours = cvzone.findContours(frame, mask, minArea=2400)
    # Change when you have bigger notes

    if contours:
        cx, cy = contours[0]['center']
        # print(contours)
        #print(cx, cy)

        print('X: ', cx)

        diff = 270 - cx

        degree = round((90 + diff), 1)

        if degree <= 0:
            degree = 0
        if degree >= 180:
            degree = 180

        degree = 180 - degree

        print("Angle: ", degree)

        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org = (50, 50)

        # fontScale
        fontScale = 1

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 2

        # Using cv2.putText() method
        image = cv2.putText(imgContours, str(degree), org, font,
                            fontScale, color, thickness, cv2.LINE_AA)


    cv2.imshow('ImgColor', imgContours)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows()
