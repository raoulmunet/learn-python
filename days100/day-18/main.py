# from tkinter import *
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("circle")
# tim.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        # for _ in range(5):
        #     tim.forward(10)
        #     tim.penup()
        #     tim.forward(10)
        #     tim.pendown()
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random_color())
    draw_shape(shape_side_n)
    
# screen = Screen()
# screen.exitonclick()