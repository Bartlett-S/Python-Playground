from turtle import *

diameter = 40
pop_diameter = 100

def draw_balloon ():
    color("red")
    dot(diameter)

def inflate_balloon ():
    global diameter
    diameter += 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")

draw_balloon()

#Make the balloon inflate upon hitting a key
onkey(inflate_balloon, "Up")

#listen keeps the program running and listening for more input until a done condition is reached
listen()

done()