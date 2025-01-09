import cv2
from deepface import DeepFace

def recognize_face(img):
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_classifier.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    results = DeepFace.analyze(img, actions=('emotion'), enforce_detection=False) 
    
    for(x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.putText(img, results[0].get('dominant_emotion'), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

    return img