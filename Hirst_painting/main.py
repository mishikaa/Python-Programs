# import colorgram

# colors = colorgram.extract('Hirst_painting\image.jpg',30) #Extracting 30 colors from image.jpg
# #.extract() finds two values i.e rgb & hsl values and store it in a list but we do not require hsl values

# rgb_colors = [] #Creating an empty list to store rgb values

# for color in colors :
#     r = color.rgb.r #Extracting the r value from rgb in 1st color and so on..
#     g = color.rgb.g #Extracting the g value from rgb in 1st color and so on..
#     b = color.rgb.b #Extracting the b value from rgb in 1st color and so on..
#     new_color = (r,g,b) #Storing rgb values of each color in a tuple
#     rgb_colors.append(new_color) #Appending the tuple containing rgb values of each color in the list


color_list = [ (182, 65, 34), (213, 149, 97), (14, 24, 42), (239, 208, 94), (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), 
(84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70), 
(167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24), (79, 70, 43), (183, 196, 189), 
(119, 121, 147),(248, 196, 4) ] #Extracted using color.extract()

from turtle import Turtle,Screen
import turtle
point = Turtle()
turtle.colormode(255)

import random
point.speed("fastest")
point.penup()
point.hideturtle()

total_dots = 100
point.setheading(225)
point.forward(300)
point.setheading(0)
for dots in range(1,total_dots + 1):
    point.dot(20, random.choice(color_list))
    point.forward(50)

    if(dots % 10 == 0):
        point.left(90)
        point.forward(50)
        point.left(90)
        point.forward(500)
        point.right(180)

'''Another method to print the Hirst painting'''      
# y_coordinate = -50

# for b in range(10):
#     x_coordinate = -200 
#     for _ in range(10) :
        
#         point.goto(x_coordinate,y_coordinate)
#         print(point.dot(20,random.choice(color_list)))
#         x_coordinate += 30

#     y_coordinate += 30
    
       
screen = Screen()
screen.exitonclick()
