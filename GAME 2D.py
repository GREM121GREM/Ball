from tkinter import*
from tkinter import ttk
import random
import time

screen = Tk()
screen.title("Ball")
screen.resizable(False, False)
screen.wm_attributes("-topmost", 1)
canvas = Canvas(width=750, height=800, bg="lightgray")
canvas.pack()
screen.update()

class Ball:
    def __init__(self, canvas, color, platform, score):
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.hit_bottom = False
        self.id = self.canvas.create_oval(0,0,20,20, fill=color)
        self.canvas.move(self.id, 490, 200)
        numbers = (-5,-4,-3,-2,2,5,3,53,7,8,42,4,5)
        self.x = random.choice(numbers)
        self.y = -3
        self.canvas_w = self.canvas.winfo_width()
        self.canvas_h = self.canvas.winfo_height()

    def hit_platform(self, position):
        position_platform = self.canvas.coords(self.platform.id)
        if position[2]>=position_platform[0] and position[0]<=position_platform[2]:
            if position[3]>=position_platform[1] and position[3]<=position_platform[3]:
                self.score.hit()
                return True
        else:
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[1]<=0:
            self.y = 4
        elif position[3]>=self.canvas_h:
            self.x = 0
            self.y = 0
            self.canvas.create_text(370, 350, text="Вы проиграли", font=("Courier", 25), fill="red")
            self.hit_bottom = True
        elif position[0]<=0:
            self.x = 6
        elif position[2]>=self.canvas_w:
            self.x = -4
        if self.hit_platform(position):
            self.y = -9

class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.canvas_w = self.canvas.winfo_width()
        self.canvas_h = self.canvas.winfo_height()
        self.id = self.canvas.create_rectangle(0,0,200,20, fill=color, outline=color)
        self.canvas.move(self.id, self.canvas_w/2-200/2, 600)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = self.canvas.coords(self.id)
        if position[0]<=0:
            self.x = 0
        elif position[2]>=self.canvas_w:
            self.x = 0
    def left(self, event):
        self.x = -5

    def right(self, event):
        self.x = 5

class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.id = self.canvas.create_text(0, 0, text=f"{self.score}", font=("Arial",50))
        self.canvas.move(self.id, 720, 30)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


platform = Platform(canvas, "yellow")
score = Score(canvas, "black")
ball = Ball(canvas, "white", platform, score)

while True:
    if not ball.hit_bottom:
        ball.draw()
        platform.draw()
    else:
        time.sleep(3)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)
