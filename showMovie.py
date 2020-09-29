import cv2
import util

mov = cv2.VideoCapture("Resources/Movies/rotatingEarth.mp4")

while not util.is_exit_key_pressed(50):
    success, img = mov.read()
    cv2.imshow("Rotating Earth --> press 'q' to exit", img)
