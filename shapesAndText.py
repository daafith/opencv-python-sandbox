import cv2
import numpy as np
import util

square = np.zeros((600, 600, 3), np.uint8)
purple_square = np.copy(square)
# Why opencv uses BGR is beyond me
purple_square[:] = 100, 0, 100

diagonal_tiles = np.copy(square)
tile_size = int(square.shape[0] / 8)
for s in range(0, 8):
    diagonal_tiles[s * tile_size:(s + 1) * tile_size, s * tile_size:(s + 1) * tile_size] = 255, 255, 255

meh_face = np.copy(square)
meh_color = 111, 134, 145
cv2.circle(meh_face, (250, 200), 28, meh_color, -1)
cv2.circle(meh_face, (350, 200), 28, meh_color, -1)
cv2.circle(meh_face, (300, 280), 15, meh_color, -1)
cv2.line(meh_face, (250, 350), (350, 350), meh_color, 6)

while not util.is_exit_key_pressed():
    cv2.imshow("Black Square", square)
    cv2.imshow("Purple Square", purple_square)
    cv2.imshow("Diagonal Tiles", diagonal_tiles)
    cv2.imshow("Meh", meh_face)
