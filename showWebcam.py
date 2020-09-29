import cv2
import util

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
webcam.set(3, 800)
webcam.set(4, 600)

while not util.is_exit_key_pressed():
    success, img = webcam.read()
    cv2.imshow("Your Webcam --> press 'q' to exit", img)

webcam.release()
cv2.destroyAllWindows()