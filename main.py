# import cv2 
# from face_recognition import recognize_face
# from deepface import DeepFace

# read image 
# img = cv2.imread('images/aaa.jpg') 
# img = recognize_face(img)

# cv2.imshow('aaa', img)
# cv2.waitKey(0)

# video = cv2.VideoCapture(0)

# while True:
#     success, frame = video.read()
#     frame = recognize_face(frame)
#     cv2.imshow('Video', frame)
#     key = cv2.waitKey(1)
#     if key != -1:
#         break 

# video.release()
# cv2.destroyAllWindows()

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from recognize_from_pic import recognize_from_pic

img_label = None

def select_img():
    path = filedialog.askopenfilename()

    if len(path) > 0:
        processed_img = recognize_from_pic(path)
        
        global img_label
        if img_label is None:
            img_label = ttk.Label(master = window, image=processed_img)
            img_label.image = processed_img
            img_label.pack()
        else:
            img_label.configure(image=processed_img)
            img_label.image = processed_img

    else:
        print("Pusto")
        return None

window = tk.Tk()
window.title("Pokaż ryja")
window.geometry("800x600")
window.resizable(0,0)

select_img_button = ttk.Button(master = window, text="Select an image", command=select_img)
select_img_button.pack()

window.mainloop()