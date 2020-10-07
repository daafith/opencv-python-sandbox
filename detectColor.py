import cv2
import util
import numpy as np


def noop(f):
    pass


car = cv2.imread("Resources/Images/car.png")
car_window = "Foobar"
trackbar_hue_min = "Hue min"
trackbar_hue_max = "Hue max"
trackbar_saturation_min = "Sat min"
trackbar_saturation_max = "Sat max"
trackbar_value_min = "Value min"
trackbar_value_max = "Value max"

cv2.namedWindow(car_window)
# cv2.resizeWindow(car_window, 700, 500)

# Initial values are normally 0, but the ideal values can be found by manually modifying the trackbars
cv2.createTrackbar(trackbar_hue_min, car_window, 0, 179, noop)
cv2.createTrackbar(trackbar_hue_max, car_window, 19, 179, noop)
cv2.createTrackbar(trackbar_saturation_min, car_window, 110, 255, noop)
cv2.createTrackbar(trackbar_saturation_max, car_window, 240, 255, noop)
cv2.createTrackbar(trackbar_value_min, car_window, 153, 255, noop)
cv2.createTrackbar(trackbar_value_max, car_window, 255, 255, noop)

hsv_image = cv2.cvtColor(car, cv2.COLOR_BGR2HSV)

while not util.is_exit_key_pressed():
    hue_min = cv2.getTrackbarPos(trackbar_hue_min, car_window)
    hue_max = cv2.getTrackbarPos(trackbar_hue_max, car_window)
    sat_min = cv2.getTrackbarPos(trackbar_saturation_min, car_window)
    sat_max = cv2.getTrackbarPos(trackbar_saturation_max, car_window)
    value_min = cv2.getTrackbarPos(trackbar_value_min, car_window)
    value_max = cv2.getTrackbarPos(trackbar_value_max, car_window)

    lower_bound = np.array([hue_min, sat_min, value_min])
    upper_bound = np.array([hue_max, sat_max, value_max])
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    result = cv2.bitwise_and(car, car, mask=mask)

    cv2.imshow("Detect color", util.stack_images(([car, hsv_image], [mask, result])))


