import cv2
import cvzone
import pyfirmata2
from time import sleep

port = "COM3"
board = pyfirmata2.Arduino(port)

wrist = board.get_pin('d:3:s')
shoulder = board.get_pin('d:9:s')
elbow = board.get_pin('d:10:s')
base = board.get_pin('d:5:s')
twist = board.get_pin('d:11:s')
grip = board.get_pin('d:6:s')

elbow.write(180)
wrist.write(110)
base.write(90)
shoulder.write(90)
grip.write(100)

openAngle = 100
closeAngle = 180

thres = 0.55
nmsThres = 0.2
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

mp = 270


def grabObject(angle):

    base.write(angle)
    sleep(1.5)
    shoulder.write(65)
    wrist.write(120)
    twist.write(90)
    grip.write(openAngle)
    sleep(1.5)
    shoulder.write(45)
    wrist.write(157)
    elbow.write(160)
    sleep(1.5)
    grip.write(160)
    sleep(1.5)
    shoulder.write(110)
    base.write(180)
    sleep(1.5)
    shoulder.write(50)
    sleep(1.5)
    grip.write(openAngle)


    print("Base is going to ", angle, " degrees")


while True:

    base.write(0)


