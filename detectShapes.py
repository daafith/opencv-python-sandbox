import cv2
import util
import numpy as np


BLUR_THRESHOLD = 50
BLUE = 255, 0, 0
GREEN = 0, 255, 0
BLACK = 0, 0, 0
# A lower percentage results in more approximation points
APPROXIMATION_PERCENTAGE = 0.02
SHAPES = {3: "Triangle", 4: "Square", 8: "Circle"}

shapes = cv2.imread("Resources/Images/shapes.png")
shapes_gray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
shapes_gray_blurred = cv2.GaussianBlur(shapes_gray, (7, 7), 1)

shapes_canny = cv2.Canny(shapes_gray_blurred, BLUR_THRESHOLD, BLUR_THRESHOLD)
blank_image = np.zeros_like(shapes)


def determine_shapes(img):
    out_lines = cv2.Canny(img, BLUR_THRESHOLD, BLUR_THRESHOLD)
    contours, hierarchy = cv2.findContours(out_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    copy = img.copy()
    for contour in contours:
        area = cv2.contourArea(contour)
        # Define a threshold in pixels to prevent noise
        if area > 500:
            cv2.drawContours(copy, contour, -1, BLUE, 3)
            perimeter = cv2.arcLength(contour, closed=True)
            approximate_points = cv2.approxPolyDP(contour, APPROXIMATION_PERCENTAGE * perimeter, closed=True)

            x, y, w, h = cv2.boundingRect(approximate_points)
            cv2.rectangle(copy, (x, y), (x + w, y + h), GREEN, 2)
            number_of_points = len(approximate_points)

            if number_of_points == 3:
                name = "Triangle"
            elif number_of_points == 4:
                aspect_ratio = w / float(h)
                if 0.98 < aspect_ratio < 1.03:
                    name = "Square"
                else:
                    name = "Rectangle"
            elif number_of_points > 4:
                name = "Circle"
            else:
                name = "Shapeless"

            cv2.putText(copy, name, (x + (w // 2) - 20, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.65,
                        BLACK, 2)
    return copy


cv2.imshow("Foo", util.stack_images(([shapes, shapes_gray, shapes_gray_blurred],
                                     [shapes_canny, determine_shapes(shapes), blank_image]), 0.85))
cv2.waitKey(0)
