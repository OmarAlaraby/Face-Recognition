import cv2
from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog as tkFileDialog
import numpy as np
import threading


class FaceRecognition:
    def __init__(self, root):
        self.window = root
        self.window.title('Face Recognition')
        self.window.minsize(700, 700)
        self.window.geometry('1700x1000+150+100')
        self.window.config(background='#120d38')
        self.frame = Frame(root)
        self.frame.pack(side=RIGHT, anchor=E, padx=120)
        self.label = Label(self.frame, width=600, height=600, background='#5146ab')
        self.label.pack()
        self.cap = cv2.VideoCapture(0)
        self.name = 'Uknown'
        self.age = 'NA'
        self.phoneNumber = 'NA'

    def updateFrame(self):
        ret, frame_cv2 = self.cap.read()
        if ret:
            frame_cv2 = cv2.resize(frame_cv2, (580, 580))
            img = cv2.cvtColor(frame_cv2, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=pil_img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
        self.window.after(10, self.updateFrame)

    def displayData(self) :
        data = f'Name : {self.name} \n\nAge : {self.age} \n\nPhone Number : {self.phoneNumber}'
        dataLabel = Label(self.window, text=data,
                         font=("Arial", 32, "bold"),
                         justify="left",
                         foreground="white",
                         background=self.window.cget("bg"))
        dataLabel.pack(side=LEFT, anchor=NW, padx=100, pady=200)

    def recognizeFrame(self) :
        pass

    def run(self) :
        self.updateFrame()
        self.displayData()
        self.recognizeFrame()


def main():
    root = Tk()
    app = FaceRecognition(root)
    app.run()
    root.mainloop()

if __name__ == '__main__':
    main()
