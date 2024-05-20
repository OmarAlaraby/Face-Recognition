from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog as tkFileDialog
from Adaline import Adaline
from utilities import load_data, preProcess
import matplotlib.pyplot as plt
from utilities import fix



class fruitRecognition :
    def __init__(self, root):
        self.window = root
        self.window.title('Fruit Recognition')
        self.window.minsize(700, 700)
        self.window.geometry('1600x900+150+100')
        self.window.config(background='#032024')
        self.gender = None
        self.accuracyRate = None
        self.accuracy = None
        self.results = None
        self.image = None
        self.displayedImage = None
        self.frame = None
        self.submitButton = None
        self.selectButton = None
        self.model = None
    def trainModel(self):
        X, Y = load_data()
        self.model = Adaline(len(X[0]))
        self.model.train(X, Y)
    def recogniseImage(self):
        image = preProcess(self.image)
        result = self.model.predict(image)
        self.results.config(text=f'Type : {result}')

    def displayPlot(self):
        plt.plot(self.model.errors)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('')
        plt.show()
    def getAccuracy(self):
        X, Y = load_data()
        acc = self.model.getAccuracy(X, Y)
        self.accuracy.config(text=f'Accuracy : {acc}%')

    def imageUploader(self):
        filename = tkFileDialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])

        if filename:
            self.displayedImage = ImageTk.PhotoImage(Image.open(filename).resize((350, 350)))
            self.image = Image.open(filename).resize((200, 200))
            self.frame.config(image=self.displayedImage)
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
        self.displayedImage = ImageTk.PhotoImage(Image.open('images.png').resize((350, 350)))
        self.frame = Label(self.window, image=self.displayedImage)
        self.frame.photo = self.displayedImage
        self.frame.place(x=250, y=150)

        self.submitButton = Button(text="Submit", background='#29a9ba', relief=FLAT, cursor= "hand2",
                              bd=0, highlightthickness=0, font=('Arial', 24, 'bold'), width=15, command=self.recogniseImage)
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

        self.results = Label(self.window, text='Type : Uknown', background='#032024', foreground='#FFFFFF',
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

        split_line = Canvas(self.window, width=500, height=1)
        split_line.place(x=780, y=600)

        split_line = Canvas(self.window, width=150, height=1)
        split_line.place(x=970, y=460)

        plotButton = Button(text="Display Plot", background='#29a9ba', relief=FLAT, cursor= "hand2",
                              bd=0, highlightthickness=0, font=('Arial', 24, 'bold'), width=15, command=self.displayPlot)
        plotButton.place(x=900, y=625)


    def run(self) :
        self.trainModel()
        self.displayData()
        self.getAccuracy()


def main():
    root = Tk()
    app = fruitRecognition(root)
    app.run()
    root.mainloop()

if __name__ == '__main__':
    main()
