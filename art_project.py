from Tkinter import *
from random import randint

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Window:
    def __init__(self, root):
        self.root = root
        self.setofPoints = []
        self.color = "#40E0D0"
        self.gameCanvas = Canvas(self.root, width=1000, height=600, bg="black")
        self.gameCanvas.pack()
        self.gameMenu = Menu(self.root)
        self.root.config(menu=self.gameMenu)
        self.fileMenu = Menu(self.gameMenu)
        self.gameMenu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Connect all nodes", command=self.connect)
        self.fileMenu.add_command(label="Color all lines", command=self.setlineColor)
        self.fileMenu.add_command(label="New", command=self.new)
        self.fileMenu.add_command(label="Exit", command=self.root.destroy)
        self.root.bind("<Button-1>", self.point)

    def point(self, event):
        self.gameCanvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="white")
        self.setofPoints.append(Node(event.x, event.y))
        self.root.mainloop()

    def connect(self):
        for i in self.setofPoints:
            for j in self.setofPoints:
                self.gameCanvas.create_line(i.x, i.y, j.x, j.y, fill="white")

    def new(self):
        self.setofPoints = []
        self.gameCanvas.delete(ALL)

    def setlineColor(self):
        for i in self.setofPoints:
            for j in self.setofPoints:
                R = hex((i.x + j.x) / 2)[2:]
                if len(R) >= 3:
                    R = R[-2:]
                elif len(R) == 1:
                    R = hex(randint(0, 15))[2:] + R
                G = hex((i.x + j.x + i.y + j.y) / 4)[2:]
                if len(G) >= 3:
                    G = G[-2:]
                elif len(G) == 1:
                    G = hex(randint(0, 15))[2:] + G
                B = hex((i.y + j.y) / 2)[2:]
                if len(B) >= 3:
                    B = B[-2:]
                elif len(B) == 1:
                    B = hex(randint(0, 15))[2:] + B
                self.color = "#" + R + G + B
                self.gameCanvas.create_line(i.x, i.y, j.x, j.y, fill=self.color)
        for i in self.setofPoints:
            self.gameCanvas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, fill="white")


def main():
    root = Tk()
    root.title("Computer Generated Art")
    root.geometry("1000x600+350+150")
    Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
