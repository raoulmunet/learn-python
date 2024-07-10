# import colorgram

# # Extract colors from an image
# colors = colorgram.extract('image.jpg', 100)  # Extract the top 6 colors from the image

# # Print the colors
# rgb_colors = []
# for color in colors:
#     rgb = color.rgb  # Tuple of (r, g, b)
#     rgb_color = (rgb[0], rgb[1], rgb[2])
#     rgb_colors.append(rgb_color)
# print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# tim.shape("circle")
tim.speed('fastest')

color_list = [(132, 165, 204), (26, 42, 64), (207, 222, 235), (230, 149, 94), (204, 136, 148), (238, 210, 86), (40, 108, 156), (134, 183, 162), (172, 60, 47), (236, 214, 219), (157, 32, 30), (51, 39, 43), (177, 28, 30), (218, 230, 227), (139, 69, 78), (38, 61, 54), (238, 166, 155), (231, 164, 168), (54, 121, 106), (215, 82, 74), (2, 103, 73), (196, 97, 105), (25, 62, 116), (61, 55, 51), (17, 83, 107), (181, 188, 214), (110, 126, 151), (169, 204, 191), (88, 148, 135), (54, 148, 192), (150, 205, 226), (63, 66, 59), (127, 130, 124)]

origin = (-400, -400)
step = 50
rows = 10
columns = 10
dot_size = 30

def random_color():
    return random.choice(color_list)

def move_turtle(x, y):
    tim.penup()  # Lift the pen so it doesn't draw
    tim.goto(x, y)  # Move the turtle to the specified position
    tim.pendown() 

def draw_circle():
    tim.dot(dot_size, random_color())

move_turtle(origin[0], origin[1])

for _ in range(rows):
    move_turtle(origin[0], tim.position()[1] + step)
    for _ in range(columns):
        draw_circle()
        move_turtle(tim.position()[0] + step, tim.position()[1])

screen = t.Screen()
screen.exitonclick()