from Tkinter import *
import math


class Window:
    def __init__(self, parent, Area):
        self.Area = Area
        self.parent = parent
        self.parent.configure(background="white")
        self.stop = False
        self.gen = 0
        self.initUI()

    def initUI(self):
        self.parent.title("Conway's Game Of Life")
        gameMenu = Menu(self.parent)
        self.parent.config(menu=gameMenu)
        fileMenu = Menu(gameMenu)
        gameMenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Exit", command=self.parent.destroy)
        self.gameCanvas = Canvas(self.parent)
        self.gameCanvas.grid(row=0, column=0, rowspan=25, columnspan=25)
        self.gameCanvas.create_line(270, 0, 270, 300, fill="red")
        self.gameCanvas.create_text(320, 20, width=95, text="Generation: " + str(self.gen),
                                    font=("Helvetica 8"))
        for i in range(25):
            for j in range(25):
                if self.Area[i][j].state == 1:
                    self.gameCanvas.create_oval(((10 * self.Area[i][j].x) + 5), ((10 * self.Area[i][j].y) + 5),
                                                ((10 * self.Area[i][j].x) + 15), ((10 * self.Area[i][j].y) + 15),
                                                fill="red")
        nextStepButton = Button(self.parent, text="Next Step",
                           font=("Helvetica 8"), command=self.NextStep)
        nextStepButton.grid(row=26, column=12)

    def NextStep(self):
        self.gameCanvas.delete(ALL)
        self.gameCanvas = Canvas(self.parent)
        self.gameCanvas.grid(row=0, column=0, rowspan=25, columnspan=25)
        self.gameCanvas.create_line(270, 0, 270, 300, fill="red")
        self.gen += 1
        self.gameCanvas.create_text(320, 20, width=95, text="Generation: " + str(self.gen),
                                    font=("Helvetica 8"))
        for i in range(25):
            for j in range(25):
                self.Area[i][j].rules()
        Moore(self.Area)
        for i in range(25):
            for j in range(25):
                if self.Area[i][j].state == 1:
                    self.gameCanvas.create_oval(((10 * self.Area[i][j].x) + 5), ((10 * self.Area[i][j].y) + 5),
                                                ((10 * self.Area[i][j].x) + 15), ((10 * self.Area[i][j].y) + 15),
                                                fill="red")


class Cell:
    def __init__(self, x, y):
        self.state = 0
        self.x = x
        self.y = y
        self.alive_n = 0

    def rules(self):
        if (self.alive_n < 2) and (self.state == 1):
            self.state = 0
        elif (self.alive_n > 3) and (self.state == 1):
            self.state = 0
        elif (self.state == 1) and ((self.alive_n == 2)or(self.alive_n == 3)):
            self.state = 1
        elif (self.state == 0) and (self.alive_n == 3):
            self.state = 1

    def set_alive(self, state1, state2, state3, state4, state5, state6, state7, state8):
        self.alive_n = state1 + state2 + state3 + state4 + state5 + state6 + state7 + state8


def Moore(Area):
    for i in range(25):
        for j in range(25):
            if (i == 0) and (j == 24):
                Area[i][j].set_alive(0, 0, 0, 0, 0, Area[i][j - 1].state, Area[i - 1][j - 1].state,
                                     Area[i + 1][j].state)
            elif (i == 0) and (j == 0):
                Area[i][j].set_alive(0, 0, 0, 0, 0, Area[i][j + 1].state, Area[i + 1][j + 1].state,
                                     Area[i + 1][j].state)
            elif (i == 0) and (j == 24):
                Area[i][j].set_alive(0, 0, 0, 0, 0, Area[i][j - 1].state, Area[i + 1][j + 1].state,
                                     Area[i + 1][j].state)
            elif (i == 24) and (j == 0):
                Area[i][j].set_alive(0, 0, 0, 0, 0, Area[i - 1][j].state, Area[i - 1][j + 1].state,
                                     Area[i][j + 1].state)
            elif (i == 24) and (j == 24):
                Area[i][j].set_alive(0, 0, 0, 0, 0, Area[i - 1][j].state, Area[i - 1][j - 1].state,
                                     Area[i][j - 1].state)
            elif (j == 0) and (i != 0) and (i != 24):
                Area[i][j].set_alive(0, 0, 0, Area[i - 1][j].state, Area[i - 1][j + 1].state, Area[i][j + 1].state,
                                     Area[i + 1][j + 1].state,
                                     Area[i + 1][j].state)
            elif (j == 24) and (i != 0) and (i != 24):
                Area[i][j].set_alive(0, 0, 0, Area[i - 1][j].state, Area[i - 1][j - 1].state, Area[i][j - 1].state,
                                     Area[i + 1][j - 1].state,
                                     Area[i + 1][j].state)
            elif (i == 0)and(j != 0) and (j != 24):
                Area[i][j].set_alive(0, 0, 0, Area[i + 1][j].state, Area[i + 1][j + 1].state, Area[i][j + 1].state,
                                     Area[i + 1][j - 1].state,
                                     Area[i][j - 1].state)
            elif (i == 24) and (j != 0) and (j != 24):
                Area[i][j].set_alive(0, 0, 0, Area[i - 1][j].state, Area[i - 1][j + 1].state, Area[i][j + 1].state,
                                     Area[i - 1][j - 1].state,
                                     Area[i][j - 1].state)
            else:
                Area[i][j].set_alive(Area[i][j + 1].state, Area[i + 1][j + 1].state, Area[i - 1][j + 1].state,
                                     Area[i][j - 1].state, Area[i - 1][j - 1].state, Area[i - 1][j].state,
                                     Area[i + 1][j].state,
                                     Area[i + 1][j - 1].state)


