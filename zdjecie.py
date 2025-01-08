import cv2 
from face_recognition import recognize_face
from deepface import DeepFace

img = cv2.imread('images/aaa.jpg') 
img = recognize_face(img)

cv2.imshow('aaa', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = DeepFace.analyze(img,actions=['emotion']) 