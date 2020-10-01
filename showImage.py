import cv2
import numpy as np
import util

ado = cv2.imread("Resources/Images/ado.jpg")
img = cv2.imread("Resources/Images/david.jpg")
canny = cv2.Canny(img, 80, 120)

kernel = np.ones((2, 2), np.uint8)
eroded = cv2.erode(img, kernel, iterations=3)
bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(bgr, (9, 9), 0)

hor = np.hstack((img, eroded))
vert = np.vstack((bgr, blurred))

half_size_face = util.resize_image(img, 50)
half_ado = util.resize_image(ado, 50)
quarter_size_face = util.resize_image(img, 25)
bloated = util.resize_image(img, 150)

while not util.is_exit_key_pressed():
    cv2.imshow("David", img)
    cv2.imshow("H-Stacked", hor)
    cv2.imshow("V-Stacked", vert)
    cv2.imshow("BGR2Gray", bgr)
    cv2.imshow("Blurred Gray", blurred)
    cv2.imshow("RGB2GRAY", cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
    cv2.imshow("Canny", canny)
    cv2.imshow("Dilated", cv2.dilate(canny, kernel, iterations=1))
    cv2.imshow("Half", half_size_face)
    cv2.imshow("Quarter", quarter_size_face)
    cv2.imshow("Bloated", bloated)
    cv2.imshow("Cropped", img[0:100, 20:120])
    cv2.imshow("ADO", half_ado)

