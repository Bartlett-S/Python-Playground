from random import *
from turtle import *

bgcolor("black")
hideturtle()
speed(0)

width = window_width()
height = window_height()

def draw_star(xpos, ypos):
    penup()
    goto(xpos, ypos)
    pendown()
    dot(randrange(1,10), "white")

for x in range(100):
    xpos = randrange(round(-width/2), round(width/2))
    ypos = randrange(round(-width/2), round(height/2))
    draw_star(xpos, ypos)
    


done()