from tkinter import *
from PIL import Image,ImageTk

class GUI:
    def __init__(self,root):
        self.master = root
        self.master.title("test")

        self.img= ImageTk.PhotoImage(Image.open("images/loudly-crying-face_1f62d.png"))
        self.label = Label(image=self.img)
        self.label.grid(row=0,column=0)



        self.label.bind("<w>", self.keypress)
        self.label.bind("<a>", self.keypress)
        self.label.bind("<s>", self.keypress)
        self.label.bind("<d>", self.keypress)
        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())


    def keypress(self, event):  # this is how we'll register the key events

        if event.char == 'w':
            print("W was pressed")  # replace wasd prints with methods of turning.
        elif event.char == 'a':
            print("A was pressed")
        elif event.char == 's':
            print("S was pressed")
        elif event.char == 'd':
            print("D was pressed")


if __name__ == '__main__':

    myTkRoot = Tk()
    my_gui = GUI(myTkRoot)
    myTkRoot.mainloop()
