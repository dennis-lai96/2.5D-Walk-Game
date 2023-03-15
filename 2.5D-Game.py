from tkinter import *
from PIL import Image, ImageTk
import json


class GUI:
    def __init__(self, root):
        self.master = root
        self.master.title("2.5D Game")

        with open ("images/MAP.json") as f:
            data = json.load(f)
        string = (data['(0,0)']['east']['img'])
        print(string[0])

        self.img = ImageTk.PhotoImage(Image.open(string[0]))
        self.label = Label(image=self.img)
        self.label.grid(row=0, column=0)

        self.label.bind("<w>", self.keypress)  # MOVES forward
        self.label.bind("<a>", self.keypress)  # TURNS left
        self.label.bind("<s>", self.keypress)  # MOVES backward
        self.label.bind("<d>", self.keypress)  # TURNS right
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
