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
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background="black")
        self.focus_get()
        self.bind_all("<Key>", self.onKeyPressed)
        self.loadResources()
        self.beginplay()

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

    def onKeyPressed(self, event):
        pass

root = Tk()
root.title("Змейка")

root.board = Snake()

root.resizable(False, False)

w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()