# import colorgram as cg
#
# color_list = cg.extract("Untitled.jpg", 30)
# color_palette = []
#
# for count in range(len(color_list)):
#     r = color_list[count].rgb.r
#     g = color_list[count].rgb.g
#     b = color_list[count].rgb.b
#     color = (r, g, b)
#
#     color_palette.append(color)
import turtle
import turtle as t
import random

turtle.colormode(255)
tim = t.Turtle()

color_list = [(225, 234, 229), (175, 49, 79), (43, 97, 145), (204, 162, 95), (223, 210, 104), (136, 90, 65),
              (111, 176, 206), (177, 164, 40), (211, 132, 173), (225, 74, 51), (199, 76, 118), (90, 105, 190),
              (27, 145, 91), (125, 218, 207), (95, 157, 64), (119, 43, 70), (227, 170, 187)]
tim.hideturtle()
tim.penup()
tim.goto(-300, -250)
x=-250

tim.speed("fastest")
for i in range (11):
    for j in range(13):

        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()
    tim.penup()
    x+=50
    tim.goto(-300,x )



screen = t.Screen()
screen.screensize(10, 10)
screen.exitonclick()
