import cv2
import cvzone
import pyfirmata2
from time import sleep
from cvzone.ColorModule import ColorFinder

colorFinder = ColorFinder(False)
img = cv2.VideoCapture(1)


hsvVals = {"hmin": 0, "smin": 0, "vmin": 242, "hmax": 179, "smax": 255, "vmax": 255}

port = "COM3"
board = pyfirmata2.Arduino(port)

wrist = board.get_pin('d:3:s')
shoulder = board.get_pin('d:9:s')
elbow = board.get_pin('d:10:s')
base = board.get_pin('d:2:s')
twist = board.get_pin('d:11:s')
grip = board.get_pin('d:6:s')

def startPos():

    elbow.write(180)
    wrist.write(110)
    base.write(90)
    shoulder.write(130)
    grip.write(100)

startPos()


openAngle = 100
closeAngle = 180


def grabObject(angle):

    base.write(angle)
    sleep(1.5)
    wrist.write(110)
    twist.write(90)
    sleep(1.5)
    shoulder.write(100)

    grip.write(openAngle)
    sleep(1.5)
    shoulder.write(85)
    wrist.write(110)
    # elbow.write(160)
    sleep(1.5)
    grip.write(155)
    sleep(1.5)
    shoulder.write(125)
    wrist.write(80)
    sleep(1.5)
    base.write(180)
    sleep(1.5)
    shoulder.write(85)
    wrist.write(100)
    sleep(1.5)
    grip.write(95)
    sleep(1.5)
    shoulder.write(110)
    sleep(1.5)
    startPos()


    print("Base is going to ", angle, " degrees")


while True:
    ret, frame = img.read()

    imgColor, mask = colorFinder.update(frame, hsvVals)

    imgContours, contours = cvzone.findContours(frame, mask, minArea=2400)
    # Change when you have bigger notes

    if contours:
        cx, cy = contours[0]['center']
        # print(contours)
        # print(cx, cy)

        print('X: ', cx)

        diff = 270 - cx
        print("Difference: ", diff)

        degree = round((90 + diff), 1)

        if degree <= 0:
            degree = 0
        if degree >= 180:
            degree = 180

        degree = 180 - degree

        print("Angle: ", degree)

        should_grab = input('Should I Grab Object (y/n)? => ')
        print(should_grab)

        if should_grab == 'y':
            grabObject(degree)
            print("****** grabbing object ******")

        print("Robot Desired Rotation: ", degree)

    cv2.imshow('ImgColor', imgContours)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows()

