import turtle
import time
import random

List=[]
Score = 0
high_score = 0

w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(width=600, height=600)
w.bgcolor("green")
w.tracer(0)

yn = turtle.Turtle()
yn.speed(0)
yn.shape("square")
yn.color("black")
yn.penup()
yn.goto(0, 0)
yn.direction = "stop"

def move():
    if yn.direction == "up":
        y = yn.ycor()
        yn.sety(y + 20)

    if yn.direction == "down":
        y = yn.ycor()
        yn.sety(y - 20)

    if yn.direction == "right":
        x = yn.xcor()
        yn.setx(x + 20)

    if yn.direction == "left":
        x = yn.xcor()
        yn.setx(x - 20)

def go_up():
    if yn.direction != "down":
        yn.direction = "up"

def go_down():
    if yn.direction != "up":
        yn.direction = "down"

def go_right():
    if yn.direction != "left":
        yn.direction = "right"

def go_left():
    if yn.direction != "right":
        yn.direction = "left"

w.listen()
w.onkeypress(go_up, "Up")
w.onkeypress(go_down, "Down")
w.onkeypress(go_right, "Right")
w.onkeypress(go_left, "Left")

point = turtle.Turtle()
point.speed(0)
point.shape("square")
point.color("red")
point.penup()
point.goto(0, 100)

def collect():
    if yn.distance(point) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        point.goto(x, y)

        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("square")
        tail.color("grey")
        tail.penup()
        List.append(tail)

        global Score
        global high_score

        Score += 5
        if Score > high_score:
            high_score = Score
            w.title("Score: {}  High Score: {}".format(Score, high_score))
    
    length = len(List)
    for indis in range(length - 1, 0, -1):
        x = List[indis - 1].xcor()
        y = List[indis - 1].ycor()
        List[indis].goto(x, y)

    if len(List) > 0:
        x = yn.xcor()
        y = yn.ycor()
        List[0].goto(x, y)
    
def start():
    time.sleep(0.1)
    yn.goto(0, 0)
    yn.direction = "stop"
    

    for tail in List:
        tail.goto(1000, 1000)
    List.clear()
    Score = 0
    w.title("Score: {}  High Score: {}".format(Score, high_score))

while True:
    w.update()
    collect()
    move()
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        start()
    for tail in List:
        if tail.distance(yn) < 20:
            start()
    time.sleep(0.1)

w.mainloop()



