import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('1000x800')

frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame, width=500, height=500)
label.pack()

cap = cv2.VideoCapture(0)

def updateFrame():
    ret, frame_cv2 = cap.read()
    if ret:
        frame_cv2 = cv2.resize(frame_cv2, (500, 500))
        img = cv2.cvtColor(frame_cv2, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=pil_img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    window.after(10, updateFrame)

updateFrame()
window.mainloop()
