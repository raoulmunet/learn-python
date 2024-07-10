# from tkinter import *
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# tim.shape("circle")
tim.speed('fastest')

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

def move_turtle(x, y):
    tim.penup()  # Lift the pen so it doesn't draw
    tim.goto(x, y)  # Move the turtle to the specified position
    tim.pendown() 

def draw_spiro(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

move_turtle(-400, 350)
for shape_side_n in range(3, 11):
    tim.color(random_color())
    draw_shape(shape_side_n)

move_turtle(100, 200)
draw_spiro(10)
    
screen = t.Screen()
screen.exitonclick()