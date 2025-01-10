import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, PhotoImage
from recognize_from_pic import recognize_from_pic

img_label = None
video_running = False
video = None

def select_img():
    global video_running, video, img_label

    if video_running:
        video_running = False
        if video is not None:
            video.release()
        if img_label is not None:
            img_label.destroy()
            img_label = None

    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

    if len(path) > 0:
        img = cv2.imread(path)
        img = recognize_from_pic(img)
        show_img(img)
    else:
        print("Nothing selected.")
        return None
    
def show_img(processed_img):
    global img_label
    if img_label is None:
        img_label = ttk.Label(master = window, image=processed_img)
        img_label.image = processed_img
        img_label.pack()
    else:
        img_label.configure(image=processed_img)
        img_label.image = processed_img

def recognize_from_vid():
    global video_running, video, img_label

    if video_running:
        video_running = False
        if video is not None:
            video.release()
        if img_label is not None:
            img_label.destroy()
            img_label = None
        return

    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Error: Could not open video device.")
        return None
    
    video_running = True

    def process_frame():
        if not video_running:
            return

        success, frame = video.read()
        if not success:
            print("Error: Could not read frame from video device.")
            video.release()
            return
        
        try:
            frame = recognize_from_pic(frame)
            show_img(frame)
        except Exception as e:
            print(f"Error during image processing: {e}")
            video.release()
            return
        
        window.after(10, process_frame)
    
    process_frame()


window = tk.Tk()
window.iconphoto(True, PhotoImage(file="images/app-icon.png"))
window.title("Emotion detection")
window.geometry("1200x800")
window.resizable(0,0)
window.configure(bg="#2e2e2e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#2e2e2e")
style.configure("TButton", background="#616161", relief="flat")
style.configure("TLabel", background="#2e2e2e")

button_frame = ttk.Frame(master=window)
button_frame.pack(padx=10, pady=30)

select_img_icon = PhotoImage(file="images/image-icon.png")
camera_icon = PhotoImage(file="images/camera-icon.png")

select_img_button = ttk.Button(master=button_frame, image=select_img_icon, command=select_img)
select_img_button.image = select_img_icon
select_img_button.pack(side=tk.LEFT, padx=15)

camera_button = ttk.Button(master=button_frame, image=camera_icon, command=recognize_from_vid)
camera_button.image = camera_icon
camera_button.pack(side=tk.LEFT, padx=15)

window.mainloop()