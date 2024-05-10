import cv2
from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog as tkFileDialog
import numpy as np
import threading
# from PCNN import PCNN_Model


class FaceRecognition :
    def __init__(self, root):
        self.window = root
        self.window.title('Face Recognition')
        self.window.minsize(700, 700)
        self.window.geometry('1600x900+150+100')
        self.window.config(background='#032024')
        self.gender = None
        self.accuracyRate = None
        self.accuracy = None
        self.results = None
        self.image = None
        self.frame = None
        self.submitButton = None
        self.selectButton = None

    def imageUploader(self):
        filename = tkFileDialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])

        if filename:
            self.image = ImageTk.PhotoImage(Image.open(filename).resize((350, 350)))
            self.frame.config(image=self.image)

    def drawSquareShape(self):
        leftBar = Canvas(self.window, width=1, height=580)
        leftBar.place(x=750, y=120)
        upperBar = Canvas(self.window, width=580, height=1)
        upperBar.place(x=750, y=120)
        rightBar = Canvas(self.window, width=1, height=580)
        rightBar.place(x=1330, y=120)
        bottomBar = Canvas(self.window, width=580, height=1)
        bottomBar.place(x=750, y=700)

    def displayData(self) :
        self.image = ImageTk.PhotoImage(Image.open('images.png').resize((350, 350)))
        self.frame = Label(self.window, image=self.image)
        self.frame.photo = self.image
        self.frame.place(x=250, y=150)

        self.submitButton = Button(text="Submit", background='#29a9ba', relief=FLAT, cursor= "hand2",
                              bd=0, highlightthickness=0, font=('Arial', 24, 'bold'), width=15)
        self.submitButton.place(x=280, y=550)

        self.selectButton = Button(text="Select Photo", background='#29a9ba', relief=FLAT, cursor= "hand2",
                              bd=0, highlightthickness=0, font=('Arial', 24, 'bold'), width=15, command=self.imageUploader)
        self.selectButton.place(x=280, y=610)

        self.drawSquareShape()
        result_title = Label(self.window, text='Results', background='#032024', foreground='#FFFFFF',
                            font=('Arial', 24, 'bold'))
        result_title.place(x=970, y=150)

        split_line = Canvas(self.window, width=130, height=1)
        split_line.place(x=970, y=200)

        self.results = Label(self.window, text=f'Gender : {self.gender}', background='#032024', foreground='#FFFFFF',
                            font=('Arial', 20, 'bold'))
        self.results.place(x=780, y=250)

        split_line = Canvas(self.window, width=500, height=1)
        split_line.place(x=780, y=400)

        accuracy_title = Label(self.window, text='Accuracy', background='#032024', foreground='#FFFFFF',
                            font=('Arial', 24, 'bold'))
        accuracy_title.place(x=970, y=420)

        self.accuracy = Label(self.window, text=f'accuracy : {self.accuracyRate}', background='#032024', foreground='#FFFFFF',
                            font=('Arial', 20, 'bold'))
        self.accuracy.place(x=780, y=490)

        split_line = Canvas(self.window, width=150, height=1)
        split_line.place(x=970, y=460)

    def run(self) :
        self.displayData()


def main():
    root = Tk()
    app = FaceRecognition(root)
    app.run()
    root.mainloop()

if __name__ == '__main__':
    main()
