import cv2 
from face_recognition import recognize_face

video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    frame = recognize_face(frame)
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)
    if key != -1:
        break 

video.release()
cv2.destroyAllWindows()