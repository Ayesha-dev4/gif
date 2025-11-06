import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
turtle.pensize(3)
def arc():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
turtle.color('red', "#FF6666")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
arc()
turtle.left(120)
arc()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

def draw_sparkle(x, y, size=10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("#C0C0C0")
    turtle.pensize(1)
    
    for i in range(5):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(72)

# --- Draw Multiple Sparkles ---
turtle.speed(0)
for _ in range(25):  # Draw 20 sparkles
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_sparkle(x, y, size=random.randint(5, 10))

turtle.hideturtle()
turtle.done()