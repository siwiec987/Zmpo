import cv2.data
from deepface import DeepFace

def recognize_face(image):
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_classifier.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    result = DeepFace.analyze(image, actions=('emotion'), enforce_detection=False) 
    
    for(x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.putText(image, result[0].get('dominant_emotion'), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

    return image