import cv2
import util


def noop(f):
    pass


car = cv2.imread("Resources/Images/car.jpg")
window_name = "Foobar"
cv2.namedWindow(window_name)
cv2.resizeWindow(window_name, 700, 400)
cv2.createTrackbar("Hue min", window_name, 0, 179, noop)
cv2.createTrackbar("Hue max", window_name, 179, 179, noop)
cv2.createTrackbar("Sat min", window_name, 0, 255, noop)
cv2.createTrackbar("Sat max", window_name, 255, 255, noop)
cv2.createTrackbar("Value min", window_name, 0, 255, noop)
cv2.createTrackbar("Value max", window_name, 255, 255, noop)

hue_saturation = cv2.cvtColor(car, cv2.COLOR_BGR2HSV)

while not util.is_exit_key_pressed():
    cv2.imshow("Car", car)
    cv2.imshow("HSV", hue_saturation)
