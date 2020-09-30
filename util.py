import cv2


def is_exit_key_pressed(delay=1):
    """
    Waits for 'q' to be pressed. The delay is 1 milliseconds by default but can be set.
    :param delay:
    :return:
    """
    return cv2.waitKey(delay) & 0XFF == ord('q')


def resize_image(image, percentage):
    """
    Returns a resized image. Not exactly precise, but good enough
    :param image:
    :param percentage: anything greater than 0
    :return:
    """
    if percentage <= 0:
        raise Exception("A percentage must be greater than  0")
    divisor = 100 / percentage
    dimension = int(image.shape[1] / divisor), int(image.shape[0] / divisor)
    return cv2.resize(image, dimension)
