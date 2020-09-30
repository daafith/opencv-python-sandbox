import cv2
import numpy as np

import util

ado = cv2.imread("Resources/Images/ado.jpg")

width = 450
height = 300
# Need to investigate this more
src = np.float32([[492, 913], [555, 80], [125, 457], [225, 425]])
dst = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(ado, matrix, (width, height))

while not util.is_exit_key_pressed():
    cv2.imshow("Perspective", warped)
