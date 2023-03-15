from tkinter import *
from PIL import Image, ImageTk
import json

class GUI:
    def __init__(self, root):
        self.newPosition = None
        self.master = root
        self.master.title("2.5D Game")
        #loads the json file
        with open("images/MAP.json") as f:
            self.data = json.load(f)

        #initalizings tarting position
        self.currentPosition = '(1,1)'  # location
        self.currentHeading = 'north'  # heading
        self.currentPos = (self.data[self.currentPosition][self.currentHeading]['img'])
        print("Current Position is ", self.currentPosition, " and current heading is ", self.currentHeading)
        print(self.currentHeading)

        #making the image and label.
        self.img = ImageTk.PhotoImage(Image.open(self.currentPos[0]))
        self.label = Label(image=self.img)
        self.label.grid(row=0, column=0)

        #making keybinds
        self.label.bind("<w>", self.keypress)  # MOVES forward
        self.label.bind("<a>", self.keypress)  # TURNS left
        self.label.bind("<s>", self.keypress)  # MOVES backward
        self.label.bind("<d>", self.keypress)  # TURNS right
        self.label.focus_set() #Not sure how this works
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def changeImg(self):#helper function to update the image
        self.newImg = ImageTk.PhotoImage(Image.open(self.currentPos[0]))
        self.label.configure(image=self.newImg)
        self.label.image = self.newImg

    def keypress(self, event):

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

            #Update image
            self.changeImg()

        elif event.char == 'a':
            print("A was pressed") #changes heading depending on the direction currently at
            if self.currentHeading== 'north': #will result in west
                self.currentHeading ='west'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            elif self.currentHeading== 'west': #will result in south
                self.currentHeading ='south'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            elif self.currentHeading== 'south': #will result in south
                self.currentHeading ='east'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            elif self.currentHeading== 'east': #will result in south
                self.currentHeading ='north'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            print(self.currentHeading)
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
            if self.currentHeading== 'north': #will result in east
                self.currentHeading ='east'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            elif self.currentHeading== 'east': #will result in south
                self.currentHeading ='south'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            elif self.currentHeading== 'south': #will result in west
                self.currentHeading ='west'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            elif self.currentHeading== 'west': #will result in north
                self.currentHeading ='north'
                self.currentPos=self.data[self.currentPosition][self.currentHeading]['img']
                self.changeImg()

            print(self.currentHeading)

if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = GUI(myTkRoot)
    myTkRoot.mainloop()
