import cv2 
from PIL import Image, ImageTk
from face_recognition import recognize_face

def recognize_from_pic(img):
    try:
        img = resize_image(img, 600, 400)
        img = recognize_face(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        return img
    except Exception as e:
        print(f"Error during image processing: {e}")
        return None

def resize_image(img, width, height):
    old_height, old_width = img.shape[:2]

    if old_width > old_height:
        resize_factor = width / old_width
    else:
        resize_factor = height / old_height

    new_width = int(old_width * resize_factor)
    new_height = int(old_height * resize_factor)
    img = cv2.resize(img, (new_width, new_height))

    return img