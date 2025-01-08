import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, PhotoImage
from recognize_from_pic import recognize_from_pic

img_label = None

def select_img():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

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
window.geometry("1200x800")
window.resizable(0,0)
window.configure(bg="#2e2e2e")

style = ttk.Style()
style.theme_use("clam")  # Use a theme that supports customization
style.configure("TFrame", background="#2e2e2e")
style.configure("CustomTButton", background="#4d4d4d", relief="flat")
style.configure("TLabel", background="#2e2e2e")

button_frame = ttk.Frame(master=window)
button_frame.pack(padx=10, pady=30)

select_img_icon = PhotoImage(file="images/image-icon.png")
camera_icon = PhotoImage(file="images/camera-icon.png")

select_img_button = ttk.Button(master=button_frame, image=select_img_icon, command=select_img, style="CustomTButton")
select_img_button.image = select_img_icon
select_img_button.pack(side=tk.LEFT, padx=15)

camera_button = ttk.Button(master=button_frame, image=camera_icon, command=lambda: print("Second button clicked"))
camera_button.image = camera_icon
camera_button.pack(side=tk.LEFT, padx=15)

window.mainloop()