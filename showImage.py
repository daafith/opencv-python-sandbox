import cv2
import util

img = cv2.imread("Resources/Images/david.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9, 9), 0)
canny = cv2.Canny(img, 80, 80)

while not util.is_exit_key_pressed():
    cv2.imshow("David", img)
    cv2.imshow("Gray David", gray)
    cv2.imshow("Blurred Gray David", blurred)
    cv2.imshow("Canny David", canny)
