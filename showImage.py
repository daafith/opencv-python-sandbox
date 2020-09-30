import cv2
import numpy as np
import util

img = cv2.imread("Resources/Images/david.jpg")
ado = cv2.imread("Resources/Images/ado.jpg")
canny = cv2.Canny(img, 80, 120)
kernel = np.ones((2, 2), np.uint8)

half_size_face = util.resize_image(img, 50)
half_ado = util.resize_image(ado, 50)
quarter_size_face = util.resize_image(img, 25)
bloated = util.resize_image(img, 150)

while not util.is_exit_key_pressed():
    cv2.imshow("David", img)
    cv2.imshow("BGR2Gray", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    cv2.imshow("Blurred Gray", cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (9, 9), 0))
    cv2.imshow("Canny", canny)
    cv2.imshow("RGB2GRAY", cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
    cv2.imshow("Dilated", cv2.dilate(canny, kernel, iterations=1))
    cv2.imshow("Eroded", cv2.erode(img, kernel, iterations=3))
    cv2.imshow("Half", half_size_face)
    cv2.imshow("Quarter", quarter_size_face)
    cv2.imshow("Bloated", bloated)
    cv2.imshow("Cropped", img[0:100, 20:120])
    cv2.imshow("ADO", half_ado)

