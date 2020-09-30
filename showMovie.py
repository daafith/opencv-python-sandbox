import cv2
import util

while not util.is_exit_key_pressed(50):
    success, img = cv2.VideoCapture("Resources/Movies/rotatingEarth.mp4").read()
    cv2.imshow("Rotating Earth --> press 'q' to exit", img)
