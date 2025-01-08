import cv2 
from face_recognition import recognize_face
from deepface import DeepFace
from PIL import Image, ImageTk
import tkinter as tk

def recognize_from_pic(path):
    img = cv2.imread(path)
    img = resize_image(img, 600, 400)
    img = recognize_face(img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    return img

def resize_image(img, width, height):
    old_height, old_width, channels = img.shape

    if old_width > old_height:
        resize_factor = width / old_width
    else:
        resize_factor = height / old_height

    new_width = old_width * resize_factor
    new_height = old_height * resize_factor

    print("\n\nOld wymiary")
    print(old_width)
    print(old_height)
    print("\n\nNew wymiary")
    print(new_width)
    print(new_height)

    img = cv2.resize(img, (int(new_width), int(new_height)))

    return img