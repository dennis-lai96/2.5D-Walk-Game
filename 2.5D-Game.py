from tkinter import *
from PIL import Image, ImageTk
import json


class GUI:
    def __init__(self, root):
        self.newPosition = None
        self.master = root
        self.master.title("2.5D Game")

        with open("images/MAP.json") as f:
            self.data = json.load(f)

        self.currentPosition = '(0,1)'  # location
        self.currentHeading = 'south'  # heading
        self.currentPos = (self.data[self.currentPosition][self.currentHeading]['img'])
        print("Current Position is ", self.currentPosition, " and current heading is ", self.currentHeading)
        # print out image
        # print(self.currentPos)

        self.img = ImageTk.PhotoImage(Image.open(self.currentPos[0]))

        self.label = Label(image=self.img)
        self.label.grid(row=0, column=0)

        # Keybinds are blackboxed AF. No idea how that shit works.
        self.label.bind("<w>", self.keypress)  # MOVES forward
        self.label.bind("<a>", self.keypress)  # TURNS left
        self.label.bind("<s>", self.keypress)  # MOVES backward
        self.label.bind("<d>", self.keypress)  # TURNS right
        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def changeImg(self):
        self.newImg = ImageTk.PhotoImage(Image.open(self.currentPos[0]))
        self.label.configure(image=self.newImg)
        self.label.image = self.newImg

    def keypress(self, event):  # this is how we'll register the key events. comment out function later.

        if event.char == 'w':
            print("W was pressed")

            #retrieves coordinates of new location
            self.newPosition = self.data[self.currentPosition][self.currentHeading]['next-pos']
            print("Current position of is of type ", type(self.data[self.currentPosition]))
            print("New location is ", self.newPosition[0])
            print("New locations is of type ", type(self.newPosition[0]))

            #updates the current position
            self.currentPosition = self.newPosition[0]
            string = self.newPosition[0]
            self.currentPos = (self.data[string][self.currentHeading]['img'])

            #Code to change image here? Maybe it should be its own method?
            self.changeImg()



        elif event.char == 'a':
            print("A was pressed")
        elif event.char == 's':
            print("S was pressed")
            #retrieves coordinates of new location
            self.newPosition = self.data[self.currentPosition][self.currentHeading]['behind-pos']
            print("Current position of is of type ", type(self.data[self.currentPosition]))
            print("New location is ", self.newPosition[0])
            print("New locations is of type ", type(self.newPosition[0]))

            #updates the current position
            self.currentPosition = self.newPosition[0]
            string = self.newPosition[0]
            self.currentPos = (self.data[string][self.currentHeading]['img'])

            #Code to change image here? Maybe it should be its own method?
            self.changeImg()


        elif event.char == 'd':
            print("D was pressed")



if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = GUI(myTkRoot)
    myTkRoot.mainloop()
