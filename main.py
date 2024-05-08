import turtle

import colorgram
from turtle import Turtle, Screen
from random import choice

colors = colorgram.extract("image.jpg", 30)

rgb_colors = []
for n in range(len(colors)):
    rgb_colors.append(colors[n].rgb)

turtle.colormode(255)

don = Turtle()
don.shape("turtle")
don.color("dark slate blue")
print(don.pos())

x = don.xcor()
y = don.ycor()
print(x, y)

don.setheading(225)
don.penup()
don.hideturtle()
don.forward(250)
# don.pendown()
don.setheading(0)

x = don.xcor()
y = don.ycor()
print(x, y)
a = x
don.speed('fastest')


for i in range(10):
    don.setposition(x, y)
    # don.pendown()
    for j in range(10):
        don.teleport(x)
        don.dot(20, choice(rgb_colors))
        x = x+50
    # don.penup()
    y = y+50
    x = a

# don.showturtle()
print(don.pos())
screen_2 = Screen()
screen_2.exitonclick()

# first_color = colors[0]
# print(first_color.rgb)
# print(first_color.rgb[0])
# print(first_color.hsl)
# print(first_color.proportion)
