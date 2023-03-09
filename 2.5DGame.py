import tkinter as tk
from PIL import ImageTk, Image
class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=400,  height=400)

        self.label = tk.Label(self, text="Key input to console", width=20)
        self.label.pack(fill="both", padx=100, pady=100)

        self.label.bind("<w>", self.keypress)
        self.label.bind("<a>", self.keypress)
        self.label.bind("<s>", self.keypress)
        self.label.bind("<d>", self.keypress)

        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def keypress(self, event): #this is how we'll register the key events

        if event.char == 'w':
            print("W was pressed") #replace wasd prints with methods of turning.
        elif event.char == 'a':
            print("A was pressed")
        elif event.char=='s':
            print("S was pressed")
        elif event.char == 'd':
            print("D was pressed")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()