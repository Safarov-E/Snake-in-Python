import random
from tkinter import *
from PIL import Image, ImageTk

WIDTH = 1000
HEIGHT = 1000
BODYSIZE = 50
STARTDELAY = 200
LENGTH = 3

counBodyW = WIDTH / BODYSIZE
counBodyH = HEIGHT / BODYSIZE
x = [0] * int(counBodyW)
y = [0] * int(counBodyW)

class Snake(Canvas):
    headImage = False
    head = False
    body = False
    apple = False
    delay = 0
    direction = 'Right'
    loss = False

    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background="black", highlightthickness=0)
        self.focus_get()
        self.bind_all("<Key>", self.onKeyPressed)
        self.loadResources()
        self.beginplay()
        self.pack()

    def loadResources(self):
        self.headImage = Image.open('./images/head.png')
        self.head = ImageTk.PhotoImage(self.headImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.body = ImageTk.PhotoImage(Image.open('./images/body.png').resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.apple = ImageTk.PhotoImage(Image.open('./images/apple.png').resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

    def beginplay(self):
        self.delay = STARTDELAY
        self.direction = "Right"
        self.loss = False

        self.delete(ALL)
        self.spawnActors()

    def spawnActors(self):

        self.spawnApple()

        x[0] = int(counBodyW / 2) * BODYSIZE
        y[0] = int(counBodyH / 2) * BODYSIZE
        for i in range(1, LENGTH):
            x[i] = x[0] - BODYSIZE * i
            y[i] = y[0]
        self.create_image(x[0], y[0], image=self.head, anchor="nw", tag="head")
        for i in range(1, LENGTH):
            self.create_image(x[i], y[i], image=self.body, anchor="nw", tag="body")
    
    def spawnApple(self):
        apple = self.find_withtag("apple")
        if apple:
            self.delete(apple[0])
        rx = random.randint(0, counBodyW - 1)
        ry = random.randint(0, counBodyH - 1)
        self.create_image(rx * BODYSIZE, ry * BODYSIZE, anchor="nw", image=self.apple, tag="apple")
        
    def onKeyPressed(self, event):
        pass

root = Tk()
root.title("Змейка")

root.board = Snake()

root.resizable(False, False)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - WIDTH / 2)
y = int(hs / 2 - HEIGHT / 2)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()