import cv2
import util


BLUE = 255, 0, 0
face = cv2.imread("Resources/Images/david.jpg")
smiles = cv2.imread("Resources/Images/twoSmiles.jpg")
gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
gray_smiles = cv2.cvtColor(smiles, cv2.COLOR_BGR2GRAY)

# Quick, not the most accurate out there.
face_cascade = cv2.CascadeClassifier("Resources/Cascades/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray_face, 1.1, 4)
two_faces = face_cascade.detectMultiScale(gray_smiles, 1.2, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(face, (x, y), (x + w, y + h), BLUE, 2)

for (x, y, w, h) in two_faces:
    cv2.rectangle(smiles, (x, y), (x + w, y + h), BLUE, 2)

while not util.is_exit_key_pressed():
    cv2.imshow("Face", face)
    cv2.imshow("Smiles", smiles)
