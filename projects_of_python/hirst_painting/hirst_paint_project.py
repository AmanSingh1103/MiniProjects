# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image resource.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [(45, 25, 11), (16, 26, 42), (120, 91, 61), (55, 92, 146), (188, 162, 114), (14, 29, 22), (238, 234, 207), (41, 21, 29), (238, 218, 83), (227, 239, 233), (114, 169, 192), (190, 155, 43), (75, 105, 95), (223, 229, 236), (139, 172, 161), (44, 53, 110), (106, 85, 94), (238, 229, 235), (90, 72, 22), (50, 111, 220), (124, 28, 39), (167, 155, 162), (31, 173, 204), (120, 37, 25), (61, 170, 158), (234, 211, 9), (28, 84, 74), (193, 102, 77), (19, 83, 95), (140, 214, 200)]
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100



for dot_count in range(1 , number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)














screen = turtle_module.Screen()
screen.exitonclick()





