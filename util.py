import cv2


def is_exit_key_pressed(delay=1):
    """
    Waits for 'q' to be pressed. The delay is 1 milliseconds by default but can be set.
    """
    return cv2.waitKey(delay) & 0XFF == ord('q')