def new(gameCanvas, Area):
    global root1
    gameCanvas.delete(ALL)
    gameCanvas = Canvas(root1)
    gameCanvas.grid(row=0, column=0, rowspan=25, columnspan=25)
    gameCanvas.create_line(270, 0, 270, 300, fill="red")
    gameCanvas.create_text(320, 30, width=95, text="Please set the initial conditions in the grid",
                           font=("Helvetica 8"))
    for i in range(25):
        for j in range(25):
            if Area[i][j].state == 0:
                gameCanvas.create_oval(((10 * Area[i][j].x) + 5), ((10 * Area[i][j].y) + 5),
                                   ((10 * Area[i][j].x) + 15), ((10 * Area[i][j].y) + 15),
                                   activefill="red")
            else:
                gameCanvas.create_oval(((10 * Area[i][j].x) + 5), ((10 * Area[i][j].y) + 5),
                                       ((10 * Area[i][j].x) + 15), ((10 * Area[i][j].y) + 15),
                                       fill="red")
            gameCanvas.bind("<Button-1>", callback)


def callback(event):
    global Area, gameCanvas
    x = event.x - 5
    y = event.y - 5
    if math.floor((x / 10.0) + 0.2) == math.floor((x / 10.0) - 0.2):
        x = math.floor((x / 10.0) + 0.2)
    if math.floor((y / 10.0) + 0.2) == math.floor((y / 10.0) - 0.2):
        y = math.floor((y / 10.0) + 0.2)
    if (x >= 0) and (x <= 24) and (y >= 0) and (y <= 24):
        for i in range(25):
            for j in range(25):
                if (Area[i][j].x == x)and(Area[i][j].y == y):
                    if Area[i][j].state == 0:
                        Area[i][j].state = 1
                    elif Area[i][j].state == 1:
                        Area[i][j].state = 0
        new(gameCanvas, Area)


def initializer():
    global Area, gameCanvas, root1
    root1 = Tk()
    Area = [[Cell(i, j) for i in range(25)] for j in range(25)]
    root1.geometry("400x300+350+150")
    root1.title("Conway's Game Of Life")
    gameMenu = Menu(root1)
    root1.config(menu=gameMenu)
    fileMenu = Menu(gameMenu)
    gameMenu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Exit", command=root1.destroy)
    gameCanvas = Canvas(root1)
    gameCanvas.grid(row=0, column=0, rowspan=25, columnspan=25)
    gameCanvas.create_line(270, 0, 270, 300, fill="red")
    gameCanvas.create_text(320, 30, width=95, text="Please set the initial conditions in the grid",
                           font=("Helvetica 8"))
    for i in range(25):
        for j in range(25):
            gameCanvas.create_oval(((10 * Area[i][j].x) + 5), ((10 * Area[i][j].y) + 5),
                                   ((10 * Area[i][j].x) + 15), ((10 * Area[i][j].y) + 15),
                                   activefill="red")
            gameCanvas.bind("<Button-1>", callback)
    nextStepButton = Button(root1, text="Begin generation",
                           font=("Helvetica 8"), command=main)
    nextStepButton.grid(row=26, column=12)
    root1.mainloop()


def main():
    global Area, root1
    root1.destroy()
    Moore(Area)
    root = Tk()
    root.geometry("400x300+350+150")
    Window(root, Area)
    root.mainloop()


if __name__ == "__main__":
    initializer()
